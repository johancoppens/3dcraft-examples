# Feedback for 3DCraft

What building these examples showed 3DCraft gets wrong or lacks, collected for the developer to take to
3DCraft in one go (3DCraft is frozen for R1; nothing is fixed from here). Kinds: **Bug** (wrong result, crash,
a valid request refused; with a reproducer in `findings/`), **Missing capability** (phrased for any shape
and anyone), **Performance** (with numbers), **Agent friction** (what made building through commands slow or
error-prone). See `AGENTS.md` §7.

All entries are against 3DCraft `f4b0813c` unless they say otherwise.

| Id | Kind | Title | Found in | Impact |
|---|---|---|---|---|
| [F-001](#f-001) | Performance | The guide's fuel tank takes 55 s to open, the chassis 9 s | calibrating the load budget | start screen |
| [F-002](#f-002) | Agent friction | An extrude with `cut`, `join` or `intersect` cannot name its extrusion | calibrating the name check | history names |
| [F-003](#f-003) | Agent friction | `craft3d-cli --version` does not print the commit | setting up the pin | tooling |
| [F-004](#f-004) | Performance | A modelled thread takes 3.5 s to regenerate, measures on it 1 s more | socket-head-cap-screw | load budget exceeded (4.8 s, 9 s on one core) |
| [F-005](#f-005) | Agent friction | `body.appearance` replaces the whole appearance; fields left out are dropped | socket-head-cap-screw | finish lost silently |
| [F-006](#f-006) | Bug | A modelled thread on a tip chamfered 0.75 P deep is refused for M3 to M6 | socket-head-cap-screw | workaround used |
| [F-007](#f-007) | Missing capability | Loft sections cannot lie on a cylinder | probe for ship-propeller | planar approximation |
| [F-008](#f-008) | Bug | Fillets at propeller blade roots fail above 1 mm, and at 1 mm on blunt sections | probe for ship-propeller | root fillet ≤ 1 mm |
| [F-009](#f-009) | Bug (suspected) | Shelling a lofted hull with a small bow section: "what fits is below 0.0571 mm" | probe for rc-yacht-hull | larger bow section |
| [F-010](#f-010) | Performance | Curves from formulas fit about 400 control points at the default tolerance: 40 s for six sections | probe for ship-propeller | tolerance 0.001 mm |
| [F-011](#f-011) | Missing capability | A spline's inner through-points must be plain numbers, not expressions | probe for ventoux-relief | data written as numbers |
| [F-012](#f-012) | Missing capability | No surface through a grid of points | probe for ventoux-relief | loft of row splines |
| [F-013](#f-013) | Bug | Screen-space reflections smear a patch onto a threaded shank in the CPU renderer | socket-head-cap-screw | reflections off in the preview |
| [F-014](#f-014) | Missing capability | A thread has no fit allowance, so a mating pair touches and cannot be shown clear | probe for moka-pot | one thread cosmetic |
| [F-015](#f-015) | Missing capability | A folded panel cannot have a slit, and thick panels do not fold to 180° | probe for mailer-box | single walls, no locks |
| [F-016](#f-016) | Agent friction | A number parameter cannot take a series of values (a step counts from 0 when `min` is a formula) | socket-head-cap-screw | a choice from a table, rows limited by `min`/`max` |
| [F-017](#f-017) | Missing capability (minor) | No precious-metal presets; a preset recoloured keeps its base metal's density | probe for solitaire-ring | `body.material` |
| [F-018](#f-018) | Agent friction | `document.inspect` on a freshly opened file reports assertions as pending; `info` and `assert.list` wait | socket-head-cap-screw | none |
| [F-019](#f-019) | Missing capability | Measures and assertions are recomputed at every regeneration; no way to compute them on demand | socket-head-cap-screw | none |

## F-001

**Performance.** `docs/examples/tank.json`, built and saved, takes **54.3 s** to open
(`craft3d-cli info tank.3dcraft`, release build on the developer's laptop, 850 MB peak); without its
assertions still 54.9 s, so the geometry itself costs it, not the checks. The chassis takes 9.0 s, the
bracket 0.04 s. Both the tank and the chassis are on the start screen, where a click builds them.
**Should:** an example on the start screen opens in a few seconds; or the start screen opens a saved
document whose bodies need not be rebuilt in full. Reproduce: `craft3d-cli run --new '{"units":"mm"}'
--script docs/examples/tank.json --out tank.3dcraft && time craft3d-cli info tank.3dcraft`.

## F-002

**Agent friction.** `feature.extrude` with `cut`, `join` or `intersect` adds two features, the extrusion and
the boolean; `name` names the boolean, and the extrusion keeps an automatic name (`Extrude1`). The history
then shows names that say nothing; renaming each costs an extra `feature.rename` step. Seen in
`docs/examples/bracket.json` (`Extrude1`, `Extrude2`). **Should:** a param to name the extrusion too (for
example `toolName`), or derive its name from the boolean's (`Drilled (tool)`).

## F-003

**Agent friction.** `craft3d-cli --version` prints `craft3d-cli 0.1.0`; the commit is built into the binary
(for bug reports) but not printed, so a script cannot check which build it runs without searching the
binary's bytes (what `tools/examples.py` does). **Should:** `--version` prints the commit and the file format
version, e.g. `craft3d-cli 0.1.0 (f4b0813c, format 69)`.

## F-004

**Performance.** `feature.thread` with `modeled: true` on an M8 × 30 shank (26 mm of thread, 21 turns,
146 faces) takes about 3.5 s to regenerate; the same screw with a cosmetic thread opens in 0.04 s. Measures
on the threaded body add about 1 s at every regeneration (volume and mass 0.45 s, `volumeBelow` 0.55 s).
The cosmetic thread draws nothing on the shank, so a screw meant to look real needs the modelled one.
**Should:** a modelled thread of this size regenerates well under a second (its turns are congruent: one
turn's faces, repeated); measures on it reuse what the faces already know. Reproduce:
`tools/examples.py build socket-head-cap-screw` and time `craft3d-cli info` on the result.
Over the screw's range it opens in 1.4 s (M3 × 6) to 7 to 8 s for the longest screws threaded to the head (M8 × 35: 26 turns, 8.2 s and 560 MB with other work running; M3 × 20: 7.2 s, 710 MB), and M8 × 30 takes 9.0 s on one core (`taskset -c 0`), which is what the single-threaded web build gets.
**Workaround in the example:** none; the example carries a budget exception.

## F-005

**Agent friction.** `body.appearance` replaces the body's whole appearance: `{"body": "Screw", "color":
"#4b5058"}` after `material.preset` drops the preset's `metallic` and `roughness` (the result reads back as
`{"color": "#4b5058"}`), so a tweak of one field silently turns brushed steel into a matte dielectric.
**Should:** fields not given are kept (as `material.preset` overrides do), or the summary says plainly
that the call replaces everything.

## F-006

**Bug.** A modelled ISO thread on a shank whose tip is chamfered 0.75 P deep (`sketch.polyline` half
section, `feature.revolve`, `feature.thread` with `modeled: true`) is refused for M3, M4, M5 and M6: "the
groove of the thread cannot be cut: boolean does not support this: two points closer together than the
tolerance can tell apart (at the edge of tolerance)"; with the full screw M6 fails as "imprint lost". M8
works. A chamfer to just below the minor diameter (0.663 P, ISO 4753) works for every size. A chamfered tip
is how threaded ends are made, so any depth should work. The prompt test of the screw (a different model, built from scratch) hit
the same refusal at M3 with a chamfer 0.1 mm under the minor diameter, and got past it at 0.15 P. Reproducer:
[`findings/F-006-thread-on-chamfered-tip/repro.json`](findings/F-006-thread-on-chamfered-tip/repro.json)
(M4; set `thread_d` and `pitch` for the others). **Workaround in the example:** the ISO 4753 chamfer depth,
which is also the standard's.

## F-007

**Missing capability.** A propeller blade's sections lie on cylinders round the shaft (each is a flat
airfoil wrapped onto its radius). `feature.loft` takes sketches, and sketches are flat, so the sections can
only be planes tangent to their cylinders: an approximation that grows with the blade's width.
`feature.extrude` can already lay profiles onto a cylinder by its development (`wrap`) for raised text; the
same for a sketch or a loft section would cover propellers, impellers, fan blades, wrapped labels and
cam grooves. **Should:** a sketch (or a curve) wrapped onto a cylinder or cone by its development, usable
as a loft section or a sweep path.

## F-008

**Bug.** On a four-blade propeller (six lofted sections, `feature.pattern` × 4, joined to a cylindrical
hub), `feature.fillet` on the blade roots works at 1 mm on thin elliptic sections, fails at 1.5, 2 and 8 mm
("the rolling ball along this edge could not be followed: the radius does not fit between the faces
somewhere along it, or a face turns too sharply under it"), and on blunter roots (t/c 0.25 to 0.40) fails
even at 1 mm: "the fillet face along this edge could not be approximated within the tolerance". A real
blade has a root fillet of several millimetres. Reproducer (53 steps, regenerates in about 40 s):
[`findings/F-008-fillet-at-blade-roots/repro.json`](findings/F-008-fillet-at-blade-roots/repro.json).

## F-009

**Bug (suspected).** A hull lofted through eight station splines, with a small bow section (8 × 6 mm), is
refused by `feature.shell` 1.5 mm: "the offset of the freeform face would fold over … what fits is below
0.0571289 mm". A 30 × 20 mm bow section shells fine. The bound looks far smaller than the section's
curvature allows. Reproducer (44 steps):
[`findings/F-009-shell-of-lofted-hull/repro.json`](findings/F-009-shell-of-lofted-hull/repro.json).

## F-010

**Performance.** A closed `sketch.curve` from formulas is fitted within the document's tolerance; at the
default 1e-6 mm each airfoil section of a 600 mm propeller became a spline of about 400 control points, and
six sections lofted, patterned and joined regenerate in 40 s using 1.5 GB. At 0.001 mm it is 100 to 150
points, 11.6 s and 0.56 GB. **Should:** a curve fitted to what it needs (curvature-adaptive, or a separate
fitting tolerance), so a formula section does not cost hundreds of points at the topological tolerance.

## F-011

**Missing capability.** `sketch.spline` through points: the points between the ends must be plain numbers
("a point the spline passes through between its ends is fitted, not held: give it as numbers"). A terrain
or a lines plan from a table cannot then follow a variable (a vertical exaggeration, a scale): the numbers
are baked in by whoever writes the script. **Should:** through-points as expressions, evaluated at
regeneration, like the ends.

## F-012

**Missing capability (minor).** There is no command that makes a surface through a grid of points (or from
a B-spline surface's control points). A loft through one spline per row works well (a 60 × 40 grid opens in
1.1 s), so this is about convenience and fidelity across the rows, not a blocker.

## F-013

**Bug (rendering).** The CPU renderer's studio look draws a smeared, mirrored patch on the thread of the
socket head cap screw next to its head, at 1000 × 750 and 1600 × 1200 (not visible at 480 × 360). With
`look.reflections: false` the patch is gone and the rest of the picture is unchanged; `specularShadow` has
no effect on it. Reproduce: build `examples/socket-head-cap-screw`, then `view.render` with `"camera":
{"eye": [48, -52, 30], "target": [-11, 0, -1], "up": [0, 0, 1], "fovY": 27}`, the gallery look
(`studio`, `workshop`, `aces`, exposure 0.5, `rotation` 90, `accumulate` 4), 1000 × 750; compare
`reflections` true and false around the thread's last turns. **Workaround in the example:** the preview is
rendered with `reflections: false`.

## F-014

**Missing capability.** `feature.thread` cuts the basic profile, with no allowance or tolerance class (6g on
the bolt, 6H in the nut). A modelled external and internal thread of the same size, phased half a pitch
apart, then touch along their flanks; `document.interference` and `measure.clearance` answer "unknown":
"boolean does not support this: more than two faces meet along an edge and two of them are tangent there
(tangent contact along an edge)". Turned under size, they overlap instead (3.8 mm³). A screwed joint can
therefore never be shown clear. Reproducer:
[`findings/F-014-mating-threads-touch/repro.json`](findings/F-014-mating-threads-touch/repro.json).
**Should:** a tolerance class or an allowance per thread (ISO 965-1), so mating threads have their real
clearance; and interference that decides tangent flank contact.

## F-015

**Missing capability.** `feature.fold` with thick panels: a panel cannot carry a slit (the locking tabs of a
FEFCO 0427 mailer go through slits), and panels are not built when folded to 180° (its rolled double side
walls). One fold amount cannot drive every crease of a box either, because the dust flaps pass through the
walls at angles between flat and closed; this one is physics, not a bug, and the box folds in stages.
**Should:** slits (cuts inside a panel) and 180° folds of thick panels.

## F-016

**Agent friction.** A number parameter cannot take the values of a series (ISO 4762's lengths: …, 10, 12,
16, 20, 25, …): `step` counts from 0 when `min` is a formula. A choice from a table of the series, its range
limited by `min` and `max` rows read from another table, works well and is what the screw does; a number
parameter with `values` from a table column would read better in the form.

## F-017

**Missing capability (minor).** The material presets have no gold, silver, brass, bronze or copper, and a
preset recoloured keeps its base metal's density (gold made from `steel` weighs 7850 kg/m³), so the mass is
wrong unless `body.material` is set as well.

## F-018

**Agent friction.** `craft3d-cli run FILE.3dcraft --cmd document.inspect` on a freshly opened file reports
some assertions with `"status": "pending"` (measured in the background) and returns, while `craft3d-cli info
FILE` and `--cmd assert.list` wait and report them passed. A one-shot check through `document.inspect` then
reads an incomplete state, and a time taken around it is not the full load. **Should:** a one-shot
`run` waits for pending measures before it prints, or `document.inspect` takes `"wait": true` as `param.set`
does.

## F-019

**Missing capability (performance).** Assertions and outputs are measured after every regeneration. On the
screw they cost 1.2 s of its 4.8 s load (A/B on the same build: 3.6 s without its 4 assertions and 3
outputs, 4.8 s with them); the measures are volume, mass and a volume below a plane on a threaded body of
146 faces. Someone who opens an example to look at it does not need them; a check, an export, a range check
or the checks panel does. **Should:** measures on demand: computed when something asks for them (the
checks panel open, `document.check`, `assert.list`, an export, `check-range`) and cached per body revision,
so a regeneration that leaves a body unchanged does not measure it again. Today `when` on each assertion
could switch them off by a variable, but then the document no longer proves itself when opened.
