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
| [F-020](#f-020) | Bug | `measure.thickness` finds a wall but proves far less (0.235 of 1.7 mm; 0 of 7 mm on a bowl), slowly | t-slot-profile, turned-bowl | wall check not asserted |
| [F-021](#f-021) | Agent friction | `variable.set` takes `332 mm^2` as (332 mm)² silently; `assert.add` refuses it | t-slot-profile | none |
| [F-022](#f-022) | Agent friction | Assertion bounds cannot be written in an output's unit (`0.8 kg/m`) | t-slot-profile | output not asserted |
| [F-023](#f-023) | Missing capability | No sketch corner round (fillet) that follows the variables | t-slot-profile | sharp cavity corners |
| [F-024](#f-024) | Bug | `volumeBelow` at a plane that holds pocket floors is refused | wall-clock | plane moved |
| [F-025](#f-025) | Missing capability | `face.appearance` takes only literal face names, not a query or a named set | wall-clock | stencil intersect |
| [F-026](#f-026) | Bug | Contact shadows of a thin part a few mm above a face draw hard, stepped bands | wall-clock | cosmetic |
| [F-027](#f-027) | Missing capability | A pattern cannot repeat a text with a value that changes per instance | wall-clock | 24 numeral steps |
| [F-028](#f-028) | Performance | `feature.shell` of a revolved spline profile takes 3.6 to 4.7 s (the revolve 0.04 s) | turned-bowl | wall as an offset curve |
| [F-029](#f-029) | Missing capability | `feature.offsetProfile` refuses splines | turned-bowl | offset written as a formula curve |
| [F-030](#f-030) | Bug (proof weakness) | `measure.distance` across a parallel wall finds 7.000 mm but proves only 6.23 mm | turned-bowl | wall proven by Steiner's formula |
| [F-031](#f-031) | Bug | `view.render` with `section` and the studio look draws flat grey | t-slot-profile (review) | no section pictures |
| [F-032](#f-032) | Bug (minor) | `feature.thread` reports the M8 tap drill as 6.75 mm; ISO 2306 gives 6.8 mm | t-slot-profile (review) | none |
| [F-033](#f-033) | Bug | Chamfering or rounding all edges of a pocket's mouth (or a step's riser) is refused | hex-key-stand | sharp socket mouths |
| [F-034](#f-034) | Performance | Booleans with text are slow: about 24 ms per glyph joined, 1 s to intersect text with a stepped block | hex-key-stand | labels a separate body |
| [F-035](#f-035) | Agent friction | A text cannot show a table's text column (`{hex_keys[1].size}`) | hex-key-stand | numbers formatted instead |
| [F-036](#f-036) | Missing capability | An extrusion cannot end on the face under each of its profiles | hex-key-stand | one sketch per label height |
| [F-037](#f-037) | Performance | A document with text embeds the whole font file (332 KB), even the bundled one | wall-clock, hex-key-stand | files of 460 KB |
| [F-038](#f-038) | Missing capability (minor) | No serif font among the bundled ones | wall-clock (review) | mixed serifs in Roman numerals |
| [F-039](#f-039) | Agent friction | `sketch.pattern` cannot skip its seed (instance 0) | wall-clock (review) | seed drawn off-axis |
| [F-040](#f-040) | Missing capability | The wood pattern has evenly spaced rings with one wobble; no ring-width variation or latewood contrast | turned-bowl (review) | pattern tuned per example |
| [F-041](#f-041) | Missing capability (minor) | A pattern's `origin` and `axis` are numbers, not expressions | turned-bowl (review) | pith fixed for the default size |
| [F-042](#f-042) | Agent friction | A body cannot be named apart from its last feature | t-slot-profile, turned-bowl (reviews) | last feature named for the part |
| [F-043](#f-043) | Bug | The studio key light's shadow draws stair-stepped, aliased bands on broad flat faces | hex-key-stand (review) | another light direction |
| [F-044](#f-044) | Agent friction | The 3MF's material names are appearance strings, not the `body.material` name | hex-key-stand (review) | none |
| [F-045](#f-045) | Missing capability | No 3MF export of several bodies as parts of one object (multi-colour prints) | hex-key-stand (review) | two build items |
| [F-046](#f-046) | Bug | The CPU studio look's ambient occlusion draws blotchy patches in narrow cavities | t-slot-profile (review) | faint, left as it is |
| [F-047](#f-047) | Missing capability | No measure of what an open vessel holds up to its rim | turned-bowl | capacity in closed form |
| [F-048](#f-048) | Bug | A face colour set on a feature is lost when a later feature is switched off (`when`) | wall-clock (prompt test) | colour on a final feature |
| [F-049](#f-049) | Missing capability (minor) | No distance measure projected onto a plane (clearance seen from the front) | wall-clock (prompt test) | hidden helper body |
| [F-050](#f-050) | Bug (proof weakness) | `flatExtent` is not proven when the flat pattern holds a spline, even a hole inside it | steel-bookend | blank length proven through the area |
| [F-051](#f-051) | Agent friction (minor) | A flat pattern's DXF splits each straight edge into collinear lines at the bend zone | steel-bookend (review) | none |
| [F-052](#f-052) | Missing capability | `feature.pattern` copies a hole but not its cosmetic thread; `feature.thread` takes one face | v-block-pair | 8 thread features |
| [F-053](#f-053) | Missing capability | Projected views (SVG, DXF) have no dimensions, centre lines, title block or ISO 128 line weights | v-block-pair | views without dimensions |

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
no effect on it. Reproduce: build `examples/01-socket-head-cap-screw`, then `view.render` with `"camera":
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

## F-020

**Bug (proof weakness).** On an extruded T-slot profile, `measure.thickness` finds the thinnest wall
(1.70 mm) but proves only `atLeast` 0.235 mm, and 0 mm once a bore in it is countersunk; an assertion of
the wall therefore stays not proven. Simple tubes and plates prove fine. Reproducer (35 steps, the profile
without its corner chambers):
[`findings/F-020-thickness-proof-on-profile/repro.json`](findings/F-020-thickness-proof-on-profile/repro.json). On the turned bowl's revolved spline wall
it finds 7.000 mm but proves `atLeast` 0, and takes 5.6 s (50 s on a shelled bowl): reproducer
[`findings/F-020-thickness-proof-on-profile/spline-wall-repro.json`](findings/F-020-thickness-proof-on-profile/spline-wall-repro.json).

## F-021

**Agent friction.** `variable.set {"expr": "332 mm^2"}` silently takes the text as (332 mm)² = 110224 mm²,
while `assert.add` refuses the same text and explains it ("means (332 mm)^2 in expressions; write
`332 * (1 mm)^2`"). **Should:** `variable.set` refuses or warns the same way. Reproducer:
[`findings/F-021-area-literal-in-variable/repro.json`](findings/F-021-area-literal-in-variable/repro.json).

## F-022

**Agent friction.** An output measured in kg/m (`variable.measure` with `"unit": "kg/m"`) cannot be bounded
in that unit: `min: "0.8 kg/m"` fails, `0.8 kg / (1 m)` works, and the result is shown as `mm^-1*kg`.
Reproducer: [`findings/F-022-output-unit-in-assertion/repro.json`](findings/F-022-output-unit-in-assertion/repro.json).

## F-023

**Missing capability.** A sketch has no corner round (fillet) between two of its lines that follows the
variables: every rounded corner of a profile needs its tangent points worked out by hand in `sketch.path`.
The T-slot profile leaves its cavity corners sharp because of it. **Should:** a sketch fillet (a radius at a
vertex, driven by an expression), as every sketcher has.

## F-024

**Bug.** `measure.below` / `volumeBelow` at a plane that holds the floors of engraved pockets is refused ("a
face in the plane whose loops enclose no area"); a plane 0.6 mm lower works. Reproducer:
[`findings/F-024-volume-below-at-pocket-floor/repro.json`](findings/F-024-volume-below-at-pocket-floor/repro.json).
**Workaround in the example:** the plane halfway up the dial's round-over.

## F-025

**Missing capability.** The faces a cut makes take the target body's appearance, and `face.appearance` takes
only literal face names (not a query or a named set), so an engraving of hundreds of faces (652 on the
clock's dial) cannot be coloured as engraved; a feature whose body a later feature consumed is refused
("has no body"). Reproducer:
[`findings/F-025-colour-of-cut-faces/repro.json`](findings/F-025-colour-of-cut-faces/repro.json).
**Should:** `face.appearance` with a query or a named set, and a way to give a cut's faces a colour of
their own (a laser's charred engraving, a painted pocket). **Workaround in the example:** a dark stencil
body is cut by the engravings and the dial intersected with it, so the pocket faces keep the dark colour.

## F-026

**Bug (rendering).** With `contactShadows` on, a thin part a few millimetres above a face (the clock's
hands over the dial) casts its contact shadow as hard, stepped bands; with `contactShadows: false` it is
soft. Reproducer (renders both):
[`findings/F-026-contact-shadow-steps/repro.json`](findings/F-026-contact-shadow-steps/repro.json). Raising the key light to about 80° (`look.light`)
hides the bands in a preview; that is a workaround, not a fix.

## F-027

**Missing capability.** A pattern cannot repeat a text whose value changes per instance (the numerals of a
dial, a ruler's graduations, numbered parts), so each numeral is its own text and its own feature: 24 steps
of the clock's 141. **Should:** a text whose content is an expression of the pattern's instance index, or a
text pattern.

## F-028

**Performance.** `feature.shell` of a revolved spline profile with its top open takes 3.6 to 4.7 s, against
0.04 s for the revolve alone; joining a foot ring to the shelled result adds 1.6 s. Reproducer:
[`findings/F-028-shell-of-revolved-spline/repro.json`](findings/F-028-shell-of-revolved-spline/repro.json).
**Workaround in the example:** the bowl's inside is the offset of its outside, written as a curve from
formulas, and the whole section is revolved once.

## F-029

**Missing capability.** `feature.offsetProfile` refuses a profile with splines ("not supported yet"), so the
even wall of a turned or drawn profile must be written out as a formula curve (the Bézier minus the wall
times its unit normal). **Should:** the offset of splines (an exact offset is not a spline, a fitted one
within the tolerance is what every modeller gives). Reproducer:
[`findings/F-029-offset-of-spline/repro.json`](findings/F-029-offset-of-spline/repro.json).

## F-030

**Bug (proof weakness).** `measure.distance` between the inner and outer faces of a parallel (offset) wall
finds 7.000 mm but proves only 6.23 to 6.78 mm, so a wall asserted to the micrometre stays not proven.
Reproducer: [`findings/F-030-distance-proof-loose/repro.json`](findings/F-030-distance-proof-loose/repro.json).
The bound also weakens with the size of the body: on the T-slot profile the same exact 2.6 mm gap is proven
"at least 2.6 mm" at a length of 300 mm and only "at least 2.25 mm" at 3000 mm.

## F-031

**Bug (rendering).** `view.render` with `section` and the studio look (CPU renderer) draws the bodies flat
grey, without their materials or the studio's shading, while the result still reports `look.mode: studio`.
Reproduce: the T-slot profile, the gallery look, the same camera with and without `"section": {"plane":
"zx", "cap": true}`.

## F-032

**Bug (minor).** `feature.thread` reports the tap drill of M8 as 6.75 mm (d − P); ISO 2306 (and every tap
drill table) gives 6.8 mm for M8, as for most sizes it rounds d − P up to a drill that exists.

## F-033

**Bug.** `feature.chamfer` or `feature.fillet` on the four mouth edges of a square pocket is refused at the
first edge ("does not end cleanly … neither all convex or all concave"); the short vertical edges where one
step of a block rises from the next are refused for the same reason. A lead-in chamfer on a socket or a
pocket is what every printed or machined part has. On the hex key stand a fillet of only the vertical riser
edges builds, but the step rims' fillet is then refused where it meets it, with and without `chain`. On the V-block pair,
chamfering every edge of an extrusion's end face is refused at the first edge that reaches a sharp inside
corner, and the advice the error gives (chamfer the continuing edges) is wrong: they are already in the
chamfer. Reproducer: [`findings/F-033-pocket-mouth-edges/end-face-chamfer-repro.json`](findings/F-033-pocket-mouth-edges/end-face-chamfer-repro.json).
The example rounds those inside corners 0.5 mm (good practice on a hardened part), which lets the chamfer
build. Reproducer:
[`findings/F-033-pocket-mouth-edges/repro.json`](findings/F-033-pocket-mouth-edges/repro.json).

## F-034

**Performance.** Booleans with text are slow: joining 14 extruded glyphs to a block costs about 0.33 s
(about 24 ms a glyph: the stand opens in 0.42 s against 0.09 s without the join), and intersecting text
prisms with a stepped block about 1 s. Reproducer:
[`findings/F-034-text-boolean-cost/repro.json`](findings/F-034-text-boolean-cost/repro.json).
**Workaround in the example:** the labels are a separate body (which a two-colour print wants anyway).

## F-035

**Agent friction.** `sketch.text` with `{hex_keys[1].size}` is refused ("holds a text there, not a number"):
a text cannot show a table's text column, only numbers. Reproducer:
[`findings/F-035-text-from-table-text/repro.json`](findings/F-035-text-from-table-text/repro.json).

## F-036

**Missing capability.** An extrusion of several profiles cannot end on the face under each profile (an
`upTo` per profile, or "up to the next face"), so labels embossed on steps of nine heights need nine
sketches and nine extrusions (27 of the hex key stand's 75 steps).

## F-037

**Performance (file size).** A `.3dcraft` with a `sketch.text` stores the whole font file as a blob
(`blobs/bfb44de2….font`, 331 784 bytes), also when it is 3DCraft's own bundled Noto Sans: the wall clock is
457 KB, of which 332 KB is the font for 12 numerals; the hex key stand 472 KB for nine labels. On the start
screen and the web, every example with a word in it carries the font again. **Should:** a bundled font is
referred to by its hash and not stored, and a font from elsewhere is stored as a subset of the glyphs used
(its licence permitting).

## F-038

**Missing capability (minor).** The bundled fonts are a sans (Noto Sans, whose capital I has slab serifs
while V and X have none), a mono and a single-stroke font; classic dial and engraving lettering, Roman
numerals above all, wants a serif face. Since 3DCraft stays light, one small serif face (or reading a font
file the user gives) would cover it.

## F-039

**Agent friction.** `sketch.pattern` can skip instances (`skip`) but not its seed, instance 0: a pattern
that leaves gaps round a dial (60 minute ticks without the 12 hour positions) needs its seed drawn off-axis
with trigonometric expressions, or two patterns.

## F-040

**Missing capability.** The procedural `wood` pattern draws its rings evenly spaced, with a single-scale
wobble, and has no control for varying ring width or for the sharpness and contrast of the latewood line,
so a turned bowl reads as zebrawood or a fingerprint rather than walnut unless its pith, axis and scale are
tuned by hand per example. **Should:** ring-width variation (a second noise on the radius) and a latewood
sharpness, so the presets read as their woods out of the box.

## F-041

**Missing capability (minor).** A pattern's `origin` and `axis` are plain numbers, so the pith cannot follow
a parameter (a bowl's height or diameter): set for the default size, it drifts off at the ends of the range.
**Should:** expressions, as body colours already take.

## F-042

**Agent friction.** A body has no name of its own: it shows as its last feature's name ("Countersunk thread
entries", "Foot coves") in outputs, assertions and the window, so the last feature must be named for the
part, or the part reads oddly. **Should:** a body name (`body.rename`, or `name` on `material.preset`).

## F-043

**Bug (rendering).** In the studio look the key light's shadow draws stair-stepped, aliased light and dark
bands across broad flat faces (the treads of the hex key stand at 1600 × 1200). `reflections: false` leaves
the picture pixel-identical; `shadows: false` or another `look.light` ([200, 70], [300, 60]) removes the
bands. **Workaround in the example:** the preview's light direction.

## F-044

**Agent friction.** In a 3MF export the `basematerials` names are appearance strings ("#e8641e metallic 0
roughness 0.7 subsurface 0.1") rather than the `body.material` name ("PLA"), and that string is what slicers
show as the filament.

## F-045

**Missing capability.** `file.export` to 3MF writes every body as its own build item; there is no option to
write several bodies as parts (components) of one object, which multi-colour and multi-material slicing
wants (the hex key stand's labels and stand).

## F-046

**Bug (rendering).** The CPU renderer's studio look draws blotchy light and dark patches of ambient occlusion
on the inner faces of narrow cavities (the T-slot profile's slots and bore near its end face), at
`accumulate` 4 and still at 16; `"ao": false` removes them, `reflections`, contact shadows and the specular
shadow do not. On this material `reflections: false` gives a byte-identical picture.

## F-047

**Missing capability.** `cavity` measures what closed shells inside a body enclose; there is no measure of
what an open vessel (a bowl, a cup, a hopper) holds up to its rim or up to a level. The turned bowl writes
its capacity as the closed-form volume of its Bézier profile revolved; the prompt test of it built a hidden
helper body. **Should:** a capacity measure for an open body: the volume between its inner faces and the
plane of its rim (or a given level), as `volumeBelow` does for a closed one.

## F-048

**Bug.** A face colour (`face.appearance`) given on the faces of a feature is lost, and the body's colour
drawn instead, when a feature after it is inactive (`when` false): the clock's engravings turned light again
when the other numeral style's cut was switched off. The prompt test of the clock worked round it by adding a
final always-active feature (a zero transform) and colouring the faces there, once per numeral style.

## F-049

**Missing capability (minor).** There is no distance measured in projection onto a plane (how far a hand is
from the numerals seen from the front, a part's clearance in plan): only the 3D distance. The clock asserts
a 3D bound that implies the projected one; its prompt test built a hidden copy of the hand moved onto the
engraving's floor.

## F-050

**Bug (proof weakness).** On a sheet-metal part whose flat pattern holds a spline (a hole inside the
pattern, or a spline in a `cutouts` sketch), `flatExtent` reports "found 303.29 mm, at least 0 mm" (not
proven) on both axes; with a circle hole or arcs in the outline it is exact, and `sheetMetal.bends` gives the
exact `flatSize`. A hole cannot change the outline's extent, and a spline's control hull bounds it anyway.
Reproducer: [`findings/F-050-flat-extent-with-spline/repro.json`](findings/F-050-flat-extent-with-spline/repro.json).

## F-051

**Agent friction (minor).** The flat pattern written to DXF (`file.export` with `sheetMetal`) splits each
straight side into three collinear LINEs, where the bend zone starts and ends (on the bookend's x = 0 edge:
0 → 112.7, 0 → −5.13, −5.13 → −165.6). Laser and punch CAM joins them, but a cut path then has needless
vertices and some software warns. **Should:** one line per straight edge of the outline; the bend lines on
their own layer.

## F-052

**Missing capability.** `feature.pattern` (and `feature.mirror`) copy a hole but not the cosmetic thread on
it, and `feature.thread` takes one face, so the V-block pair's eight identical M6 and M8 threads are eight
features. **Should:** a thread that follows its hole into patterns and mirrors, or a thread on several faces
(a named set) at once. Reproducer:
[`findings/F-052-pattern-drops-thread/repro.json`](findings/F-052-pattern-drops-thread/repro.json).

## F-053

**Missing capability.** `file.export` of projected views (end, side, top as SVG or DXF) draws the outlines
only: no dimensions, centre lines or title block, and one stroke width for every layer, so not the thick
visible and thin hidden lines of ISO 128. A workshop drawing still needs another program. **Should:** at
least line weights per layer and centre lines on holes; dimensions from the model's variables later.
