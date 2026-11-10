#!/usr/bin/env python3
"""Build, render and check the 3DCraft examples (AGENTS.md).

  tools/examples.py build    [ID ...]   build.json -> ID.3dcraft and its exports; document.check;
                                        stats into meta.json
  tools/examples.py render   [ID ...]   ID.3dcraft -> preview.png in the gallery look
  tools/examples.py check    [ID ...]   rebuild in a scratch folder and check what AGENTS.md asks
                                        (--quick skips check-range)
  tools/examples.py coverage            the 3DCraft commands the examples use, and those none uses
  tools/examples.py readme              rewrite the gallery table in README.md from the meta.json files

Without an ID: every example under examples/. Every craft3d-cli run is capped in memory
(systemd-run, when there is one) and in time. CRAFT3D_CLI names the binary (default: craft3d-cli
on PATH); by what its --version reports, it must be the 3DCraft commit pinned in tools/pin.json,
or the release named there, with the pinned file format. Linux and macOS only. Exit code 0 when
all passed.
"""

import argparse
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
PIN = json.loads((ROOT / "tools" / "pin.json").read_text())

# The gallery look (AGENTS.md, The preview): the look of 3DCraft's start-screen thumbnails,
# larger and smoother. meta.json "preview" may change only the framing keys below.
RENDER = {"width": 1600, "height": 1200, "view": "iso", "projection": "perspective", "zoom": 1,
          "renderer": "cpu"}
LOOK = {"mode": "studio", "environment": "workshop", "tonemap": "aces", "exposure": 0.5,
        "background": "plain", "accumulate": 8}
PREVIEW_KEYS = {"view", "zoom", "camera", "projection", "box"}
PREVIEW_LOOK_KEYS = {"light", "rotation", "reflections"}

TIERS = ("simple", "difficult", "complex")
BUDGET_LOAD_S = {"simple": 1.0, "difficult": 2.0, "complex": 4.0}
MEASURED_AT_LOAD = 0.0  # the 1-minute load average when the last load time was measured
BUDGET_BYTES = 1_000_000
STEP_GUIDE = {"simple": 50, "difficult": 120, "complex": 250}
REQUIRED_META = ("id", "title", "summary", "description", "domain", "process", "tier",
                 "difficulty", "standards", "materials")
REQUIRED_FILES = ("build.json", "meta.json", "README.md", "prompt.md")
# Families outside this repository's scope (no Jigs, no assemblies) or session-only.
NOT_IN_SCOPE = ("assembly.", "instance.", "mate.", "joint.", "coupling.", "motion.", "jig.",
                "recovery.", "session.", "agent.", "select.", "history.", "edit.", "file.list",
                "file.activate", "file.close", "file.open", "file.new", "file.save", "file.import",
                "view.scrub", "view.motion", "view.trace", "view.drive", "view.replay",
                "view.pick", "measure.joint", "measure.pose", "param.", "font.")
# Commands that edit or query rather than model: a build script has no use for them.
NOT_MODELLING = ("variable.delete", "variable.rename", "variable.unpublish", "feature.edit",
                 "feature.suppress", "feature.move", "feature.delete", "feature.rename",
                 "document.inspect", "document.measure", "document.edges", "document.sample",
                 "document.setTolerance", "view.render", "sketch.edit", "sketch.delete",
                 "sketch.inspect", "sketch.textEdit", "material.presets", "datum.references",
                 "fold.edit", "fold.inspect", "assert.edit", "assert.delete", "assert.list",
                 "output.list", "set.edit", "set.remove", "set.list", "table.delete",
                 "table.rename", "table.list")
EXPORT_COMMANDS = ("file.export", "cut.export")
DEFAULT_NAME = re.compile(r"^[A-Za-z]+[0-9]+$")
VARIABLE_NAME = re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]+)*$")
GALLERY_START = "<!-- gallery:start -->"
GALLERY_END = "<!-- gallery:end -->"

# What `craft3d-cli --version` prints: the program, the version, the commit when the build knows it, the file format.
VERSION_LINE = re.compile(r"^craft3d-cli (?P<version>\S+) \((?:(?P<commit>[0-9A-Za-z]+), )?format (?P<format>[0-9]+)\)$")

_cli = None
_build = None  # (version, commit or None, format) of _cli


