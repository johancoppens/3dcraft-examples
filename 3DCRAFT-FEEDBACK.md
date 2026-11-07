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
| [F-004](#f-004) | Performance | A modelled thread takes 3.5 s to regenerate, measures on it 1 s more; 27 s of CPU | socket-head-cap-screw | load budget exceeded (4.8 s wall, 27 s CPU) |
| [F-005](#f-005) | Agent friction | `body.appearance` replaces the whole appearance; fields left out are dropped | socket-head-cap-screw | finish lost silently |
| [F-006](#f-006) | Bug | A modelled thread on a tip chamfered 0.75 P deep is refused for M3 to M6 | socket-head-cap-screw | workaround used |
| [F-007](#f-007) | Missing capability | Loft sections cannot lie on a cylinder | probe for ship-propeller | planar approximation |
| [F-008](#f-008) | Bug | Fillets at propeller blade roots fail above 1 mm, and at 1 mm on blunt sections | probe for ship-propeller | root fillet ≤ 1 mm |
| [F-009](#f-009) | Bug (suspected) | Shelling a lofted hull with a small bow section: "what fits is below 0.0571 mm" | probe for rc-yacht-hull | larger bow section |
| [F-010](#f-010) | Performance | Curves from formulas fit about 400 control points at the default tolerance: 40 s for six sections | probe for ship-propeller | tolerance 0.001 mm |
| [F-011](#f-011) | Agent friction (was filed as a missing capability) | Expressions in `sketch.spline` `through` points are refused with an error that does not mention `live: true`, which takes them | probe for ventoux-relief | numbers baked in |
| [F-012](#f-012) | Missing capability | No surface through a grid of points | probe for ventoux-relief | loft of row splines |
| [F-013](#f-013) | Bug | Screen-space reflections smear a patch onto a threaded shank in the CPU renderer | socket-head-cap-screw | reflections off in the preview |
| [F-014](#f-014) | Missing capability | A thread has no fit allowance, so a mating pair touches and cannot be shown clear | probe for moka-pot | one thread cosmetic |
| [F-015](#f-015) | Missing capability | A folded panel cannot have a slit, and thick panels do not fold to 180° | probe for mailer-box | none in the end: rolled ends as two 90° creases, slots as holes |
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
| [F-054](#f-054) | Agent friction | The Workshop environment's warm key light tints every glossy neutral body yellow at rotation 0 | screw, t-slot, v-block-pair | rotation per example |
| [F-055](#f-055) | Agent friction (minor) | The `hole: true` face query returns a hole's bore only, not its countersink or drill-point cone | v-block-pair (review) | measure by `madeBy` |
| [F-056](#f-056) | Missing capability (minor) | A modelled or cosmetic thread cannot run through a hole's whole length (its run-out must fit inside) | v-block-pair | thread 1 mm short |
| [F-057](#f-057) | Agent friction | An output is refused as unknown when its proof bounds lie 1e-6 apart | v-block-pair (prompt test) | distance used instead |
| [F-058](#f-058) | Missing capability (cosmetic) | Thick fold panels leave every folded corner open: a notch the board deep, light through the crease | mailer-box | visible notches |
| [F-059](#f-059) | Missing capability | An assertion is measured only at the current parameter values | mailer-box | hidden closed copy |
| [F-060](#f-060) | Agent friction | On a thick fold panel `startCap` is the far face and `endCap` the face on the sketch, the opposite of an extrusion | mailer-box | none |
| [F-061](#f-061) | Missing capability | A fold's boundary takes straight lines only: rounded ears become chords, cut as facets | mailer-box (review) | chorded ears |
| [F-062](#f-062) | Bug | The CPU studio look shows a flat face's triangulation diagonal as a dark line | mailer-box (review) | none |
| [F-063](#f-063) | Agent friction | A fold's DXF names its layers `boundary` and `valley`; die makers and plotters expect CUT and CREASE | mailer-box (review) | none |
| [F-064](#f-064) | Bug | A loft through closed splines gives two side faces the same name | headphone-stand | none |
| [F-065](#f-065) | Bug | A fillet at the foot of a lofted column on a plane is refused from 12 to 14 mm | headphone-stand | 10 mm root fillet |
| [F-066](#f-066) | Bug | Rounding a rod's end to a full ball is refused, and the error points at the refused radius | headphone-stand | ball as its own body |
| [F-067](#f-067) | Bug (proof weakness) | A draft assertion passes on sampled faces (`proven: false`) without a warning, and reports radians | headphone-stand | none |
| [F-068](#f-068) | Missing capability | No assertion that a body is in one piece (`shells` counts voids too) | headphone-stand | count of cut faces |
| [F-069](#f-069) | Bug | `feature.developable` refuses a straight side facing one point of a curve (the square-to-round) | square-to-round-transition | corners and fills sewn |
| [F-070](#f-070) | Bug | `feature.plate` refuses a developable fan (a cone running into a point): "freeform face has a pole" | square-to-round-transition | corners rounded 10 mm |
| [F-071](#f-071) | Bug | The plate of a corner developable rounded to 5 mm is refused at the default tolerance after 10 s | square-to-round-transition | tolerance 1e-4 mm |
| [F-072](#f-072) | Performance | `feature.unfold` takes 0.7 s per quarter cone at any tolerance; with the plate the example opens in 8 s | square-to-round-transition | budget exception |
| [F-073](#f-073) | Agent friction | `feature.unfold` cuts its seam opposite the first face listed, undocumented; no way to name the seam | square-to-round-transition | faces ordered |
| [F-074](#f-074) | Missing capability | A flat pattern's DXF writes every edge, straight ones too, as a 385-point spline (534 KB) | square-to-round-transition | none |
| [F-075](#f-075) | Bug | A chamfer round the rim of a level cut through a leaning prism with rounded arrises is refused | splayed-stool | chamfered arrises |
| [F-076](#f-076) | Performance | `volumeBelow` and `sectionExtent` take about 1 s per body with freeform faces, even far from the plane | splayed-stool | rounds left off the feet |
| [F-077](#f-077) | Missing capability | `cut.list` lists plates and sheet metal only: no rough-stock sizes of solid-wood parts | splayed-stool | sizes in the README |
| [F-078](#f-078) | Missing capability (minor) | `boxMax` and `extent` take bodies, not faces | splayed-stool | section 0.001 mm above the floor |
| [F-079](#f-079) | Agent friction (minor) | `9.81 m/s^2` is refused ("s is the unit second only right after a number") | splayed-stool | `9.80665 N / (1 kg)` |
| [F-080](#f-080) | Performance (file size) | 3MF exports are stored (uncompressed) ZIPs with 17 significant digits per coordinate | headphone-stand (review) | the examples' tool deflates them |
| [F-081](#f-081) | Agent friction | Mesh-export quality is relative to the model's size (0.33 mm on a 270 mm part at `normal`); no print preset | headphone-stand (review) | explicit `tolerance` |
| [F-082](#f-082) | Missing capability (minor) | Section caps in `view.render` draw every body in one colour | headphone-stand (review) | none |
| [F-083](#f-083) | Missing capability | A wood pattern has one frame (axis, pith) per body: pattern copies cannot each have their grain | splayed-stool (review) | legs split into bodies |
| [F-084](#f-084) | Agent friction (minor) | Where `material.preset` puts a wood's pith (from the body's box) is not reported | splayed-stool (review) | trial renders |
| [F-085](#f-085) | Missing capability | A flat pattern's DXF from `feature.unfold` has the outline only: no tangent, ruling or bump lines on a layer | square-to-round-transition (review) | outline only |
| [F-086](#f-086) | Missing capability | `cut.list` and `cut.export` refuse a plate whose edges are broken (a 0.3 mm chamfer) | fpv-drone-frame | DXF from the sketches |
| [F-087](#f-087) | Missing capability | No measure of whether a round tool of radius r can cut a profile; an offset cannot be offset again | fpv-drone-frame | Steiner area check |
| [F-088](#f-088) | Agent friction | A chamfer's `chain` stops at sharp corners; no "every edge of a face" | fpv-drone-frame | 22 edge pairs per plate |
| [F-089](#f-089) | Bug | `feature.plate` joints `onto` are refused along a flat-to-cone tangent chain | square-to-round-transition | rims square, inside the laps |
| [F-090](#f-090) | Missing capability | `feature.unfold` refuses a curved fold line; `feature.plate` cannot cross a fold | square-to-round-transition | straights as rings |
| [F-091](#f-091) | Performance | `feature.developable` makes 184 rulings at any tolerance where a ruled loft of the same arcs makes 2 | square-to-round-transition | ruled loft, asserted developable |
| [F-092](#f-092) | Bug | The plate of a corner rounded 5 mm is refused at some sizes ("the rim could not be traced … 2.52 off") | square-to-round-transition | 8 mm corners |
| [F-093](#f-093) | Performance | `boxMax` of one lofted propeller takes 5.3 s (`sectionExtent` 0.03 s); joining blades to a hub adds 0.9 s | fpv-drone-frame | blades and hub two bodies |
| [F-094](#f-094) | Agent friction | A measure's `axis` takes no expression | fpv-drone-frame | hidden turned copy |
| [F-095](#f-095) | Bug | A fillet whose border would cross a smooth edge onto the next face is refused | solitaire-ring | prong roots left sharp |
| [F-096](#f-096) | Agent friction (minor) | `body.material` refuses a density-valued variable ("is a density, not a plain number") | solitaire-ring | written out in kg/m³ |
| [F-097](#f-097) | Missing capability (cosmetic) | The studio look cannot draw a gem: no internal reflection or dispersion | solitaire-ring | stone half transmissive |
| [F-098](#f-098) | Performance | An `overlap` or `clearance` assertion between a 58-face stone and a ring costs 2 to 3 s at every load | solitaire-ring | `distance` checks |
| [F-099](#f-099) | Missing capability | Two root fillets meeting where a convex crease runs into them are refused | cast-handwheel | spokes without draft |
| [F-100](#f-100) | Bug | A fillet crossing a revolved arc's face split off-centre (20° from the sketch plane) is refused | cast-handwheel | hub as a cone |
| [F-101](#f-101) | Missing capability | `feature.draft` refuses the flat sides of a body swept along a bend | cast-handwheel | no `feature.draft` in the example |
| [F-102](#f-102) | Bug (proof weakness) | `measure.draft` finds 0° on a face swept along an arc but proves only −21° (−67° in the model), reported as proven | cast-handwheel | none |
| [F-103](#f-103) | Performance | Cutting a spot face across a boss filleted to a torus rim takes 0.6 s (everything before it 0.16 s) | cast-handwheel | handle on the rim's centre line |
| [F-104](#f-104) | Agent friction | A `section` render on a named view keeps the half nearest the camera, so no cut shows without `flip` | cast-handwheel (review) | `flip: true` |
| [F-105](#f-105) | Missing capability | `clearance` and `distance` refuse sheets ("a body that is a sheet, which has no inside") | square-to-round-transition (prompt test) | box checks |
| [F-106](#f-106) | Missing capability (minor) | No volt, ampere, rpm or minute units | fpv-drone-frame | `1750 / (60 s)`, a plain 25.2 |
| [F-107](#f-107) | Bug | Root fillets between a swept oval spoke and a torus rim are refused at tolerance 1e-4 mm and built at 1e-5 mm | cast-handwheel (review) | tolerance 1e-5 mm |
| [F-108](#f-108) | Missing capability | `feature.thread` knows ISO metric threads only: no pipe threads (ISO 228-1 G, ISO 7-1 R, NPT) | hydraulic-cylinder | G 3/8 ports drilled, not threaded |
| [F-109](#f-109) | Bug | A seat cut across a filleted prong head is refused as "zero thickness" at tolerance 1e-6 mm and built at 1e-7 mm | solitaire-ring (prompt test) | tolerance 1e-7 mm |
| [F-110](#f-110) | Agent friction | `feature.boolean` takes one target and one tool, so subtracting four bodies takes four chained features | hydraulic-cylinder | steps |
| [F-111](#f-111) | Missing capability | `measure.clearance` reports a cosmetically threaded stud in its cosmetically threaded hole as an overlap | hydraulic-cylinder | no interference check of screwed parts |
| [F-112](#f-112) | Agent friction | An arc centre given as plain numbers in a sketch of expressions is free and moves silently on a parameter change | spiral-staircase | tread 7 mm² too large; revolved instead |
| [F-113](#f-113) | Bug | After a parameter change an arc centre left 1.4e-11 mm off makes a 3 mm round-over "at the edge of tolerance"; a fresh build passes | spiral-staircase | treads and landing revolved |
| [F-114](#f-114) | Bug | A chained round-over through a plan corner rounded into an arc is refused | spiral-staircase | tread corners square |
| [F-115](#f-115) | Missing capability | `feature.extrude` `upTo` refuses a rational freeform (swept) face | spiral-staircase | balusters cut by a tangent plane |
| [F-116](#f-116) | Performance | Joining a helical swept rail to 42 balusters takes 7.5 s | spiral-staircase | balusters stop 0.5 mm under the rail |
| [F-117](#f-117) | Performance, proof weakness | `boxMax` of a helical swept tube takes 63 s (250 s CPU) and is not proven; distances to it are loose | spiral-staircase | rail's clearances not asserted |
| [F-118](#f-118) | Bug | A top view of 14 stacked rings is refused ("too many overlapping triangles"); projected views draw hidden bodies | spiral-staircase | no plan or elevation drawing |
| [F-119](#f-119) | Missing capability | No measure of the angle between two planar faces, edges or directions | spiral-staircase (review) | tread angle and going asserted on formulas only |
| [F-120](#f-120) | Bug | `measure.continuity` of a fillet's edge on an extruded closed-spline wall reports no continuity (exhausted, 8 s) | guitar-body | roundover not proven on the sides |
| [F-121](#f-121) | Missing capability | `measure.continuity` refuses a fillet's edge on a freeform (network) face | guitar-body | carved top's roundover not proven |
| [F-122](#f-122) | Bug (proof), performance | `boxMax` of a body with a freeform top is not proven closely enough to be a value, and costs seconds | guitar-body | depths measured to the top face |
| [F-123](#f-123) | Missing capability | `measure.ray` (material along a line) cannot be an assertion or an output | guitar-body (review) | wood under each pot hole not asserted |
| [F-124](#f-124) | Bug | An 11-section loft has an edge 1.0 mm off its own face, so every cut and boolean on it is refused | ship-propeller | root section placed to avoid it |
| [F-125](#f-125) | Performance | `feature.pattern` × 4 at 90° of disjoint lofted blades costs 1 s where × 2 at 180° costs 0.04 s | ship-propeller | load budget |
| [F-126](#f-126) | Performance | `feature.shell` of a lofted hull takes 18 to 29 s; `feature.plate` of its faces 0.2 s | rc-yacht-hull | laminate plated, not shelled |
| [F-127](#f-127) | Bug | `measure.below` and `levelFor` refuse a plane between a spline body's lowest point and its control net | rc-yacht-hull | bumper not floated alone |
| [F-128](#f-128) | Performance | `measure.floating` with wholly submerged appendages takes 2.7 s against 0.6 s for the hull alone | rc-yacht-hull | envelope floated under net weight |
| [F-129](#f-129) | Performance | A 3 mm fillet on a small part joined to a hull makes `levelFor` and floating 2 to 3 times slower | rc-yacht-hull | bumper unrounded in the envelope |
| [F-130](#f-130) | Bug, performance | `document.interference` cannot check `feature.plate`'s own joints on a lofted hull ("unknown … at the edge of tolerance"), in 31 s | rc-yacht-hull (review) | laminate joints unchecked |
| [F-131](#f-131) | Agent friction (minor) | The error for a non-integer exponent of `^` does not point to `pow(x, y)` | guitar-body (prompt test) | `exp(x * ln(2))` written instead |
| [F-132](#f-132) | Performance | Subtracting a core from a drafted blank whose rim has a chained round takes 1.4 s against 0.08 s without it | moka-pot | collector's rim left sharp |
| [F-133](#f-133) | Bug | `datum.plane` from a face name finds the face before a later draft, while `feature.fillet` follows the same name to the drafted body | moka-pot | boss drafted about its own base |
| [F-134](#f-134) | Agent friction | Feature names work in face names in params but not in query globs; `mL` works but is not in the unit table | moka-pot | references renumber on every inserted step |
| [F-135](#f-135) | Bug | `feature.surface.trim` along z of an 8-point loop over a lofted terrain does not converge, flipping with the data's 4th decimal | ventoux-relief | no road drawn |
| [F-136](#f-136) | Performance | A road band intersected with a lofted terrain adds 4.8 s and 56 s of CPU to the load | ventoux-relief | no road drawn |
| [F-137](#f-137) | Bug | A slab intersected with a terrain is refused ("a piece of a face too thin") when its face passes near a saddle, at any tolerance | ventoux-relief | contour interval capped at 200 m |
| [F-138](#f-138) | Performance (file size) | A live spline point costs about 670 bytes in the `.3dcraft` (pretty-printed JSON in an uncompressed ZIP) | ventoux-relief | grid capped at 37 × 29 |
| [F-139](#f-139) | Missing capability | A flat face cannot become a sketch's profile or be extruded | ventoux-relief | layers are slices, not flat sheets |
| [F-140](#f-140) | Bug | `feature.plate` of a trimmed patch is refused: "the joint reaches past the faces' surfaces" | ventoux-relief | no road drawn |

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
Its CPU time is 27 s (`/usr/bin/time`: 26.8 s user at 4.8 s wall): the regeneration is spread over many
threads, so the single-threaded web build would wait about that long.
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
A smaller case from the ship propeller (8 steps, 0.1 s): a rolling-ball fillet between an elliptic lofted fin
and a Ø 100 cylinder builds at 3 mm and is refused at 5 mm, once the radius exceeds the fin's edge curvature,
although the ball rolls on the fin's convex side:
[`findings/F-008-fillet-at-blade-roots/fin-on-cylinder.json`](findings/F-008-fillet-at-blade-roots/fin-on-cylinder.json).

## F-009

**Bug (suspected).** A hull lofted through eight station splines, with a small bow section (8 × 6 mm), is
refused by `feature.shell` 1.5 mm: "the offset of the freeform face would fold over … what fits is below
0.0571289 mm". A 30 × 20 mm bow section shells fine. The bound looks far smaller than the section's
curvature allows. Reproducer (44 steps):
[`findings/F-009-shell-of-lofted-hull/repro.json`](findings/F-009-shell-of-lofted-hull/repro.json).
The RC yacht's prompt tester met the same family: `feature.thicken` of the lofted deck's cambered face is
refused at 8 mm ("the freeform face has a pole or a border or corner drawn into a point, where its normal and
so its offset are not defined") and built at 7 mm (no reproducer kept).

## F-010

**Performance.** A closed `sketch.curve` from formulas is fitted within the document's tolerance; at the
default 1e-6 mm each airfoil section of a 600 mm propeller became a spline of about 400 control points, and
six sections lofted, patterned and joined regenerate in 40 s using 1.5 GB. At 0.001 mm it is 100 to 150
points, 11.6 s and 0.56 GB. On the headphone stand, elliptic formula sections had 35 to 86 control
points each even at 0.001 mm, and lofted and cut they cost 2.0 s against 0.13 s for live splines. **Should:** a curve fitted to what it needs (curvature-adaptive, or a separate
fitting tolerance), so a formula section does not cost hundreds of points at the topological tolerance.

## F-011

**Agent friction** (first filed here as a missing capability, which it is not). `sketch.spline` with `through`
points refuses an expression in a point between the ends: "a point the spline passes through between its ends
is fitted, not held: give it as numbers, or give `control` points". `live: true` takes such points (they are
the spline's own points, refitted at every regeneration), and the Mont Ventoux relief uses it for its vertical
exaggeration, but the error does not point to it, so the probe and two builders baked numbers in. **Should:**
the error names `live: true`. Also seen: an expression is capped at 4096 bytes, which a section written as
formulas of a table (the ship propeller) runs into, and closed control-point splines refuse expressions.

## F-012

**Missing capability (minor).** There is no command that makes a surface through a grid of points (or from
a B-spline surface's control points). A loft through one spline per row works well (a 60 × 40 grid opens in
1.1 s), so this is about convenience and fidelity across the rows, not a blocker. The guitar body's carved top, a
sheet from a grid of control points, took 24 curve sketches and 15 knot formulas to make an exact Gordon
network (`feature.surface.network`).

## F-013

**Bug (rendering).** The CPU renderer's studio look draws a smeared, mirrored patch on the thread of the
socket head cap screw next to its head, at 1000 × 750 and 1600 × 1200 (not visible at 480 × 360). With
`look.reflections: false` the patch is gone and the rest of the picture is unchanged; `specularShadow` has
no effect on it. Reproduce: build `examples/01-socket-head-cap-screw`, then `view.render` with `"camera":
{"eye": [48, -52, 30], "target": [-11, 0, -1], "up": [0, 0, 1], "fovY": 27}`, the gallery look
(`studio`, `workshop`, `aces`, exposure 0.5, `rotation` 90, `accumulate` 4), 1000 × 750; compare
`reflections` true and false around the thread's last turns. **Workaround in the example:** the preview is
rendered with `reflections: false`. The same artefact draws a jagged ghost of the V-block
pair's polished pin on the flat ground end face of a block.

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
**Should:** slits (cuts inside a panel) and 180° folds of thick panels. The mailer box example got round both without a workaround in the model:
a rolled end is two 90° creases with a narrow top panel between, and the locking tabs drop into slots that are
holes in the base panel, which thick panels accept.

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
("has no body"). Reproducers:
[`findings/F-025-colour-of-cut-faces/repro.json`](findings/F-025-colour-of-cut-faces/repro.json), and for
the consumed body [`consumed-body.json`](findings/F-025-colour-of-cut-faces/consumed-body.json) (the
hydraulic cylinder paints only the outside of its parts: 26 to 37 names per part, each list right after its
feature, before a later feature takes the body).
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
On a saturated face the shadow renders desaturated (tan on the headphone stand's yellow base) rather than a
darker yellow.
The jagged shadow line also crosses curved faces (a fillet on the headphone stand).
On a tall model of thin bars (the spiral staircase's balusters) the ground shadow on a plain background
draws as faint streaks.

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

## F-054

**Agent friction (rendering).** In the studio look's Workshop environment at rotation 0, the warm key light
tints every glossy neutral body yellow or olive, metallic or dielectric: polished steel reads as brass,
black oxide as bronze, clear anodising as champagne (the screw, the T-slot profile, the V-block pair). A
builder cannot tell this from a material error. Turning the environment (`look.rotation`, often 180)
gives neutral metals. **Should:** a key light whose colour reads neutral on neutral materials, or the
environment's default turned so it does; at least say it in the look's documentation. On the square-to-round transition no rotation renders both neutral:
up-facing flat metal reads dark olive at 180 and 270, vertical metal yellow at 0, 90 and 270. On the solitaire
ring, near-white glossy faces (the stone's crown facets) pick up a lime-yellow tint at grazing angles in every
variant tried. On the hydraulic cylinder a chrome rod (roughness 0.06) streaks brown at every
rotation, with reflections on or off, and bare up-facing steel reads brass or olive. On the RC yacht the
clearcoated carbon preset reads bronze, gold or white in any view from below, at all four rotations (it
mirrors the floor). On the moka pot, flat satin-aluminium faces in the gallery look (Workshop, ACES,
+0.5) saturate to a uniform near-white brighter than the plain background, so the metal reads as white
plastic; even at #8a8f95 the iso view reads white, and only a lower camera gives the facets metallic contrast.

## F-055

**Agent friction (minor).** The face query `{"hole": true}` returns a hole's bore cylinder only, not its
countersink or its drill-point cone, so a "wall around the hole" check over that set silently skips the
nearest faces (the V-block pair's countersink came 0.7 mm closer to a groove than its bore).

## F-056

**Missing capability (minor).** `feature.thread` needs its quarter-turn run-out to lie inside the cylinder,
so a hole cannot be threaded through its whole length (a nut, a tapped plate, the V-block clamp's 10 mm
crossbar): "the thread with its run-out reaches 10.9375 mm … the cylinder is 10 mm long". **Should:** a
thread `through` that runs out of both ends. Reproduce: in `examples/07-v-block-pair`, set
`clamp_thread_length` to `clamp_bar`.

## F-057

**Agent friction.** A `variable.measure` output of `boxMax` or `extent` on the V-block pair's screws was
refused as "not proven closely enough to be a value: found 108.642135 mm (at most 108.642136 mm)": an output
whose proof bounds lie a millionth of a millimetre apart, well inside the document's tolerance of the model's
size, is unknown rather than a value. The `extent` of an unfolded flat pattern cannot be an output either ("at least 0 mm"), on the
square-to-round transition: [`findings/F-057-output-near-exact/repro.json`](findings/F-057-output-near-exact/repro.json).
The RC yacht's bulb, a revolved formula curve, gives no `boxMin` or `extent` output either (found
-20.985 mm, at least -21.014 mm):
[`revolved-curve.json`](findings/F-057-output-near-exact/revolved-curve.json).
**Should:** an output takes the found value when its bounds lie within
the document's tolerance (scaled to the model, as an assertion's `tol` does), and says how far it is proven.

## F-058

**Missing capability (cosmetic).** `feature.fold` with thick panels leaves every folded corner open: a notch
the board's thickness deep runs along each crease, with a line of sight through it (a 45° ray through a
folded corner meets nothing). Real board bends round the crease. **Should:** the crease bridged by a bent
strip (a cylinder sector of the panel's thickness). Reproducer:
[`findings/F-058-open-crease-corners/repro.json`](findings/F-058-open-crease-corners/repro.json).

## F-059

**Missing capability.** An assertion is measured at the current parameter values only. The mailer box is
shown half open (Fold 0.71) but must be proven closed; a `when` makes the check inactive at the default
rather than proving it at another value, so the example carries a hidden second fold at the closed angles.
**Should:** an assertion measured at given values of some variables (`at: {"fold_amount": 1}`), as
check-range already evaluates other points. Reproducer:
[`findings/F-059-assert-at-other-values/repro.json`](findings/F-059-assert-at-other-values/repro.json).

## F-060

**Agent friction.** On a thick fold panel `startCap` names the far face and `endCap` the face on the sketch,
the opposite of an extrusion's, and the documentation does not say so: the mailer box's first distance
assertions measured 203.2 mm instead of the inside 200 mm. Reproducer:
[`findings/F-060-panel-cap-sides/repro.json`](findings/F-060-panel-cap-sides/repro.json).

## F-061

**Missing capability.** The boundary of a `feature.fold` blank takes straight lines only, so the mailer's
rounded tuck ears are chords, and the DXF for the die or the plotter then cuts facets instead of arcs.
**Should:** arcs and splines in a fold's boundary (the creases stay straight).

## F-062

**Bug (rendering).** On the closed mailer box, the CPU studio look draws a dark diagonal line corner to
corner across the flat lid, apparently the diagonal of the face's triangulation; it stays with
`reflections: false` and with `ao: false`.

## F-063

**Agent friction.** `file.export` of a fold writes its DXF with the layers `boundary`, `valley`, `mountain`
and `cut`; die makers and cutting-plotter software expect CUT and CREASE (and sometimes PERF), and there is
no way to name or map the layers. **Should:** layer names given in the export (`"layers": {"boundary":
"CUT", "valley": "CREASE"}`), or die-line names by default.

## F-064

**Bug.** `feature.loft` through closed splines gives two of its side faces the same name, so a fillet or a
measure that names one of them is ambiguous. Reproducer:
[`findings/F-064-loft-face-names/repro.json`](findings/F-064-loft-face-names/repro.json).

## F-065

**Bug.** A fillet where a lofted column meets a plane (the headphone stand's column on its base) is refused
from 14 mm on a round column and 12 mm on an elliptic one ("the rolling ball along this edge could not be
followed"), though the column is far wider than that and the base flat. Reproducer:
[`findings/F-065-loft-root-fillet/repro.json`](findings/F-065-loft-root-fillet/repro.json). See also F-008.

## F-066

**Bug.** Rounding the end of a rod to a full ball is refused: with the radius equal to the rod's it is "too
large"; with a radius between half and the full radius the refusal says that exactly the rod's radius gives
a ball piece. Reproducers: [`findings/F-066-rod-end-round/`](findings/F-066-rod-end-round/).

## F-067

**Bug (proof weakness).** A `draft` assertion passes when its measure was taken on sampled faces only
(`proven: false` in the detail) without the not-proven warning other measures give, and its message gives
the angles in radians while the bound is written in degrees. Reproducer:
[`findings/F-067-draft-proof/repro.json`](findings/F-067-draft-proof/repro.json).

## F-068

**Missing capability.** There is no assertion that a body is one piece: `shells` also counts voids, so a cut
that leaves two loose pieces (the headphone stand's saddle cut at its widest, before it was fixed) passes
every check. **Should:** a `pieces` (or `lumps`) measure. Reproducer:
[`findings/F-068-one-piece/repro.json`](findings/F-068-one-piece/repro.json).

## F-069

**Bug.** `feature.developable` between a straight side and a curve fails where the side faces one point of
the curve ("still 995.98 off"): the natural square-to-round, rectangle and circle in one developable, is
refused at its last corner. Reproducer:
[`findings/F-069-developable-flat-triangle/repro.json`](findings/F-069-developable-flat-triangle/repro.json).
**Workaround in the example:** four corner developables between two arcs and eight half-triangle fills,
sewn.

## F-070

**Bug.** `feature.plate` refuses any developable fan, a cone that runs into a point ("freeform face has a
pole"), though the offset of a cone is well defined away from its apex. Reproducer:
[`findings/F-070-plate-of-fan/repro.json`](findings/F-070-plate-of-fan/repro.json). **Workaround in the
example:** the corners rounded 10 mm inside (a real sheet cannot be bent to a point either).

## F-071

**Bug.** At the default tolerance (1e-6 mm) the plate of a corner developable rounded to 5 mm is refused after
about 10 s ("offset could not be approximated"); at 1e-4 mm it works. Reproducer:
[`findings/F-071-plate-narrow-cone/repro.json`](findings/F-071-plate-narrow-cone/repro.json).

## F-072

**Performance.** `feature.unfold` takes about 0.7 s per quarter cone, the same at every tolerance; with
`feature.plate` (about 2.5 s) the square-to-round transition opens in about 8 s, 27.6 s to regenerate at its
longest. Reproducer: [`findings/F-072-unfold-cost/repro.json`](findings/F-072-unfold-cost/repro.json).
The load is 8.7 s of wall time but 27 s of CPU time, so the single-threaded web build would take about 27 s;
plating a quarter and mirroring it saves nothing (8.2 s), and with a union it is 11.5 s.
A copy of a plated body (mirror, pattern) costs about as much CPU as the plate itself, about 2 s each, and
giving the bodies a density adds the time of their exact mass properties at open (1.2 s wall): reproducer
[`findings/F-072-unfold-cost/copy-and-mass-repro.json`](findings/F-072-unfold-cost/copy-and-mass-repro.json).
**Workaround in the example:** a four-piece fitting (seams at the middles of the sides), one quarter pattern,
and the plated pieces as ruled lofts (F-091): 2.0 s wall and 3.3 s CPU instead of 8.7 s and 27 s.

## F-073

**Agent friction.** `feature.unfold` cuts a closed sheet open along the seam opposite the first face listed;
nothing documents it, and a seam cannot be named. **Should:** a `seam` parameter naming the edges to cut.
Reproducer: [`findings/F-073-unfold-seam/repro.json`](findings/F-073-unfold-seam/repro.json).

## F-074

**Missing capability.** A flat pattern from `feature.unfold` goes to DXF with every edge, the straight ones
included, as a 385-point cubic SPLINE: the transition's flat pattern is 534 KB, and CAM has to fit lines
back. **Should:** straight edges as LINEs and circular ones as ARCs where they are, splines only where the
edge is freeform. Reproducer:
[`findings/F-074-flat-pattern-splines/repro.json`](findings/F-074-flat-pattern-splines/repro.json).

## F-075

**Bug.** On a leaning square prism with rounded arrises (the stool's legs), a chamfer round the rim of a
level cut (the foot) is refused: "chain of freeform chamfers … not yet where one of the faces changes"; a
round on the same rim works. Reproducer:
[`findings/F-075-chamfer-slanted-rim/repro.json`](findings/F-075-chamfer-slanted-rim/repro.json).
**Workaround in the example:** the arrises chamfered instead of rounded.

## F-076

**Performance.** `volumeBelow` and `sectionExtent` take about 1 s per body once it has freeform faces (a
leg whose foot rim is rounded), even with the plane nowhere near those faces, while `volume` of the same
body is fast: the stool's load went from 0.3 to 2.8 s. Reproducer:
[`findings/F-076-volume-below-slow/repro.json`](findings/F-076-volume-below-slow/repro.json). See F-019.

## F-077

**Missing capability.** `cut.list` lists plates and sheet-metal parts only. Solid-wood parts (a round seat,
splayed legs, stretchers) get no rough-stock sizes, and the bodies of a pattern count as one. **Should:**
a cut list of every body with its bounding stock in the grain's direction and the count of copies.
Reproducer: [`findings/F-077-cut-list-solid-wood/repro.json`](findings/F-077-cut-list-solid-wood/repro.json).

## F-078

**Missing capability (minor).** `boxMax`, `boxMin` and `extent` measure bodies only, not faces, so the
footprint of a stool's feet cannot be measured from their contact faces; the stool measures a section
0.001 mm above the floor instead. With rounded feet, `boxMax` of the legs was also "not proven closely
enough" (F-057).

## F-079

**Agent friction (minor).** `9.81 m/s^2` is refused ("s is the unit second only right after a number");
the stool writes `9.80665 N / (1 kg)`. **Should:** compound units after a number (m/s^2, kg/m, N·m), as
outputs already show them.

## F-080

**Performance (file size).** `file.export` writes 3MF as a stored (uncompressed) ZIP with 17 significant
digits per coordinate: the headphone stand's 18 124 triangles make 1.6 MB, 88 bytes a triangle; deflated, the
same file is 340 KB, and 3MF consumers read deflate (the specification's own examples use it). **Should:**
deflate, and coordinates to the precision the tolerance needs. **Workaround in this repository:**
`tools/examples.py` rewrites every 3MF export with deflate (entries, order and dates unchanged).

## F-081

**Agent friction.** Mesh-export quality is relative: `normal` is a chordal tolerance of 1/1000 of the root of
the bodies' area, 0.33 mm at 10° on the 270 mm headphone stand, coarser than a 0.2 mm print layer, so flats
show across a printed curve. **Should:** for print formats (3MF, STL) an absolute tolerance in millimetres, or
a `print` preset finer than a layer, as the default.

## F-082

**Missing capability (minor).** `view.render` with `section` caps every body's cut in one colour, so an
insert in its pocket (the stand's steel disc) cannot be told from the part around it. **Should:** each cap in
its body's colour.

## F-083

**Missing capability.** A solid texture (`pattern`) has one frame, axis and pith, per body. The copies a
`feature.pattern` makes inside one body (the stool's four leaning legs) cannot each have their grain along
their own axis, so they show bands across them that read as short grain, and their end faces (the through
tenons) show long grain instead of end grain. **Should:** a grain frame that follows the feature or the
pattern instance that made the faces. The prompt test of the stool found a partial way: `face.appearance` on a
selection can give the faces of one lump their own pattern frame.

## F-084

**Agent friction (minor).** `material.preset` fits a wood's pith and axis from the body's box, but the
result does not report where it put them, so an agent needs trial renders to see the grain; the fitted
`axis` and `origin` should come back in the result.

## F-085

**Missing capability.** The DXF of a flat pattern from `feature.unfold` holds the outline only (18 splines on
the transition): no tangent lines between its flat and curved regions, no rulings or bump lines for press-brake
forming, no bend lines, on a layer of their own. A sheet-metal shop's pattern carries them. **Should:** the
pattern's inner face boundaries and a chosen number of rulings per curved region, on marking layers.

## F-086

**Missing capability.** `cut.list` and `cut.export` refuse a plate whose edges are broken: a 0.3 mm chamfer
round a carbon plate's outline or holes makes it "not a plate". Every CNC-cut plate has its edges broken.
**Should:** a plate is a plate whatever its edge treatment; the cut outline is the plate's largest section.
Reproducer: [`findings/F-086-cut-list-edge-break/repro.json`](findings/F-086-cut-list-edge-break/repro.json).

## F-087

**Missing capability.** There is no measure of whether a round tool of radius r can cut a profile (every
inside corner at least r, no gap narrower than 2r), and an offset profile cannot be offset again (which would
test it: offset out by r and back in). The drone frame proves it through Steiner's area formula of the outline
grown by r. On the guitar body the query side shows too: a face filter cannot tell a concave from a convex
partial cylinder (`hole: false` returns both), and a sharp inside edge is no face at all, so "no inside corner
below the router's radius" cannot be counted directly. **Should:** a `toolReach` measure, or offsets of
offsets, and a `concave` face filter. Reproducer:
[`findings/F-087-router-reach/repro.json`](findings/F-087-router-reach/repro.json).

## F-088

**Agent friction.** A chamfer's `chain` stops at sharp corners, and there is no option for every edge of a
face, so breaking the edges of a plate's outline takes 22 edge pairs per plate. **Should:** `edges` given as
a face (all its boundary edges) or a named set. The same on the spiral staircase: the end cap of a tube swept
along a helix meets side pieces numbered by the helix's half turns, so a rounded rail end cannot be named to
survive a parameter change. Reproducer:
[`findings/F-088-chamfer-whole-outline/repro.json`](findings/F-088-chamfer-whole-outline/repro.json).

## F-089

**Bug.** On the square-to-round transition's plate, a joint `onto` the end planes is refused along the chain
of edges where a flat triangle meets a cone tangentially; on the corner alone it works. Reproducer:
[`findings/F-089-plate-onto-tangent/repro.json`](findings/F-089-plate-onto-tangent/repro.json).
**Workaround in the example:** the plate's rims stay square to the sheet, inside the collar's and the
spigot's laps.

## F-090

**Missing capability.** A sheet with a straight band at its end (a duct fitting's lap) has a curved fold line
where the band meets a cone; `feature.unfold` refuses it ("images up to 0.98 mm apart"), and `feature.plate`
cannot plate across a fold. **Should:** the unfold of a curved fold (the band then develops to a curved strip,
as a sheet-metal layout does). Reproducer:
[`findings/F-090-curved-fold/repro.json`](findings/F-090-curved-fold/repro.json).

## F-091

**Performance.** `feature.developable` between two arcs builds its surface with 184 rulings at any
tolerance; `feature.loft` (ruled) between the same two arcs gives the same surface with 2, and plating it
costs 0.73 s of CPU against 2.59 s. On the transition this took the load from 11.5 s to 3.3 s of CPU.
**Should:** a developable described as exactly as the loft when its rulings form a cone or a cylinder.
Reproducer: [`findings/F-091-developable-rulings/repro.json`](findings/F-091-developable-rulings/repro.json).

## F-092

**Bug.** The plate of a corner developable rounded to 5 mm is refused at some sizes of the transition (500 ×
500 to Ø 315: "the rim could not be traced … still 2.52 off"); 8 mm passes everywhere. See also F-070 and
F-071. Reproducer: [`findings/F-092-plate-rim-fan/repro.json`](findings/F-092-plate-rim-fan/repro.json).

## F-093

**Performance.** On one lofted propeller (three blades through six spline sections), `boxMax` takes 5.3 s
while `sectionExtent` of the same body takes 0.03 s; joining the blades to their hub with `feature.boolean`
costs 0.4 s of regeneration plus 0.5 s to measure the trimmed freeform faces. Reproducer:
[`findings/F-093-loft-measure-cost/repro.json`](findings/F-093-loft-measure-cost/repro.json).
On the B4-55 propeller (11 sections) measuring the joined propeller's volume is about 4 of its 9 s of CPU,
and lofts through sharp-edged sections took 111 s (398 s of CPU) to load.
**Workaround in the example:** blades and hub are two bodies (they overlap 7.4 mm³), and every check is a
planar cut.

## F-094

**Agent friction.** A measure's `axis` (or direction) takes a fixed axis or vector, not an expression, so a
blade angle that follows the pitch formula cannot be measured along it; the drone measures a hidden copy
turned back by the angle. **Should:** directions as expressions, as positions already take. Reproducer:
[`findings/F-094-measure-axis-expression/repro.json`](findings/F-094-measure-axis-expression/repro.json).

## F-095

**Bug.** A fillet whose rolling border would cross a smooth (tangent) edge onto the next face is refused: the
solitaire's prong roots, where the prongs meet the shank near the smooth edge between two arcs of its oval
section, take a fillet of d/5 at 1 ct but not from 1.4 ct. Reproducer (a post near a rounded edge, a 3 mm root
fillet refused): [`findings/F-095-fillet-across-smooth-edge/repro.json`](findings/F-095-fillet-across-smooth-edge/repro.json).
**Workaround in the example:** the prong roots are left sharp, rather than with a radius tuned to pass.

## F-096

**Agent friction (minor).** `body.material` refuses a variable holding a density ("is a density, not a plain
number"), so a density defined once as a variable must be written out as `diamond_density * (1 m)^3 / (1 kg)`.
Reproducer: [`findings/F-096-density-variable/repro.json`](findings/F-096-density-variable/repro.json).
**Should:** a density accepted as a value with its unit.

## F-097

**Missing capability (cosmetic).** The studio look draws glass as one refraction of the picture behind it, with
no internal reflection and no dispersion, so a cut diamond reads as a glass blob (fully clear) or as frosted
glass (the solitaire's compromise, transmission 0.5). A brilliant's look is total internal reflection and fire.
**Should:** a few bounces of internal reflection for high-ior bodies, and dispersion as an option.

## F-098

**Performance.** An `overlap` or `clearance` assertion between a 58-face stone and the ring's gold costs 2 to 3 s
at every load (0.84 s rises to 2.8 and 3.8 s), while a `distance` between named faces costs too little to
measure. See F-019.

## F-099

**Missing capability.** Two root fillets that meet where a convex crease runs into them are refused: a spoke
drafted both ways from its parting line has a crease along it, and the fillets round its roots at the hub and
the rim cannot cross that crease. Reproducer:
[`findings/F-099-fillet-across-crease/repro.json`](findings/F-099-fillet-across-crease/repro.json).
**Workaround in the example:** the spokes are ovals parted at their widest line, without draft.

## F-100

**Bug.** A revolved arc becomes two faces split at the sketch plane, and a fillet crossing that split off
its centre is refused: at 20° off the plane it fails, at 0° and 90° it works. Reproducer:
[`findings/F-100-fillet-across-revolve-seam/repro.json`](findings/F-100-fillet-across-revolve-seam/repro.json).
**Workaround in the example:** the hub is a drafted cone, not a barrel.

## F-101

**Missing capability.** `feature.draft` refuses the flat sides of a body swept along a bend (the drafted edges
would become ellipses), so a curved spoke cannot be drafted for its pattern. Reproducer:
[`findings/F-101-draft-swept-sides/repro.json`](findings/F-101-draft-swept-sides/repro.json).

## F-102

**Bug (proof weakness).** `measure.draft` finds 0° on a face swept along an arc but proves only −21° (−67° on the
handwheel), and still reports the measure as proven. Reproducer:
[`findings/F-102-draft-bound-on-swept-torus/repro.json`](findings/F-102-draft-bound-on-swept-torus/repro.json).
See also F-067.
The moka pot shows it on a drafted prism's rounded corners: `measure.draft` finds 1.5° on the balls where three
rounds meet but proves only −6.0°, so a draft assertion over a whole cast body with its rounds is not proven:
[`fillet-corners.json`](findings/F-102-draft-bound-on-swept-torus/fillet-corners.json).

## F-103

**Performance.** Cutting a spot face (a revolve cut) across a boss filleted into a torus rim takes about 0.6 s,
against 0.16 s for everything before it. Reproducer:
[`findings/F-103-spot-face-cost/repro.json`](findings/F-103-spot-face-cost/repro.json).
**Workaround in the example:** the handle sits on the rim's centre line, not on DIN 950's boss.

## F-104

**Agent friction.** `view.render` with a `section` on the plane `zx` and the view `front` keeps the half nearest
the camera, so the picture shows the outside, not the cut, unless `flip: true` is given. **Should:** with a named
view, keep by default the half whose cut faces the camera.

## F-105

**Missing capability.** `measure.clearance` and `measure.distance` refuse a sheet body ("a body that is a sheet,
which has no inside"), so a flat pattern's clearance from a frame, or a sheet's distance to anything, must be
checked through boxes. A distance between a sheet and a body (or two sheets) is well defined. **Should:**
distance and clearance for sheets.

## F-106

**Missing capability (minor).** Expressions have no volt, ampere, watt, rpm or minute units, so a motor's
1750 KV is written `1750 / (60 s)` and a battery's 25.2 V as a plain number, and the root-stress formula
cannot check its own dimensions. **Should:** the electrical units and rpm (with min and h), as the mechanical
ones already exist.

## F-107

**Bug.** On the cast handwheel the root fillets between a swept oval spoke and the torus rim are refused at a
document tolerance of 1e-4 mm and built at 1e-5 mm (and at the default 1e-6 mm, which loads slower). A looser
tolerance should never refuse a fillet that a tighter one builds. Reproduce: in
`examples/13-cast-handwheel`, change `document.setTolerance` to 1e-4 mm.

## F-108

**Missing capability.** `feature.thread` knows ISO metric threads only. A hydraulic port's G 3/8 (ISO 228-1,
55° Whitworth form, 19 threads per inch) is refused by its designation ("unknown variable `G3`; size is an
ISO metric size … or a length"), and given as 16.662 mm with pitch 1.337 mm it is taken for a 60° metric
thread whose tap drill (15.325 mm) is larger than G 3/8's minor diameter (14.950 mm), so the port's hole is
refused. Pipe threads (ISO 228-1 G, ISO 7-1 R/Rp tapered, NPT) and the other inch and trapezoidal forms are
everyday in hydraulics, plumbing and pneumatics. Reproducer:
[`findings/F-108-pipe-threads/repro.json`](findings/F-108-pipe-threads/repro.json). **Should:** thread forms
as data (profile angle, pitch or TPI, taper), with the common standards' designations. **In the example:** the
ports are drilled to the minor diameter and say so.

## F-109

**Bug.** In the solitaire ring's prompt test (Sonnet's own model of the ring, 161 steps), the stone's seat cut
across the four prongs, whose roots are filleted into the gallery, is refused at 1.25 ct: "the result would
have zero thickness at (2.84, -2.06, 13.83): two of its parts touch there along an edge or in a point, at
F47:copy(0)/F40:side(e2,e3) and F47:fillet(0), and no solid can be that thin". It is refused at document
tolerances 1e-6, 1e-5 and 1e-4 mm and at 0.999 times the fillet radius, and built at 1e-7 mm and at 1.001
times the radius, so the parts do not touch: as in [F-107](#f-107), a looser tolerance refuses what a tighter
one builds. The same tester's first cutters, cylinders, were refused at 1.05 ct with "boolean produced an
invalid body: vertex 0 is 1.0076788542080009e-6 away from the end of edge 7" (no reproducer kept). Reproducer
(the tester's script at 1.25 ct and 1e-6 mm, not minimal):
[`findings/F-109-seat-cut-tolerance/repro.json`](findings/F-109-seat-cut-tolerance/repro.json), run with
`craft3d-cli run --script`.

## F-110

**Agent friction.** `feature.boolean` takes one target and one tool. The hydraulic cylinder's oil (the
chambers' solid, measured for their volumes) is a cylinder less piston, rod, head and cap: four chained
subtracts, each a feature with a name; the cutaway's box needs two. **Should:** `tool` (and for a union
`target`) as a list. Seen in the reviewer's count: about four of the example's 250 steps.

## F-111

**Missing capability.** `measure.clearance` (and an `overlap` assertion) reports a stud with a cosmetic thread
inside a hole with the matching cosmetic thread as an overlap: the cylinder's M14 × 1.5 rod end in its rod
clevis, and the tie rods in their tapped holes. A screwed assembly cannot be checked for interference without
listing the threaded pairs as exceptions. **Should:** a thread fit (a cosmetic external thread in a cosmetic
internal thread of the same size and pitch) counted as a fit, not an overlap, or an `except` list of such
pairs.

## F-112

**Agent friction.** In a sketch path whose points are expressions, an arc centre given as plain numbers
(`[0, 0]`) is only a starting guess: it keeps two degrees of freedom, and after a parameter change the solver
moves it (0.94 mm at a stair of Ø 2000 mm) without a warning, so the spiral staircase's tread came out 7 mm²
too large. Given as `["0 mm", "0 mm"]` it is held. **Should:** a warning when a re-solve moves a point the
script gave as a number, or plain numbers held like expressions in a sketch that has any. Reproducer:
[`findings/F-112-free-arc-centre/repro.json`](findings/F-112-free-arc-centre/repro.json).

## F-113

**Bug.** With the arc centre held at `["0 mm", "0 mm"]`, a parameter change leaves it 1.4e-11 mm off, and a
3 mm round-over of the landing is then refused ("a point too close to a face boundary to tell inside from
outside (at the edge of tolerance)"), where a fresh build at the same values passes. A re-solve should land
where a fresh solve does, and 1.4e-11 mm should not decide a fillet. The staircase's prompt tester met the same kind of
refusal for a revolved landing that ends at exactly 180° (3200 mm × Ø 1400 mm: "the largest radius that fits
there is below 0.53309 mm" for a 3 mm round-over), and joining a 3 mm plug into the end of a tube swept
along a helix was refused ("an imprinted curve that does not fit the edges it should coincide with", at the
edge of tolerance) until the plug was made 0.1 mm larger; no reproducers kept. Reproducer:
[`findings/F-113-fillet-near-exact-centre/repro.json`](findings/F-113-fillet-near-exact-centre/repro.json).

## F-114

**Bug.** A chained round-over along a tread's edge, through a plan corner rounded into an arc, is refused ("the
boolean that cuts this fillet refused it: … at the edge of tolerance"). Reproducer:
[`findings/F-114-round-over-arc-corner/repro.json`](findings/F-114-round-over-arc-corner/repro.json).

## F-115

**Missing capability.** `feature.extrude` with `upTo` refuses a rational freeform face ("extrude up to a face
does not support this: a rational freeform face as the end of an extrusion"), such as a handrail swept along a
helix: the spiral staircase's balusters cannot run up to the rail. **Should:** `upTo` on any face. Reproducer:
[`findings/F-115-extrude-up-to-swept-face/repro.json`](findings/F-115-extrude-up-to-swept-face/repro.json).
The same for a revolved face of a formula curve (an RC yacht's fin down to its bulb):
[`revolved-face.json`](findings/F-115-extrude-up-to-swept-face/revolved-face.json).

## F-116

**Performance.** Joining the spiral staircase's handrail (a tube swept along a helix) to its 42 balusters
takes 7.5 s (8.9 s CPU), on its own over the complex tier's load budget. The balusters stay a body of their
own, 0.5 mm under the rail. Reproducer:
[`findings/F-116-union-helical-rail/repro.json`](findings/F-116-union-helical-rail/repro.json).

## F-117

**Performance and proof weakness.** `boxMax` of a tube swept along a helix (the staircase's handrail) takes
63 s (250 s of CPU) and is not proven (found 792.75 mm where the true value is 791.2 mm); its distance to
the column costs 2 s at every load and is "not proven closely enough to be a value", and its distance to the
balusters (0.45 mm) is proven only above 0 mm. The reproducer takes about a minute. Reproducer:
[`findings/F-117-box-of-helical-tube/repro.json`](findings/F-117-box-of-helical-tube/repro.json).

## F-118

**Bug.** `file.export` of a top view of 14 stacked collars (rings on a column) is refused: "the view has too many
overlapping triangles to decide what is hidden; use a coarser `tolerance` or a simpler view". Projected views
also draw hidden bodies (the staircase's headroom gauges) and take no `bodies` to leave them out, so the
staircase ships no plan or elevation drawing. Reproducer:
[`findings/F-118-plan-view-stacked-rings/repro.json`](findings/F-118-plan-view-stacked-rings/repro.json).

## F-119

**Missing capability.** No `measure.*`, `variable.measure` or `assert.add` measure gives the angle between
two planar faces, two straight edges, or a face and an axis (`jointAngle` is for assemblies). The spiral
staircase's tread angle, and with it the going at the walking line, can be asserted only on the formulas
that made them, not proven from the geometry; the same holds for a bend angle, a mitre or a splay. **Should:**
an `angle` measure between two subjects (faces, edges, datum planes and axes).

## F-120

**Bug.** `measure.continuity` of the edge between a roundover (`feature.fillet`, 6.35 mm) and the side wall of
an extruded closed `sketch.spline` outline reports no continuity at all: every bound found 0 and
`within: false`, `exhausted: true` after 4096 pieces, about 8 s per edge, where the same fillet's edge on the
flat face proves G1. Reproducer:
[`findings/F-120-continuity-spline-wall/repro.json`](findings/F-120-continuity-spline-wall/repro.json).

## F-121

**Missing capability.** `measure.continuity` refuses the edge between a fillet and a freeform face made by
`feature.surface.network` ("the edge is neither a parameter line of the other spline face nor a curve
recovered on it"), so a carved top's roundover cannot be proven tangent. Reproducer:
[`findings/F-121-continuity-freeform-fillet/repro.json`](findings/F-121-continuity-freeform-fillet/repro.json).

## F-122

**Bug (proof) and performance.** `boxMax` of a body whose top is a freeform network face is "not proven
closely enough to be a value" (the reproducer: found 44.999999 mm, at most 45.0107 mm; the guitar body: found
44.990, at most 45.200 mm), and costs 1.5 s on a small body and about 2.4 s wall and 9 s of CPU on the
guitar (see [F-093](#f-093)). On the guitar an `area` assertion of one flat face also cost about 0.45 s wall
and 5 s of CPU, while the body's area and volume were free (no minimal reproducer: on a small body it costs
what the body's area does). Reproducer:
[`findings/F-122-boxmax-freeform/repro.json`](findings/F-122-boxmax-freeform/repro.json).

## F-123

**Missing capability.** `measure.ray` lists the faces a line meets, entering and leaving the material, but it is
not a measure of `assert.add` or `variable.measure`. The material along a given line (the wood under each of
the guitar's pot holes on the carved slope, a wall's thickness at one place, the depth of a blind hole) cannot
be checked or reported; `measure.thickness` gives a body's least thickness, not the thickness at a point.
**Should:** a `ray` measure (the length of material, or the distance to the first face, along a line from a
point) usable in assertions and outputs.

## F-124

**Bug.** An 11-section loft (a B4-55 propeller blade at P/D 0.7, its root section at 0.8 of the hub radius)
has an edge 1.016 mm away from its own face, so every cut and boolean on the blade is refused ("boolean
produced an invalid body: edge 1 is 1.0161979469882407e0 away from the surface of face 0"), here in a
`measure.section`. The builder met the same refusal in unions of a root trimmed by a cylinder. A loft
should never produce an edge off its face; when it cannot be built within tolerance it should say so.
Reproducer: [`findings/F-124-loft-edge-off-face/repro.json`](findings/F-124-loft-edge-off-face/repro.json).
The reviewer found the same at the default propeller's tip: a `measure.section` of the blade at 295 or 296 mm
(0.983 to 0.987 R) is refused ("edge 2 is 0.914 mm away from the surface of face 0") where 294 and 297 mm
pass (`craft3d-cli run examples/17-ship-propeller/ship-propeller.3dcraft --cmd measure.section --params
'{"of":"One blade","plane":"yz","offset":"295 mm","torsion":false}'`); and one extra, larger section near
the hub (a flared root) raised the load from 3.1 to 7.3 s (9.5 to 20 s of CPU) and its cut at the hub was
refused with an edge 0.71 mm off its face. Flat sections cannot follow the cylinder ([F-007](#f-007)), so the
propeller's root narrows by 14 % at the hub: with these refusals and [F-008](#f-008) a gallery propeller
cannot have a castable root.

## F-125

**Performance.** `feature.pattern` × 4 at 90° of a lofted blade (disjoint copies) adds 1.06 s (2.4 s of CPU)
to the propeller's regeneration, where × 2 at 180° adds 0.04 s. Reproducer:
[`findings/F-125-pattern-of-lofts/repro.json`](findings/F-125-pattern-of-lofts/repro.json).

## F-126

**Performance.** `feature.shell` of a hull lofted through seven stations takes 18 to 29 s (measured on a busy
machine), where `feature.plate` lays the same 0.6 mm laminate behind its faces in 0.2 s. A lofted hull is the
ordinary case for a shell (see also [F-009](#f-009) and [F-028](#f-028)). Reproducer:
[`findings/F-126-shell-of-lofted-hull/repro.json`](findings/F-126-shell-of-lofted-hull/repro.json).

## F-127

**Bug.** `measure.below` and `measure.levelFor` refuse a plane that passes between a spline body's lowest point
and its control net: "nothing of body 0 was found below the plane at offset -10.1, yet it may reach 1.9 below
it: not measured". Nothing below is an answer (zero volume), once the surface itself is shown to stay above
the plane. Reproducer:
[`findings/F-127-below-under-spline-bottom/repro.json`](findings/F-127-below-under-spline-bottom/repro.json).

## F-128

**Performance.** `measure.floating` of an RC yacht's hull with its fin and bulb takes 2.7 s, against 0.6 s for the
hull alone, though the appendages lie wholly below the water (their buoyancy is their volume). The model floats
the hull's envelope under the boat's weight less the appendages' buoyancy, which is exact. Also seen: a one-off
`measure.floating` does not take outputs as its `centerOfGravity`, and an `overlap` assertion between the
touching bumper and deck errors at the edge of tolerance (no reproducers). Reproducer:
[`findings/F-128-floating-with-appendages/repro.json`](findings/F-128-floating-with-appendages/repro.json).

## F-129

**Performance.** A 3 mm fillet on the yacht's 10 mm bow bumper, joined into the hull's envelope, makes
`levelFor` and `measure.floating` of the envelope two to three times slower. Reproducer:
[`findings/F-129-blend-slows-hydrostatics/repro.json`](findings/F-129-blend-slows-hydrostatics/repro.json).

## F-130

**Bug and performance.** On the RC yacht, `document.interference` of its eight bodies takes 31 s (188 s of CPU)
and cannot check the joints `feature.plate` made itself: hull and deck (joint `under`) and deck and transom
come back "unknown … at the edge of tolerance", although `feature.plate`'s documentation says interference
will tell. Plates that meet by construction should be known to touch, not to overlap. Reproduce: in
`examples/19-rc-yacht-hull`, run `document.interference`.

## F-131

**Agent friction (minor).** `2^(-22/12)` (the fret rule) is refused with "the exponent of `^` must be an integer
literal without a unit, as in `x ^ 2` or `x ^ -1`". `pow(x, y)` takes any exponent and the user guide says so,
but the error does not, so the guitar's prompt tester wrote `exp(x * ln(2))`. **Should:** the error names
`pow(x, y)`.

## F-132

**Performance.** Subtracting a drafted core from a drafted twelve-sided blank whose rim was rounded with a
chained fillet takes about 1.4 s, against about 0.08 s for the whole script without the round. A cast part's
rounded rim is the ordinary case. Reproducers:
[`findings/F-132-boolean-after-rim-round/repro.json`](findings/F-132-boolean-after-rim-round/repro.json) and,
for comparison, `without-rim-round.json` beside it.

## F-133

**Bug.** After `feature.draft` has taken a block, `datum.plane` `from` the face's original name (`F1:face(5)`)
lies on the face as it was before the draft (normal [1, 0, 0]), while `feature.fillet` follows the same name
to the drafted face; only the drafted name (`F2:copy(0)/F1:face(5)`) gives the drafted plane. One name should
mean one face: the latest, as the fillet reads it, or a refusal that names the drafted face. Reproducer:
[`findings/F-133-datum-from-earlier-face/repro.json`](findings/F-133-datum-from-earlier-face/repro.json).

## F-134

**Agent friction.** Face names carry sequential feature ids (`F12:side(e3)`), so inserting one step renumbers
every later reference. A feature's name works in its place in a feature's params (`"Base plate:face(1)"`,
undocumented) but not in a query's name glob (`*Base plate:face(2)` finds nothing where `*F1:face(2)` finds
the face). Separately, `ml`/`mL` works as a unit but is missing from the reference's unit table and from the
unit error's list. Reproducer:
[`findings/F-134-feature-names-in-face-names/repro.json`](findings/F-134-feature-names-in-face-names/repro.json).
**Should:** feature names everywhere a face name is taken, documented, and the unit table complete.

## F-135

**Bug.** `feature.surface.trim` projecting an 8-point loop along z onto a lofted terrain fails: "outer[0]: did not
converge: the walk from the start of a projection did not settle"; whether it fails flips with the fourth
decimal of the data and with the vertical exaggeration. The Mont Ventoux relief could not draw its road. Reproducer:
[`findings/F-135-trim-projection/repro.json`](findings/F-135-trim-projection/repro.json).

## F-136

**Performance.** A band along the road, intersected with the lofted terrain, adds 4.8 s and 56 s of CPU to the
relief's load; its 16 pin holes alone cost about 6 s of CPU. Reproducer:
[`findings/F-136-route-band-cost/repro.json`](findings/F-136-route-band-cost/repro.json).

## F-137

**Bug.** A slab intersected with the terrain is refused ("a piece of a face too thin to find a point inside it
(at the edge of tolerance)") when the slab's face passes near a saddle of the terrain, at tolerances 1e-6,
1e-4 and 1e-3 alike; the relief's contour interval stops at 200 m because 250 m meets it. Reproducer:
[`findings/F-137-slab-near-saddle/repro.json`](findings/F-137-slab-near-saddle/repro.json).

## F-138

**Performance (file size).** A live spline point costs about 670 bytes in the `.3dcraft` (pretty-printed JSON
in an uncompressed ZIP; see also F-080 for 3MF), so the relief's 1 MB budget holds a 37 × 29 grid and no
finer. Reproducer:
[`findings/F-138-live-spline-file-size/repro.json`](findings/F-138-live-spline-file-size/repro.json).

## F-139

**Missing capability.** A contour's region is there as a flat face (the slab's cut), but a sketch on that face
gets none of its outline and a face cannot be extruded ("has nothing to extrude"), so a laser-cut layer
cannot be made from a section. **Should:** a sketch from a face's outline (or `sketch.project`), or an
extrusion of a face. Reproducer:
[`findings/F-139-layer-from-section/repro.json`](findings/F-139-layer-from-section/repro.json).

## F-140

**Bug.** `feature.plate` of a trimmed patch of the terrain is refused: "along F9:startEdge(e8,e8): the joint
reaches past the faces' surfaces continued beyond their borders". Reproducer:
[`findings/F-140-plate-of-trim/repro.json`](findings/F-140-plate-of-trim/repro.json).
