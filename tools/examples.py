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
on PATH); it must be the 3DCraft commit pinned in tools/pin.json. Exit code 0 when all passed.
"""

import argparse
import json
import os
import re
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
PREVIEW_LOOK_KEYS = {"light", "rotation"}

TIERS = ("simple", "difficult", "complex")
BUDGET_LOAD_S = {"simple": 1.0, "difficult": 2.0, "complex": 4.0}
BUDGET_BYTES = 1_000_000
STEP_GUIDE = {"simple": 40, "difficult": 100, "complex": 200}
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

_cli = None


def die(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(2)


def cli():
    """The craft3d-cli binary, checked once against the pinned commit."""
    global _cli
    if _cli is None:
        path = os.environ.get("CRAFT3D_CLI") or shutil.which("craft3d-cli")
        if not path or not os.access(path, os.X_OK):
            die("craft3d-cli not found: put it on PATH or set CRAFT3D_CLI")
        # The binary carries the commit it was built from (for bug reports), but does not print it.
        if PIN["commit"][:12].encode() not in Path(path).read_bytes():
            die(f"{path} is not 3DCraft {PIN['commit'][:12]} (tools/pin.json): install that build "
                "or ask the coordinator to move the pin")
        _cli = path
    return _cli


def run_cli(args, cwd, memory="3G", timeout=900):
    """Runs craft3d-cli under a memory cap and a timeout; returns (result, seconds)."""
    command = [cli()] + [str(a) for a in args]
    if shutil.which("systemd-run") and not os.environ.get("CRAFT3D_NO_CAP"):
        command = ["systemd-run", "--user", "--scope", "-q", "-p", f"MemoryMax={memory}",
                   "-p", "MemorySwapMax=0", "timeout", str(timeout)] + command
    elif shutil.which("timeout"):
        command = ["timeout", str(timeout)] + command
    start = time.monotonic()
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    return result, time.monotonic() - start


def explain_failure(result, what):
    code = result.returncode
    reason = {137: "killed at the memory cap", 124: "timed out"}.get(code, f"exit code {code}")
    tail = "\n".join((result.stdout.strip().splitlines() + result.stderr.strip().splitlines())[-8:])
    return f"{what}: {reason}\n{tail}"


def example_ids(given):
    if given:
        for i in given:
            if not (EXAMPLES / i / "build.json").is_file():
                die(f"no example {i} (examples/{i}/build.json)")
        return list(given)
    return sorted(p.parent.name for p in EXAMPLES.glob("*/build.json"))


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
    building = target / f".{eid}.building.3dcraft"
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
            {k: report.get(k) for k in ("problems", "assertions")}, indent=1)[:3000])
    exports = meta.get("exports", [])
    if exports:
        args = ["run", building]
        for export in exports:
            params = {k: v for k, v in export.items() if k != "command"}
            command = export.get("command", "file.export")
            if command not in EXPORT_COMMANDS:
                raise CheckError(f"export command {command!r} must be one of {EXPORT_COMMANDS}")
            path = params.get("path", "")
            if not path.startswith("exports/"):
                raise CheckError(f"export path {path!r} must start with exports/")
            (target / path).parent.mkdir(parents=True, exist_ok=True)
            args += ["--cmd", command, "--params", json.dumps(params)]
        result, _ = run_cli(args, cwd=target)
        if result.returncode != 0:
            raise CheckError(explain_failure(result, "exports failed"))
    final = target / f"{eid}.3dcraft"
    building.replace(final)
    result, load_s = run_cli(["info", final], cwd=target)
    if result.returncode != 0:
        raise CheckError(explain_failure(result, "craft3d-cli info failed"))
    doc = manifest(final)
    ids = Counter(step_id(s) for s in script)
    assertions = report.get("assertions", {})
    return {
        "steps": len(script),
        "variables": ids["variable.set"],
        "parameters": ids["variable.publish"],
        "features": len(doc.get("document", {}).get("features", [])),
        "assertions": assertions.get("count", ids["assert.add"]),
        "warnings": len(assertions.get("unproven", [])),
        "build_s": round(seconds, 2),
        "load_s": round(load_s, 2),
        "file_bytes": final.stat().st_size,
    }, doc, report


def lint(eid, meta, doc, stats, script):
    """Returns (errors, warnings) for names, budgets and the meta.json fields."""
    errors, warnings = [], []
    for key in REQUIRED_META:
        if key not in meta or meta[key] in ("", None):
            errors.append(f"meta.json: missing {key}")
    if meta.get("id") != eid:
        errors.append(f"meta.json: id is {meta.get('id')!r}, not {eid!r}")
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
    if stats["load_s"] > BUDGET_LOAD_S[tier] and not meta.get("budget_exception"):
        errors.append(f"loads in {stats['load_s']} s, budget {BUDGET_LOAD_S[tier]} s for {tier}")
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
            meta["craft3d"] = {"commit": PIN["commit"][:12],
                               "format_version": doc.get("format_version")}
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
            document = directory / f"{eid}.3dcraft"
            if not document.is_file():
                raise CheckError(f"no {eid}.3dcraft: run build first")
            params = dict(RENDER)
            look = dict(LOOK)
            for key, value in meta.get("preview", {}).items():
                if key == "look":
                    look.update({k: v for k, v in value.items() if k in PREVIEW_LOOK_KEYS})
                elif key in PREVIEW_KEYS:
                    params[key] = value
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
            for name in REQUIRED_FILES + (f"{eid}.3dcraft", "preview.png"):
                if not (directory / name).is_file():
                    problems.append(f"missing {name}")
            meta = read_json(directory / "meta.json")
            script = read_json(directory / "build.json")
            with tempfile.TemporaryDirectory(prefix=f"check-{eid}-") as scratch:
                stats, doc, _ = build_into(eid, Path(scratch), meta)
                errors, warnings = lint(eid, meta, doc, stats, script)
                problems += errors
                notes += warnings
                committed = directory / f"{eid}.3dcraft"
                rebuilt = Path(scratch) / f"{eid}.3dcraft"
                if committed.is_file() and committed.read_bytes() != rebuilt.read_bytes():
                    problems.append(f"{eid}.3dcraft is stale: run build")
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
        ids |= {f"measure.{step_params(s).get('measure')}" for s in script
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
        rows.append((score if score is not None else 99, TIERS.index(meta.get("tier", "complex"))
                     if meta.get("tier") in TIERS else 3, meta.get("title", eid), eid, meta))
    rows.sort()
    lines = ["| | Example | Domain | Difficulty |", "|---|---|---|---|"]
    for score, _, title, eid, meta in rows:
        picture = (f'<img src="examples/{eid}/preview.png" width="240" alt="{title}">'
                   if (EXAMPLES / eid / "preview.png").is_file() else "")
        shown = f"{score}/10" if score != 99 else "not scored yet"
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
