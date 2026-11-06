# AGENTS.md: guide for AI agents working on the 3DCraft examples

This repository holds **21 example models** for [3DCraft](https://github.com/johancoppens/3dcraft), the
parametric CAD modeller built for AI. Together they show what 3DCraft can do, from simple to difficult to
fairly complex, across machine building, sheet metal, 3D printing, laser and CNC work, woodworking,
packaging, jewellery, architecture, naval design, product design and art. They also feed the start screen
of the 3DCraft release and its website, so each one must be **real, makeable, beautiful and light**.

Read this file, then [`CATALOGUE.md`](CATALOGUE.md) (what each example must be), then the example you work on.

## 1. Ground rules

- **Language.** The developer writes in Dutch: answer in Dutch. Everything that lands in this
  repository is English: files, names inside the models, commit messages.
- **3DCraft is pinned.** Every example is built and checked with one 3DCraft commit, recorded in
  [`tools/pin.json`](tools/pin.json) (`f4b0813c`, file format 69): the installed `craft3d-cli`
  (`~/.local/bin/craft3d-cli`). `tools/examples.py` refuses any other build. Only the coordinator moves the
  pin, after rebuilding and checking every example.
- **Do not change 3DCraft from here.** R1 is frozen. What 3DCraft gets wrong or lacks is *collected* in
  [`3DCRAFT-FEEDBACK.md`](3DCRAFT-FEEDBACK.md) (§7); the developer takes it to 3DCraft in one go.
- **No Jigs, no assemblies.** No `.3dcraftjig` packages and no `assembly.*`, `instance.*`, `mate.*`,
  `joint.*`, `coupling.*` or motion commands: they get repositories of their own later. A document may hold
  several bodies, and it publishes 2 to 4 public parameters (§4.5).
- **Original designs.** Generic types (a cap screw, a moka pot, a solid-body guitar) are fine; a brand's
  specific design, logo or name is not. Text uses 3DCraft's bundled fonts; never commit font files.
- **Licence.** MIT for everything here. Data from elsewhere (an elevation model, a route) needs a licence
  that allows it and a row in [`ATTRIBUTION.md`](ATTRIBUTION.md).

## 2. Layout

```text
AGENTS.md README.md CATALOGUE.md 3DCRAFT-FEEDBACK.md ATTRIBUTION.md LICENSE
tools/examples.py       build, render, check, coverage, readme (python3, standard library only)
tools/pin.json          the pinned 3DCraft commit and file format
findings/<F-nnn>-<slug>/  minimal reproducers for 3DCRAFT-FEEDBACK.md
examples/NN-<id>/       one directory per example: NN its place in CATALOGUE.md, <id> kebab-case
log/ plan/              local only (gitignored): dev log, plans
```

| File in `examples/NN-<id>/` | What it is | Made by |
|---|---|---|
| `build.json` | **The source**: a JSON list of `[command, params]` steps run in a new document, ending with `document.check`. The same format as 3DCraft's own `docs/examples`, so the start screen can run it as is: no file paths, no `file.*` steps in it. | hand |
| `meta.json` | title, card summary, domain, tier, difficulty, standards, materials, preview framing, exports | hand; `stats` and `craft3d` written by the tool |
| `README.md`, `prompt.md` | the example's page and its AI rebuild chat (§6) | hand |
| `<id>.3dcraft` | the document built from `build.json`, opens directly | `tools/examples.py build` |
| `exports/` | only what the process needs: 3MF for printing, DXF or SVG for laser, plasma, CNC and flat patterns, STEP for machining; listed in `meta.json` `exports` (`file.export` params, plus `values` to export at other public parameter values) | `tools/examples.py build` |
| `preview.png` | the picture (§5) | `tools/examples.py render` |
| `make.py`, `data/` | only for the one example whose input comes from outside (§3) | hand |

## 3. Working with 3DCraft

- **Build headless.** Edit `build.json`, then `tools/examples.py build <id>`: it runs the script, refuses to
  save when `document.check` is not ok, writes the exports, measures, and lints names and budgets. To look
  around: `craft3d-cli run examples/NN-<id>/<id>.3dcraft --cmd document.inspect`. To learn a command:
  `craft3d-cli commands --filter <id>`. The user guide (`~/code/3dcraft/docs/guide/`) and the guide's
  examples (`~/code/3dcraft/docs/examples/*.json`) show the idioms; read them, never edit them.
- **Never use the session's 3DCraft MCP tools** (`mcp__craft3d__*`): they drive the developer's own window.
  Work through `craft3d-cli`; its commands are the same ones MCP runs.
- **Memory and time.** The developer's laptop has crashed on runaway processes. `tools/examples.py` caps every
  run; by hand, always `systemd-run --user --scope -q -p MemoryMax=3G -p MemorySwapMax=0 timeout 900
  craft3d-cli …`. Exit 137 means the cap was hit: that is a finding, never a reason to raise the cap. When several agents
  work at once, the coordinator sets a shared slice (`systemctl --user set-property --runtime examples.slice
  MemoryMax=10G MemorySwapMax=0`): then `export CRAFT3D_SLICE=examples.slice` (the tool adds it) and add
  `--slice=examples.slice` to every `systemd-run` you type. One
  render or `check-range` at a time. No cargo builds are needed here; never build 3DCraft from this repo. A
  3DCraft window you start gets `--recovery-dir none`.
- **Python.** Allowed for what does not belong in a CAD platform: fetching and converting outside data,
  searching. Python that computes geometry 3DCraft should compute is a workaround: first log the missing
  capability (§7), and use it only when the example cannot exist otherwise, saying so in its README. A
  `make.py` runs offline from committed inputs, is deterministic, and writes steps into `build.json`.
- **Lessons from the first example** (they cost time once; don't pay again):
  - Face names come from the sketch's entity ids (`F2:side(e13)`): a point added to a profile renumbers its
    lines. Read them from `document.inspect` (`faceNames`) after every change to a profile.
  - A measure's face subject is a query: `{"kind": "face", "where": {"name": "*F6:side(e7)"}}` (a glob:
    later features prefix the names, `F8:copy(0)/F7:copy(1)/F6:side(e7)`).
  - A feature's body cannot be measured once a later feature has taken it: measure the final body, and
    split it with planes (`volumeBelow`) or outputs (`variable.measure`) for closed-form checks.
  - Units in `tol` are expressions: `0.01 mm^3` means (0.01 mm)³; write the plain number `0.01` (the
    document's unit).
  - `body.appearance` replaces the whole appearance (F-005): give every field, or set them all in
    `material.preset`.
  - Coatings (black oxide, paint, powder coat, anodising) render best as what they are, a dielectric layer
    (`metallic` 0); a dark metallic body reflects dark and loses its form under ACES.
  - Every measure on a complex body runs at every regeneration (the screw: 1 s of its 4.6 s). Measure what
    proves something.
  - Run `tools/examples.py check` early: `check-range` finds per-size kernel refusals the defaults hide.
- **Lessons from the first reviews** (what reviewers found again and again):
  - Standard values written from memory are often wrong (an ISO 2936 key length, an ISO 4762 socket band):
    verify every value against a source and cite it.
  - Every number in the README is the model's (`output.list`, `assert.list`), and every claim is one the
    checks prove ("every length" when check-range tried 32 points is untrue).
  - Look at the full-size preview for renderer artefacts: smears (F-013, `look.reflections`), stepped
    shadow bands (F-026, F-043, `look.light`), blotches in cavities (F-046). Fix them with the framing keys
    of §5 and say so in the README.
  - Under the Workshop environment at rotation 0 the warm key light makes polished steel read as brass and
    black oxide as bronze (F-054): render the preview at `look.rotation` 0, 90, 180 and 270 and keep the
    one where neutral metals read neutral (often 180).
  - The body is named after its last feature (F-042): name that feature for the part ("Stand", "Bowl").
  - A prompt must give every size its Acceptance depends on (a spline's handles, a wall, a count).
  - Real use, not only the drawing: will it be gripped, driven, hung, will it tip, does it fit the tool
    that makes it (jaws, a quartz movement's torque, a slicer's walls)?
- **Prefer 3DCraft's own means**: variables and formulas, tables, `sketch.curve` (curves from formulas),
  `feature.pattern`, `sketch.pattern`, conditional features (`when`), named sets, datums.

## 4. The quality bar

### 4.1 Real
Sizes follow the named standard (number, part, table) or a stated real reference, cited in the README.
Proportions a professional of the trade would accept. Real units and tolerances where they matter.

### 4.2 Makeable
Name the process; prove with assertions what can be proven:
- **FDM printing:** walls ≥ 1.2 mm (`measure.thickness`); no overhang below 45° from the bed unless the
  README says where supports go (`measure.draft`, pull = the build direction); a first-layer chamfer;
  clearances for fits; 3MF export in the print orientation.
- **Sheet metal:** inner bend radius ≥ the material's minimum; `bendable`; holes ≥ 2.5 t + r from a bend;
  reliefs; flat pattern as DXF.
- **Laser, plasma, waterjet:** smallest slot and hole ≥ the thickness; kerf stated; cut and engrave apart.
- **CNC milling:** inside corners ≥ the tool radius; pockets ≤ 4 × the tool diameter deep.
- **Turning, casting, woodworking, packaging:** casting draft ≥ 1° (`measure.draft`) and fillets on every
  cast edge; boards of stock thickness, grain stated, joints in proportion; a board grade and style code
  for packaging.

### 4.3 Beautiful
- Fillets and chamfers wherever the real object has them (the developer asks this explicitly): no blocky,
  untouched edges.
- Materials from `material.preset`, tuned with `body.appearance` (colour, roughness). Keep to your
  example's line of the palette in `CATALOGUE.md`, so the 21 look different side by side.
- The preview frames the object well (§5). Look at it at full size, and from two more angles before you
  hand in.

### 4.4 Light
Loading means opening the `.3dcraft` and regenerating it; the tool measures it (`stats.load_s`,
`craft3d-cli info`, the least of two openings, since other agents' work only adds time). Budgets on the developer's laptop: **simple ≤ 1 s, difficult ≤ 2 s, complex ≤ 4 s**,
file ≤ 1 MB, and CPU time (all threads, `stats.load_cpu_s`) at most 3 × the load budget: the web build is
single-threaded, so the CPU time is roughly what it waits. For scale: the
guide's chassis opens in 9 s and its fuel tank in 55 s, both far too slow for this gallery. Over budget,
simplify (fewer, larger features; a pattern instead of copies; no needless booleans); only the coordinator
grants an exception (`meta.json` `budget_exception` with the reason).

### 4.5 Parametric, named, minimal
- Every size a maker might change is a variable; everything derived is a formula. No magic numbers in
  feature params (0, 1 and angles of symmetry aside).
- **Names.** Variables in descriptive `snake_case` with the unit in the expression (`wall_thickness` =
  `2 mm`, not `t`); features, sketches, datums, sets and assertions named for their intent in plain English
  (`Bolt holes`, `Seat round-over`). No automatic names (`Extrude2`): the tool rejects them (only the hidden
  tool of an extrude-with-cut keeps one: see F-002).
- **2 to 4 public parameters** (`variable.publish` with label, group, range and step): the knobs a maker
  would really turn. The tool proves the ranges with `craft3d-cli check-range`. No more: a configurator
  with many options is a Jig.
- **A minimal history.** Every step contributes to the final model: no dead, suppressed, trial or undone
  steps; one feature where one suffices. Guide: simple ≤ 50 steps, difficult ≤ 120, complex ≤ 250 (variables
  and assertions included). Order: variables, then per part its sketches and features, materials,
  assertions, `document.info` (title, description, author `3DCraft examples`, licence `MIT`),
  `document.check`.

### 4.6 Proven
End with assertions that make the example prove itself: at least one closed-form or independently computed
measure (volume, area, capacity, mass, a section property), the counts that matter (holes, treads, facets),
and the process checks of §4.2. All pass at the defaults and over the public ranges; `document.check` is
`ok` and any unproven assertion is explained in the README. Keep assertions cheap: they run at every
regeneration.

## 5. The preview

`tools/examples.py render <id>`: 1600 × 1200, studio look, **Workshop** environment, **ACES** tone curve,
**+0.5 stop**, plain background, CPU renderer, 8 frames accumulated: the developer's look, the same as
3DCraft's start-screen thumbnails. `meta.json` `preview` may set only the framing (`view`, `zoom`,
`camera`, `projection`, `box`, and `look.light`, `look.rotation`; `look.reflections: false` only where
the renderer's screen-space reflections smear a surface, F-013, said in the README). It takes about a minute.

## 6. README, meta.json and prompt

**`README.md`** of an example, in this order: title and a one-paragraph pitch; the preview; *What it shows*
(the 3DCraft techniques, command ids in backticks); *The real thing* (standards, process, material, how to
make it: print settings, cut and bend order, finish); *Parameters* (the public ones and their ranges);
*Checks* (the assertions in words); *Files*; *Rebuild*; *Difficulty* (the reviewer's score out of 10 and one
line why); *Platform notes* (links to `3DCRAFT-FEEDBACK.md` entries, if any). Every claim must be true of the
model.

**`meta.json`**:

```json
{
  "id": "socket-head-cap-screw",
  "title": "Socket head cap screw",
  "summary": "revolve, hex socket, size table",
  "description": "An ISO 4762 socket head cap screw, M3 to M12, in black-oxide steel.",
  "domain": "Machine building",
  "process": "Cold heading, thread rolling",
  "tier": "simple",
  "difficulty": {"score": null, "rationale": ""},
  "standards": ["ISO 4762:2004"],
  "materials": ["Steel, property class 12.9, black oxide"],
  "units": "mm",
  "preview": {"zoom": 1.1, "look": {"light": [200, 70]}},
  "exports": [{"path": "exports/socket-head-cap-screw.step"}],
  "prompt_test": {"date": null, "model": null, "result": null}
}
```

`summary` is the start-screen card's line (a few words, like "sheet metal, bends"). `stats` and `craft3d`
are written by the tool.

**`prompt.md`**: the chat a person could paste, turn by turn, into an AI connected to 3DCraft over MCP to
build the same model. Only the person's turns, in a designer's words (intent, sizes, standards, finish); no
command ids, no JSON; 3 to 8 turns, the last asking for a check and a picture. Below the turns,
*Acceptance*: the measures the result must meet (volume within 1 %, counts, the process checks). A prompt
counts as done once tested (§8): `meta.json` `prompt_test` records the date, model and result.

## 7. 3DCraft feedback

Collect, never fix. [`3DCRAFT-FEEDBACK.md`](3DCRAFT-FEEDBACK.md) has four kinds:
- **Bug**: a wrong result, a crash, a valid request refused. With a minimal reproducer in
  `findings/<F-nnn>-<slug>/repro.json` (a script for `craft3d-cli run --new '{"units":"mm"}' --script`).
- **Missing capability**: phrased generally, for any shape and anyone who designs with 3DCraft (3DCraft is a
  platform: never "a FEFCO box command", but "fold a sheet along crease lines with its thickness").
- **Performance**: too slow or too heavy, with numbers.
- **Agent friction**: what made building through commands slow or error-prone (unclear errors, missing
  params, naming).

Each entry: id (`F-001` …), kind, title, the example it was found in, the 3DCraft commit, what happens and
what should happen, the reproducer, the impact on the example (blocked, workaround used, cosmetic) and the
workaround. An example that works around something links its entry from its README, so it can be improved
once 3DCraft is fixed. Builders propose entries in their report and write the reproducer; the coordinator
numbers them and edits `3DCRAFT-FEEDBACK.md`.

## 8. Roles and the review loop

| Role | Model, effort | Does |
|---|---|---|
| **Coordinator** (main session) | Opus 5.5, xhigh | Owns this file, `CATALOGUE.md`, `README.md`, `3DCRAFT-FEEDBACK.md`; briefs agents; runs the review loop; commits (the only one who does); reports to the developer in Dutch. |
| **Feasibility probe** | Opus 5.5, medium | Answers "can 3DCraft do X at the pin" with a minimal script, before a risky example is built. |
| **Builder** | Opus 5.5; high (simple), xhigh (difficult, complex) | Owns `examples/<id>/` only. Writes `build.json`, `meta.json`, `README.md`, `prompt.md`; builds, renders, checks itself against §4 and looks at the pictures before handing in; writes reproducers in `findings/`. Never commits. |
| **Reviewer** | Opus 5.5; high, xhigh for complex | Fresh, and reads the files, not the builder's report. Plays the trade's professional (toolmaker, sheet-metal shop, print farm, cabinetmaker, luthier, naval architect, jeweller, industrial designer). Rebuilds, renders two more views, checks §4 point by point, gives the difficulty score. |
| **Prompt tester** | Sonnet 5.5, medium (once Opus 5.5 if Sonnet fails, to tell a weak prompt from a weak model) | Fresh, gets only `prompt.md` and a 3DCraft MCP session; builds; the coordinator compares the result with the *Acceptance*. |

**Review verdict**: `PASS` or `REVISE`, with findings marked **MUST** (wrong, unmakeable, ugly, over budget,
untrue README), **SHOULD** or **NIT**, each with its evidence (a measure, a picture, a clause of a
standard), and the difficulty score with one line why. Builder and reviewer loop until no MUST is open;
the same reviewer is continued for the re-review.

**Difficulty** (1 to 10, scored by the reviewer): what it takes to build this from scratch in 3DCraft, by
hand or with an agent.

| Score | Typical content |
|---|---|
| 1–2 | one or two solid features from simple sketches |
| 3–4 | several features, a constrained sketch, patterns, fillets and chamfers, a table or formulas |
| 5–6 | datums and angled work, booleans between several bodies, sheet metal with several bends, folds, conditional features, careful edge naming |
| 7–8 | freeform: lofts, sweeps along 3D paths, developables, surfaces; many coupled formulas; process checks across bodies; kernel limits to navigate |
| 9–10 | class-A surfacing (G2), data-driven geometry, large coupled multi-body designs, expert domain knowledge |

Tiers roughly: simple 1–3, difficult 4–6, complex 7–10. The folders are numbered in CATALOGUE.md's order
(simple → complex); if the scores end up far from that order, the coordinator renumbers once at the end. The
id (and the file names) never carry the number, so the start screen's ids stay stable.

**Done, for one example:** `tools/examples.py check <id>` passes · the preview is rendered at the pin and
looked at · README, meta.json and prompt.md are complete and true · reviewer PASS, score in `meta.json` ·
prompt tested · feedback entries filed · committed by the coordinator and `tools/examples.py readme` run.

## 9. Before a session ends

Append to `log/devlog.md` (local): what landed, the numbers (load time, steps, score), what is open. Keep
`tools/examples.py check` green for every committed example: a session can end abruptly, and the dev log
plus a clean tree is how the next one picks up.