def die(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(2)


def capped(command, memory, timeout):
    """command under a memory cap (systemd-run, where there is one) and a timeout: every craft3d-cli run of the tool
    goes through here. CRAFT3D_NO_CAP=1 leaves the memory cap out; CRAFT3D_SLICE names a shared slice that caps
    parallel agents together (AGENTS.md §3)."""
    command = [str(c) for c in command]
    if shutil.which("systemd-run") and not os.environ.get("CRAFT3D_NO_CAP"):
        slice_ = [f"--slice={os.environ['CRAFT3D_SLICE']}"] if os.environ.get("CRAFT3D_SLICE") else []
        return ["systemd-run", "--user", "--scope", "-q", *slice_, "-p", f"MemoryMax={memory}",
                "-p", "MemorySwapMax=0", "timeout", str(timeout)] + command
    if shutil.which("timeout"):
        return ["timeout", str(timeout)] + command
    return command


def version_of(path):
    """What `craft3d-cli --version` prints, and what it says: (line, (version, commit or None, format) or None).
    The line is `craft3d-cli 0.1.0 (8c8383e9c89a, format 69)`; a build that does not know its commit leaves it out."""
    try:
        result = subprocess.run(capped([path, "--version"], "1G", 60), capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        return str(e), None
    lines = result.stdout.strip().splitlines()
    line = lines[-1].strip() if lines else (result.stderr.strip() or f"exit code {result.returncode}")
    match = VERSION_LINE.match(line)
    if result.returncode != 0 or not match:
        return line, None
    return line, (match["version"], match["commit"], int(match["format"]))


def pinned(build):
    """How a build meets tools/pin.json: "commit" when it is the pinned commit (the check the examples were built
    with), "release" when it reports itself as the pinned release, or None; either way with the pinned file format.
    `--version` marks nothing else that tells a release build from a development build of the same version."""
    version, commit, file_format = build
    if file_format != PIN["format_version"]:
        return None
    pin = PIN["commit"].lower()
    if commit and len(commit) >= 12 and (pin.startswith(commit.lower()) or commit.lower().startswith(pin)):
        return "commit"
    if PIN.get("release") and version == PIN["release"]:
        return "release"
    return None


def cli():
    """The craft3d-cli binary, checked once against tools/pin.json by what its --version reports."""
    global _cli, _build
    if _cli is None:
        path = os.environ.get("CRAFT3D_CLI") or shutil.which("craft3d-cli")
        if not path or not os.access(path, os.X_OK):
            die("craft3d-cli not found: put it on PATH or set CRAFT3D_CLI (README.md, Rebuild and check)")
        line, build = version_of(path)
        how = pinned(build) if build else None
        if how is None:
            release = f" or the release {PIN['release']}" if PIN.get("release") else ""
            die(f"{path} reports {line!r}, not 3DCraft {PIN['commit'][:12]}{release} with file format "
                f"{PIN['format_version']}, the build this repository is pinned to (tools/pin.json): the committed "
                "files and their checks are what that build produces, and another build may write other bytes. "
                "Install that build (README.md, Rebuild and check); a build.json itself runs in any 3DCraft with "
                "craft3d-cli run --script")
        if how == "release":
            print(f"note: {line}: accepted as 3DCraft {PIN['release']}, the release in tools/pin.json, but it is "
                  f"not the pinned commit {PIN['commit'][:12]}: if its files differ in bytes, check reports them "
                  "as stale", file=sys.stderr)
        _cli, _build = path, build
    return _cli


def built_with(file_format):
    """meta.json's `craft3d`: the build that wrote the files, as its --version reports it."""
    version, commit, _ = _build
    return {"commit": commit[:12] if commit else None, "version": version, "format_version": file_format}


def run_cli(args, cwd, memory="3G", timeout=900):
    """Runs craft3d-cli under a memory cap and a timeout; returns (result, seconds)."""
    command = capped([cli()] + list(args), memory, timeout)
    start = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    # CPU time of the run (all threads): what a single-threaded host such as the web build pays.
    result.cpu_seconds = (after.ru_utime - before.ru_utime) + (after.ru_stime - before.ru_stime)
    return result, time.monotonic() - start


def explain_failure(result, what):
    code = result.returncode
    # The cap's kill reaches the whole scope: systemd-run itself dies by SIGKILL (-9), or timeout reports it (137).
    reason = {137: "killed at the memory cap", -9: "killed at the memory cap", 124: "timed out"}.get(
        code, f"exit code {code}")
    tail = "\n".join((result.stdout.strip().splitlines() + result.stderr.strip().splitlines())[-8:])
    return f"{what}: {reason}\n{tail}"


def slug(folder):
    """An example's id: its folder's name without the leading number (`01-socket-head-cap-screw`)."""
    return re.sub(r"^[0-9]{2}-", "", folder)


def example_ids(given):
    """The examples' folders, in their order; a given name may be the folder or the id."""
    folders = sorted(p.parent.name for p in EXAMPLES.glob("*/build.json")
                     if not p.parent.is_symlink())
    if not given:
        return folders
    chosen = []
    for name in given:
        match = [f for f in folders if name in (f, slug(f))]
        if not match:
            die(f"no example {name} (examples/<NN>-{name}/build.json)")
        chosen.append(match[0])
    return chosen


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError) as e:
        raise CheckError(f"{path.relative_to(ROOT)}: {e}")


def write_meta(directory, meta):
    (directory / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")


def step_id(step):
    if isinstance(step, list) and step:
        return step[0]
    if isinstance(step, dict):
        return step.get("command", "?")
    return "?"


def step_params(step):
    if isinstance(step, list) and len(step) > 1:
        return step[1]
    if isinstance(step, dict):
        return step.get("params", {})
    return {}


def deflate_zip(path):
    """Rewrites a ZIP-based export (3MF) with deflate: 3DCraft stores it uncompressed (F-080). The entries,
    their order, names and dates stay as they are, so the result is as deterministic as the export."""
    with zipfile.ZipFile(path) as z:
        entries = [(info, z.read(info.filename)) for info in z.infolist()]
    temporary = path.with_suffix(path.suffix + ".deflating")
    with zipfile.ZipFile(temporary, "w") as z:
        for info, data in entries:
            copy = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            copy.external_attr = info.external_attr
            copy.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(copy, data, compresslevel=9)
    temporary.replace(path)


def manifest(path):
    with zipfile.ZipFile(path) as z:
        return json.loads(z.read("manifest.json"))


class CheckError(Exception):
    pass


def build_into(eid, target, meta):
    """Builds examples/eid/build.json into target/eid.3dcraft (and its exports). Returns stats."""
    source = EXAMPLES / eid
    script = read_json(source / "build.json")
    if not isinstance(script, list) or not script:
        raise CheckError("build.json must be a non-empty JSON list of steps")
    if step_id(script[-1]) != "document.check":
        raise CheckError("build.json must end with document.check")
    building = target / f".{slug(eid)}.building.3dcraft"
    new = json.dumps({"units": meta.get("units", "mm")})
    result, seconds = run_cli(["run", "--new", new, "--script", source / "build.json",
                               "--out", building], cwd=target)
    if result.returncode != 0:
        building.unlink(missing_ok=True)
        raise CheckError(explain_failure(result, "build.json failed"))
    lines = [line for line in result.stdout.splitlines() if line.strip()]
    try:
        report = json.loads(lines[-1])
    except (IndexError, ValueError):
        building.unlink(missing_ok=True)
        raise CheckError("no document.check result in the output")
    if not report.get("ok"):
        building.unlink(missing_ok=True)
        raise CheckError("document.check is not ok:\n" + json.dumps(
            {k: report.get(k) for k in ("problems", "assertionSummary")}, indent=1)[:3000])
    exports = meta.get("exports", [])
    if exports:
        # Exports at the defaults share one run; an export with "values" (public parameters, as param.set
        # takes them) gets a run of its own, so its values never leak into another export.
        runs = [["run", building]]
        for export in exports:
            params = {k: v for k, v in export.items() if k not in ("command", "values")}
            command = export.get("command", "file.export")
            if command not in EXPORT_COMMANDS:
                raise CheckError(f"export command {command!r} must be one of {EXPORT_COMMANDS}")
            path = params.get("path", "")
            if not path.startswith("exports/"):
                raise CheckError(f"export path {path!r} must start with exports/")
            (target / path).parent.mkdir(parents=True, exist_ok=True)
            step = ["--cmd", command, "--params", json.dumps(params)]
            if export.get("values"):
                runs.append(["run", building, "--cmd", "param.set",
                             "--params", json.dumps({"values": export["values"]})] + step)
            else:
                runs[0] += step
        for args in runs:
            if len(args) == 2:
                continue
            result, _ = run_cli(args, cwd=target)
            if result.returncode != 0:
                raise CheckError(explain_failure(result, "exports failed"))
        for export in exports:
            if export.get("path", "").endswith(".3mf"):
                deflate_zip(target / export["path"])
    final = target / f"{slug(eid)}.3dcraft"
    building.replace(final)
    # The least of two openings: other work on the machine only ever adds time.
    global MEASURED_AT_LOAD
    load_s = load_cpu_s = None
    for _ in range(2):
        result, seconds = run_cli(["info", final], cwd=target)
        if result.returncode != 0:
            raise CheckError(explain_failure(result, "craft3d-cli info failed"))
        load_s = seconds if load_s is None else min(load_s, seconds)
        load_cpu_s = result.cpu_seconds if load_cpu_s is None else min(load_cpu_s, result.cpu_seconds)
    MEASURED_AT_LOAD = os.getloadavg()[0]
    doc = manifest(final)
    ids = Counter(step_id(s) for s in script)
    # document.check reports its assertions under assertionSummary (since 3DCraft 150f0015, F-151).
    assertions = report.get("assertionSummary") or {}
    return {
        "steps": len(script),
        "variables": ids["variable.set"],
        "parameters": ids["variable.publish"],
        "features": len(doc.get("document", {}).get("features", [])),
        "assertions": assertions.get("count", ids["assert.add"]),
        "warnings": len(assertions.get("unproven", [])),
        "build_s": round(seconds, 2),
        "load_s": round(load_s, 2),
        "load_cpu_s": round(load_cpu_s, 2),
        "file_bytes": final.stat().st_size,
    }, doc, report


def lint(eid, meta, doc, stats, script):
    """Returns (errors, warnings) for names, budgets and the meta.json fields."""
    errors, warnings = [], []
    for key in REQUIRED_META:
        if key not in meta or meta[key] in ("", None):
            errors.append(f"meta.json: missing {key}")
    if meta.get("id") != slug(eid):
        errors.append(f"meta.json: id is {meta.get('id')!r}, not {slug(eid)!r}")
    tier = meta.get("tier")
    if tier not in TIERS:
        errors.append(f"meta.json: tier must be one of {', '.join(TIERS)}")
        tier = "complex"
    for key in meta.get("preview", {}):
        if key == "look":
            bad = set(meta["preview"]["look"]) - PREVIEW_LOOK_KEYS
            if bad:
                errors.append(f"meta.json: preview.look may only set {sorted(PREVIEW_LOOK_KEYS)}")
        elif key not in PREVIEW_KEYS:
            errors.append(f"meta.json: preview may only set {sorted(PREVIEW_KEYS)} and look")
    body = doc.get("document", {})
    tools = {f.get("kind", {}).get("tool") for f in body.get("features", [])
             if f.get("kind", {}).get("type") == "boolean"}
    for feature in body.get("features", []):
        name = feature.get("name", "")
        if DEFAULT_NAME.match(name):
            if feature.get("id") in tools:
                warnings.append(f"feature {name!r} keeps its automatic name (the tool of a boolean)")
            else:
                errors.append(f"feature {name!r} has an automatic name: name it for its intent")
    for assertion in body.get("assertions", []):
        if DEFAULT_NAME.match(assertion.get("name", "")):
            errors.append(f"assertion {assertion.get('name')!r} has an automatic name")
    for variable in body.get("variables", []):
        name = variable.get("name", "")
        if not VARIABLE_NAME.match(name) or len(name) < 3:
            errors.append(f"variable {name!r}: use a descriptive snake_case name of 3+ letters")
    if not any(step_id(s) == "document.info" for s in script):
        errors.append("build.json: no document.info (title, description, author, licence)")
    # Timings taken while the machine is busy (load average over half its CPUs) only warn: other work
    # inflates them. Commit stats measured at a quiet moment.
    busy = MEASURED_AT_LOAD > (os.cpu_count() or 1) / 2
    timing = warnings if busy else errors
    busy_note = (f" (measured at load average {MEASURED_AT_LOAD:.1f} on {os.cpu_count()} CPUs: "
                 "re-measure at a quiet moment)") if busy else ""
    if stats["load_s"] > BUDGET_LOAD_S[tier] and not meta.get("budget_exception"):
        timing.append(f"loads in {stats['load_s']} s, budget {BUDGET_LOAD_S[tier]} s for {tier}{busy_note}")
    cpu_budget = 3 * BUDGET_LOAD_S[tier]
    if stats.get("load_cpu_s", 0) > cpu_budget and not meta.get("budget_exception"):
        timing.append(f"loads in {stats['load_cpu_s']} s of CPU (the single-threaded web build's time), "
                      f"budget {cpu_budget} s for {tier}{busy_note}")
    if stats["file_bytes"] > BUDGET_BYTES and not meta.get("budget_exception"):
        errors.append(f"{stats['file_bytes']} bytes, budget {BUDGET_BYTES}")
    if stats["steps"] > STEP_GUIDE[tier]:
        warnings.append(f"{stats['steps']} steps, guide {STEP_GUIDE[tier]} for {tier}")
    if not 2 <= stats["parameters"] <= 4:
        warnings.append(f"{stats['parameters']} public parameters (AGENTS.md asks 2 to 4)")
    if stats["warnings"]:
        warnings.append(f"{stats['warnings']} assertion(s) not proven: explain in the README")
    return errors, warnings


def cmd_build(ids):
    failed = 0
    for eid in ids:
        directory = EXAMPLES / eid
        try:
            meta = read_json(directory / "meta.json")
            stats, doc, _ = build_into(eid, directory, meta)
            meta["stats"] = stats
            meta["craft3d"] = built_with(doc.get("format_version"))
            write_meta(directory, meta)
            errors, warnings = lint(eid, meta, doc, stats, read_json(directory / "build.json"))
            for w in warnings:
                print(f"{eid}: warning: {w}")
            for e in errors:
                print(f"{eid}: ERROR: {e}")
            print(f"{eid}: built, {stats['steps']} steps, {stats['features']} features, "
                  f"load {stats['load_s']} s, {stats['file_bytes']} bytes")
            failed += bool(errors)
        except CheckError as e:
            print(f"{eid}: FAILED: {e}")
            failed += 1
    return failed


def cmd_render(ids):
    failed = 0
    for eid in ids:
        directory = EXAMPLES / eid
        try:
            meta = read_json(directory / "meta.json")
            document = directory / f"{slug(eid)}.3dcraft"
            if not document.is_file():
                raise CheckError(f"no {eid}.3dcraft: run build first")
            params = dict(RENDER)
            look = dict(LOOK)
            for key, value in meta.get("preview", {}).items():
                if key == "look":
                    look.update({k: v for k, v in value.items() if k in PREVIEW_LOOK_KEYS})
                elif key in PREVIEW_KEYS:
                    params[key] = value
            if "camera" in params:
                # A camera is the whole framing: view, zoom and projection would contradict it.
                for key in ("view", "zoom", "projection", "box"):
                    params.pop(key, None)
            params["look"] = look
            params["path"] = str(directory / "preview.png")
            result, seconds = run_cli(["run", document, "--cmd", "view.render", "--params",
                                       json.dumps(params)], cwd=directory, memory="4G",
                                      timeout=1800)
            if result.returncode != 0:
                raise CheckError(explain_failure(result, "view.render failed"))
            size = (directory / "preview.png").stat().st_size
            print(f"{eid}: preview.png, {size} bytes, {seconds:.0f} s")
        except CheckError as e:
            print(f"{eid}: FAILED: {e}")
            failed += 1
    return failed


def cmd_check(ids, quick):
    failed = 0
    for eid in ids:
        directory = EXAMPLES / eid
        problems, notes = [], []
        try:
            for name in REQUIRED_FILES + (f"{slug(eid)}.3dcraft", "preview.png"):
                if not (directory / name).is_file():
                    problems.append(f"missing {name}")
            meta = read_json(directory / "meta.json")
            script = read_json(directory / "build.json")
            with tempfile.TemporaryDirectory(prefix=f"check-{eid}-") as scratch:
                stats, doc, _ = build_into(eid, Path(scratch), meta)
                errors, warnings = lint(eid, meta, doc, stats, script)
                problems += errors
                notes += warnings
                committed = directory / f"{slug(eid)}.3dcraft"
                rebuilt = Path(scratch) / f"{slug(eid)}.3dcraft"
                if committed.is_file() and committed.read_bytes() != rebuilt.read_bytes():
                    problems.append(f"{slug(eid)}.3dcraft is stale: run build")
                for params in meta.get("exports", []):
                    path = params.get("path", "")
                    mine, fresh = directory / path, Path(scratch) / path
                    if not mine.is_file():
                        problems.append(f"missing {path}: run build")
                    elif fresh.is_file() and mine.read_bytes() != fresh.read_bytes():
                        problems.append(f"{path} is stale: run build")
                if stats["parameters"] and not quick:
                    result, seconds = run_cli(["check-range", rebuilt, "--samples", 8,
                                               "--seed", 1], cwd=scratch, memory="4G",
                                              timeout=3600)
                    if result.returncode != 0:
                        problems.append(explain_failure(result, "check-range failed"))
                    else:
                        notes.append(f"check-range passed in {seconds:.0f} s")
            score = (meta.get("difficulty") or {}).get("score")
            if score is None:
                notes.append("no difficulty score yet (the reviewer gives it)")
            if not (meta.get("prompt_test") or {}).get("result"):
                notes.append("prompt not tested yet")
        except CheckError as e:
            problems.append(str(e))
        for n in notes:
            print(f"{eid}: note: {n}")
        for p in problems:
            print(f"{eid}: PROBLEM: {p}")
        print(f"{eid}: {'FAILED' if problems else 'ok'}")
        failed += bool(problems)
    return failed


def measure_command(measure):
    """The measure.* command an assertion's or output's measure kind stands for (volumeBelow is
    measure.below, floatingGM is measure.floating, sectionArea is measure.section, ...)."""
    for prefix, command in (("floating", "measure.floating"), ("section", "measure.section"),
                            ("volumeBelow", "measure.below"), ("centroidBelow", "measure.below"),
                            ("symmetric", "measure.symmetry")):
        if measure.startswith(prefix):
            return command
    return f"measure.{measure}"


def cmd_coverage():
    result, _ = run_cli(["commands"], cwd=ROOT)
    if result.returncode != 0:
        die(explain_failure(result, "craft3d-cli commands failed"))
    every = [line.strip() for line in result.stdout.splitlines()
             if line and not line[0].isspace() and re.match(r"^[a-z]+(\.[a-zA-Z]+)+$", line.strip())]
    relevant = [c for c in every if not c.startswith(NOT_IN_SCOPE) and c not in NOT_MODELLING]
    used = Counter()
    users = {}
    for eid in example_ids([]):
        script = read_json(EXAMPLES / eid / "build.json")
        meta = read_json(EXAMPLES / eid / "meta.json")
        ids = {step_id(s) for s in script}
        ids |= {e.get("command", "file.export") for e in meta.get("exports", [])}
        # A measure used by an assertion or an output counts as its measure command.
        ids |= {measure_command(step_params(s).get("measure")) for s in script
                if step_id(s) in ("assert.add", "variable.measure")
                and isinstance(step_params(s), dict) and step_params(s).get("measure")}
        for c in ids:
            used[c] += 1
            users.setdefault(c, []).append(eid)
    print(f"{len([c for c in relevant if used[c]])} of {len(relevant)} commands in scope used")
    for c in relevant:
        mark = f"{used[c]:2d}  {', '.join(users.get(c, [])[:4])}" if used[c] else " -  UNUSED"
        print(f"  {c:32s} {mark}")
    return 0


def cmd_readme():
    rows = []
    for eid in example_ids([]):
        try:
            meta = read_json(EXAMPLES / eid / "meta.json")
        except CheckError:
            continue
        score = (meta.get("difficulty") or {}).get("score")
        if score is None:
            continue  # the gallery shows reviewed examples only
        rows.append((eid, score, meta.get("title", eid), meta))
    lines = ["| | Example | Domain | Difficulty |", "|---|---|---|---|"]
    for eid, score, title, meta in rows:
        picture = (f'<img src="examples/{eid}/preview.png" width="240" alt="{title}">'
                   if (EXAMPLES / eid / "preview.png").is_file() else "")
        shown = f"{score}/10" if score is not None else "not scored yet"
        lines.append(f"| {picture} | **[{title}](examples/{eid}/)**<br>{meta.get('description', '')}"
                     f" | {meta.get('domain', '')} | {shown} |")
    readme = ROOT / "README.md"
    text = readme.read_text()
    if GALLERY_START not in text or GALLERY_END not in text:
        die("README.md lacks the gallery markers")
    head, rest = text.split(GALLERY_START, 1)
    _, tail = rest.split(GALLERY_END, 1)
    readme.write_text(head + GALLERY_START + "\n" + "\n".join(lines) + "\n" + GALLERY_END + tail)
    print(f"README.md: {len(rows)} examples")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("action", choices=("build", "render", "check", "coverage", "readme"))
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--quick", action="store_true", help="check: skip check-range")
    args = parser.parse_args()
    if args.action == "build":
        failed = cmd_build(example_ids(args.ids))
    elif args.action == "render":
        failed = cmd_render(example_ids(args.ids))
    elif args.action == "check":
        failed = cmd_check(example_ids(args.ids), args.quick)
    elif args.action == "coverage":
        failed = cmd_coverage()
    else:
        failed = cmd_readme()
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
