# Catalogue: the 21 examples

The brief for every example: what the real thing is, what it must show of 3DCraft, its line of the gallery's
palette, its public parameters, what it must prove, and its risks. The order is the intended progression
(simple → difficult → complex); the final order in `README.md` follows the reviewers' scores. Sizes named here
are starting points: the builder verifies every number against the standard or source and cites it.

A builder may improve a brief (a better standard, a better parameter), but changes its domain, its main
techniques or its palette line only with the coordinator.

## Simple

### 1. Socket head cap screw · `socket-head-cap-screw` · machine building
- **Real thing:** ISO 4762 M8 × 30, property class 12.9; sizes M3 to M12 from a table of the standard's
  dimensions (head diameter and height, socket size and depth, thread length), coarse pitch per ISO 261.
- **Shows:** a constrained revolve profile; the hexagon socket with its drill-point cone; head chamfer and
  under-head fillet; `table.set` and a choice parameter read from the table; `feature.thread`.
- **Look:** black-oxide steel, satin.
- **Parameters:** size (choice from the table), length (the standard's preferred lengths for that size).
- **Proves:** socket depth ≥ the standard's minimum, head height = d, a volume worked out by hand.
- **Risks:** a modelled helical thread may break the load budget: decide between `feature.thread` (cosmetic)
  and a modelled thread by look and load time, and say why in the README.

### 2. T-slot aluminium profile · `t-slot-profile` · machine building, frames
- **Real thing:** a 30 × 30 mm B-type profile with 8 mm slots and a 6.8 mm core bore (tapped M8 at the
  ends), anodised 6063-T66; dimensions as common to several makers, cited.
- **Shows:** a fully constrained sketch built once and repeated by symmetry (`sketch.pattern`); extrusion to a
  length; section properties with `measure.section` (area, second moments) as outputs; mass per metre in
  kg/m (`variable.measure` with a unit).
- **Look:** clear anodised aluminium, brushed.
- **Parameters:** length.
- **Proves:** area and Ix within a few percent of the makers' published values; mass per metre.

### 3. Plywood wall clock · `wall-clock` · laser cutting, art
- **Real thing:** a Ø 300 mm dial of 6 mm birch plywood for a standard quartz sweep movement (shaft hole as
  the movement's, stated), engraved minute ticks and numerals, a keyhole hanger at the back, hands of black
  steel set to 10:10.
- **Shows:** `sketch.pattern` round a centre (ticks, markers); `sketch.textOnCurve` for the numerals; a
  choice parameter switching Roman and Arabic numerals with conditional features (`when`); hand angles from
  a time formula; SVG and DXF exports with cut and engrave apart.
- **Look:** light birch (the `beech` preset), black hands.
- **Parameters:** numerals (Roman, Arabic), diameter, time shown.
- **Proves:** 60 ticks and 12 numerals; the hand angles for the time; slots and holes ≥ the sheet thickness.

### 4. Turned walnut bowl · `turned-bowl` · woodturning, art
- **Real thing:** a Ø 220 × 85 mm salad bowl turned from a walnut blank, wall 7 mm, with a foot ring and a
  rounded rim; blank size stated.
- **Shows:** a spline profile with constraints, `feature.revolve`, a uniform wall (`feature.offsetProfile` or
  `feature.shell`), fillets; capacity in millilitres as an output.
- **Look:** walnut, oiled.
- **Parameters:** diameter, height, wall thickness.
- **Proves:** wall thickness (`measure.thickness`), capacity within a range, fits the stated blank.

### 5. Hex key stand · `hex-key-stand` · 3D printing
- **Real thing:** a desk stand for a metric hex key set to ISO 2936 (1.5 to 10 mm), printed in PLA without
  supports: hexagonal holes from a table with a print clearance, the keys stepped in height, sizes embossed.
- **Shows:** `table.set` driving holes; positions and depths from formulas; `sketch.text`; a first-layer
  chamfer; `measure.thickness` and `measure.draft` as print checks; 3MF export.
- **Look:** orange PLA (the `abs` preset, recoloured, matte).
- **Parameters:** clearance, label depth.
- **Proves:** nine holes, walls ≥ 1.2 mm, no overhang below 45°.

### 6. Steel bookend · `steel-bookend` · sheet metal, laser cutting
- **Real thing:** a bookend laser cut from 2 mm DC01 and bent once, powder coated: a decorative cut-out in
  the upright, rounded corners, inner bend radius per the material.
- **Shows:** `feature.sheetMetal` with one bend; a spline cut-out; the flat pattern exported as DXF with the
  bend line; `bendable` and hole-to-bend checks.
- **Look:** deep teal powder coat.
- **Parameters:** height, width.
- **Proves:** bendable; the flat pattern's size in closed form; cut-out ≥ 2.5 t + r from the bend.

## Difficult

### 7. V-block pair with clamp · `v-block-pair` · toolmaking
- **Real thing:** a matched pair of hardened, ground 90° V-blocks with a relief groove, side slots, tapped
  holes and a U-clamp with its screw; sizes from a common commercial range, cited.
- **Shows:** `feature.mirror` and `feature.pattern`; tapped holes (`feature.thread`); named sets
  (`set.define`) for the tapped holes; a test pin resting in the V (`measure.clearance` = 0 on both flanks);
  projected views exported as SVG (a technical drawing).
- **Look:** ground tool steel (bright, fine) with a black-oxide clamp.
- **Parameters:** pin diameter, block length.
- **Proves:** the pin's centre height in closed form (r·√2 above the V's apex), both flanks touching.

### 8. Square-to-round transition · `square-to-round-transition` · sheet metal, HVAC
- **Real thing:** a 400 × 300 rectangular duct to a Ø 250 round duct (EN 1505 and EN 1506 sizes) over
  300 mm, in 0.8 mm galvanised steel, with a flange on the rectangle and a spigot on the round end.
- **Shows:** `feature.developable` (four planar triangles and four cones), `feature.plate`,
  `measure.developability`, `unfold.map` / `feature.unfold` to one flat pattern with its seam, DXF export.
- **Look:** galvanised steel, light grey with low roughness.
- **Parameters:** rectangle width and height, round diameter, length.
- **Proves:** developable (zero Gaussian curvature), flat pattern area = surface area.

### 9. Mailer box · `mailer-box` · packaging
- **Real thing:** a FEFCO 0427 die-cut mailer of E-flute corrugated board for 200 × 150 × 60 mm inside, with
  dust flaps, a tuck-in front and locking tabs.
- **Shows:** a flat die-cut outline with crease lines; `feature.fold` from flat to closed, with a fold
  amount as a parameter (the box half open in the preview); `fold.check`; cut and crease lines exported as
  DXF for a cutting plotter.
- **Look:** kraft brown board.
- **Parameters:** inside length, width, height; fold amount.
- **Proves:** the folded inside size; the blank's size in closed form; no flaps colliding when closed.
- **Risks:** folding with the board's thickness: feasibility probe first.
- **Probe (2026-11-06):** works: one closed polyline blank, ten crease lines as construction lines,
  `feature.fold` with `panels: {thickness: 1.5 mm, clearance: 0.5 mm}`; the sketch is the inside face, so
  the inside size is the sketch's. Base corners chamfered and the side walls' creases offset by thickness +
  clearance so the dust flaps fold inside; lid and tuck flap as trapezoids. No slit locks and no rolled
  double walls (F-015): single side walls with dust flaps and a tuck-in lid. Fold in stages (walls, then
  lid): one angle for all creases makes the flaps pass through the walls. `file.export` with `fold` writes
  the DXF with layers `boundary`, `valley`, `mountain`, `cut`. `fold.check` says nothing useful here (no
  interior vertices). 0.02 s. Starting point: `plan/probes/q9-mailer-staged.json` (local).

### 10. Headphone stand · `headphone-stand` · 3D printing, product design
- **Real thing:** a one-piece stand printed in PETG upright without supports: a weighted round base, a slim
  upright and a wide curved saddle that keeps the headband's shape, a cable hook.
- **Shows:** lofts and sweeps, generous fillets, `measure.draft` proving every overhang ≥ 45° in the print
  orientation, `measure.thickness`, 3MF export.
- **Look:** sunflower-yellow PETG, satin.
- **Parameters:** height, saddle width.
- **Proves:** printable without supports; walls ≥ 1.2 mm; the centre of mass over the base.

### 11. Splayed-leg stool · `splayed-stool` · woodworking
- **Real thing:** an oak stool, seat height 450 mm, a 30 mm round seat with eased edges, four legs splayed
  and raked about 10° in wedged through-tenons, two stretchers; boards of stock thickness.
- **Shows:** datum axes and planes at compound angles; legs placed by `feature.pattern`; tenons and mortises
  by booleans; `cut.list` of the parts; fillets and chamfers.
- **Look:** oak, oiled.
- **Parameters:** seat height, splay angle.
- **Proves:** seat height, the feet inside a stable footprint, tenon proportions (a third of the leg).

### 12. 5-inch FPV drone frame · `fpv-drone-frame` · CNC, RC
- **Real thing:** a true-X freestyle frame: 5 mm carbon arms, 2 mm top and bottom plates, a 30.5 × 30.5 mm
  M3 stack, 16 × 16 and 19 × 19 mm motor patterns, aluminium standoffs, a cage for a 19 mm camera, 5.1"
  props.
- **Shows:** plates and arms from sketches; `sketch.pattern` and `feature.pattern`; several bodies;
  `measure.clearance` between the props and everything else; DXF of the carbon parts for the router.
- **Look:** carbon fibre with purple anodised standoffs.
- **Parameters:** prop size, arm thickness.
- **Proves:** prop clearance ≥ 3 mm; inside corners ≥ the router's tool radius.

### 13. Cast handwheel · `cast-handwheel` · casting, machine building
- **Real thing:** a DIN 950 handwheel of Ø 200 mm in cast iron, curved spokes, a revolving handle, a bore
  H7 with a DIN 6885 keyway; painted machine green, machined faces bright.
- **Shows:** `feature.draft` and fillets on every cast edge; spokes by sweep and `feature.pattern`;
  `measure.draft` proving the pattern draws from the mould; the keyway by a cut.
- **Look:** machine-green cast iron, bright machined faces.
- **Parameters:** diameter, bore.
- **Proves:** draft ≥ 1° on every cast face; DIN 950 sizes for the chosen diameter; keyway per DIN 6885.

### 14. Solitaire ring · `solitaire-ring` · jewellery
- **Real thing:** an 18 ct yellow-gold comfort-fit band in ring size 54 (ISO 8653: inner circumference
  54 mm) with a 1 ct round brilliant (Tolkowsky proportions: table 53 %, crown 34.5°, pavilion 40.75°) in a
  four-prong head.
- **Shows:** a revolved band; the brilliant's 57 facets by planar cuts repeated by `feature.pattern` round
  the axis; prongs by sweep; glass for the stone.
- **Look:** yellow gold and a clear stone.
- **Parameters:** ring size, carat.
- **Proves:** the inner circumference; 57 facets; the stone's diameter from the carat; gold mass from 18 ct
  density.
- **Risks:** many planar cuts on a small solid: feasibility probe first.
- **Probe (2026-11-06):** works, 0.55 s: a cylinder blank; per facet group a `datum.plane` through three
  ideal vertices, a large `sketch.rect` on it, an extrude outward as a cutter slab, `feature.pattern` × 8 at
  45°, `feature.boolean` subtract (the 16-facet sets as two groups of 8), the table last: exactly 57
  facets plus the girdle. Drive every vertex by formulas, never rounded numbers (rounded ones fall on the
  edge of tolerance). Band: revolve with an inner arc; prongs: sweep of a circle along a two-line path,
  transformed and patterned × 4, joined. Gold: `steel` preset recoloured (#e0b04a, metallic 1, roughness
  0.15) plus `body.material` for 18 ct gold's density; diamond: `glass` with ior 2.42, transmission 1 and a
  white absorption (the default is greenish) plus `body.material` 3510 kg/m³ (F-017). Starting points:
  `plan/probes/q14-*.json` (local).

## Complex

### 15. Hydraulic cylinder · `hydraulic-cylinder` · hydraulics
- **Real thing:** a double-acting tie-rod cylinder, bore 40, rod 22 (ISO 3320 sizes), mounting and ports
  after ISO 6020-2 (ports to ISO 228-1), rod-end and rear clevis, stroke 200 mm.
- **Shows:** several bodies (barrel, caps, tie rods and nuts, piston, rod, clevises); the rod's extension as a
  parameter that moves the rod; tapped ports; a section in the preview showing piston, seals and glands;
  the oil volumes as outputs.
- **Look:** gentian-blue paint, chrome rod, zinc-plated tie rods.
- **Parameters:** stroke, extension (0 to 100 %).
- **Proves:** the two chambers' volumes in closed form; pin-to-pin lengths retracted and extended.

### 16. Spiral staircase · `spiral-staircase` · architecture, steel construction
- **Real thing:** a steel spiral staircase, floor to floor 2800 mm, Ø 1600 mm, 14 oak treads on a Ø 114.3 mm
  central column (EN 10220 tube), balusters, a handrail along a helix, a landing.
- **Shows:** `datum.helix`; treads placed by a pattern that turns and rises; the handrail by sweep along the
  helix; formulas for rise and going; the stair rule (2 risers + 1 going ≈ 630 mm, DIN 18065) as an
  assertion.
- **Look:** anthracite steel and oak treads.
- **Parameters:** floor-to-floor height, diameter.
- **Proves:** the stair rule at the walking line, headroom ≥ 2000 mm, the number of risers.

### 17. Ship propeller · `ship-propeller` · marine
- **Real thing:** a four-blade fixed-pitch propeller, Ø 600 mm, Wageningen B4-55 outline and thickness
  (published series data), pitch ratio 0.8, 15° rake, a hub with a 1:12 taper bore and keyway, nickel-aluminium
  bronze.
- **Shows:** blade sections from formulas (`sketch.curve`) and a table; a loft through them;
  `feature.pattern` of the blades; root fillets; `measure.symmetry`.
- **Look:** polished bronze.
- **Parameters:** diameter, pitch ratio.
- **Proves:** expanded area ratio within 2 % of 0.55; four blades; the bronze mass in a range.
- **Risks:** sections on cylinders, root fillets on freeform blades: feasibility probe first.
- **Probe (2026-11-06):** works as six planar sections (`sketch.curve` on `yz` with `offset` r, turned by the
  pitch angle) lofted, `feature.pattern` × 4, joined to a hub of about 0.2 R that contains the root section
  wholly; set `document.setTolerance` linear 0.001 mm (F-010: 40 s at 1e-6, 11.6 s at 1e-3); root fillets
  only up to about 1 mm (F-008); sections cannot lie on cylinders (F-007): say "expanded sections placed
  tangent to the cylinder". Still over the load budget: fewer, simpler sections. Starting point:
  `plan/probes/q17-propeller-tol.json` (local).

### 18. Electric guitar body · `guitar-body` · lutherie, CNC
- **Real thing:** an original double-cutaway solid body, 45 mm thick, carved top, bolt-on neck pocket,
  two humbucker routes, a rear control cavity with its cover recess, a bridge placed by a 648 mm scale.
- **Shows:** a freeform outline of splines; the carved top as a surface (`feature.surface.network` or
  `feature.fill`) cut into the body; pockets by cuts; formulas from the scale length; `measure.continuity`
  on the top.
- **Look:** candy-apple red car paint with clear coat.
- **Parameters:** scale length, body thickness.
- **Proves:** bridge position from the scale; pocket depths; inside corners ≥ the router's radius.
- **Risks:** the carved top cut by pockets: feasibility probe first.
- **Probe (2026-11-06):** works, 1.3 s: a periodic `sketch.spline` outline (17 points) extruded 45 mm; the
  top a 5 × 5 `feature.surface.network`, applied with `feature.boolean` `op: intersect`; pockets as
  rounded rectangles (`sketch.path`, r 6.35) on datum planes at their floor heights, extruded with `cut`.
  A crown of 10 mm hardly shows in an iso view: plan a lower camera. Starting point:
  `plan/probes/q18-guitar.json` (local).

### 19. RC yacht hull · `rc-yacht-hull` · naval design
- **Real thing:** a radio-sailing yacht to the International One Metre class rules (hull length ≤ 1000 mm,
  draft ≤ 420 mm, total mass ≥ 4000 g): a lofted hull, a fin of a symmetric NACA section, a lead bulb, a
  rudder.
- **Shows:** a hull lofted through stations from a table of offsets; the fin's section from a formula;
  `measure.levelFor` (waterline for the mass), `measure.floating`, `measure.below`; the hull shelled.
- **Look:** white gelcoat hull, carbon fin, dark lead bulb.
- **Parameters:** bulb mass, fin depth.
- **Proves:** the class limits; the waterline for 4 kg; the bulb mass from lead's density; upright stability.
- **Probe (2026-11-06):** works: a table of offsets, one `sketch.spline` per station, `feature.loft`;
  a `feature.transform` copy (`keep`) of the closed hull is the envelope that `measure.levelFor`,
  `measure.floating` and `measure.below` need (a shelled body counts only its material); shell 1.5 mm with
  the deck open; NACA 0009 fin as two `sketch.curve` halves; bulb revolved; levelFor and floating take well
  under a second. Give the bow a section of at least 30 × 20 mm (F-009). Loads in 10.5 s at tolerance
  0.001 mm: over budget, simplify. Starting point: `plan/probes/q19-yacht-b.json` (local).

### 20. Moka pot · `moka-pot` · product design, casting
- **Real thing:** an original three-cup stovetop espresso maker in cast aluminium: boiler with safety valve,
  funnel basket, filter plate, gasket, collector with spout and hinged lid, a heat-proof handle.
- **Shows:** revolves and lofts, `feature.shell`, a threaded joint, a perforated filter by pattern, a
  swept handle with fillets, several bodies, the capacities as outputs.
- **Look:** brushed aluminium and black handle.
- **Parameters:** cups (choice), handle angle.
- **Proves:** boiler capacity below the valve for the cups; drafts on the castings; parts not overlapping.
- **Risks:** load budget (many bodies): keep features few and large.
- **Probe (2026-11-06):** the boiler and collector revolve and shell (shell before thread); a modelled
  M68 × 2 thread works but costs about 3 s per threaded body, and a mating pair touches on its flanks and
  cannot be shown clear (F-014). Model the boiler's external thread, keep the collector's internal thread
  cosmetic, and prove "no overlap" for the other pairs only. Starting point: `plan/probes/q20-*.json`
  (local).

### 21. Mont Ventoux relief · `ventoux-relief` · topography, art
- **Real thing:** a relief of Mont Ventoux (1910 m) with the final climb of the 2026 Tour de France Femmes'
  stage 7 (7 August 2026: the Bédoin side, 15.7 km at 8.8 %, the side the men's 2025 stage 16 also took),
  vertical exaggeration stated, the summit's observatory tower; as a 3D-printable relief and as
  laser-cut contour layers.
- **Shows:** the one example with Python (`make.py`): it reads public elevation data (SRTM, public domain, or
  Copernicus DEM with its attribution) and fits a B-spline terrain; 3DCraft does the rest: the terrain
  surface, the solid, the route on it, contour sections (`measure.section`) and a DXF per layer.
- **Look:** marble relief on a walnut base.
- **Parameters:** vertical exaggeration, contour interval.
- **Proves:** summit height and the climb's height gain within the data's accuracy; layer count.
- **Risks:** route data licence (OpenStreetMap is ODbL: attribution as a produced work); "a surface through
  a grid of points" may be a missing capability (log it).
- **Probe (2026-11-06):** works and is light: one `sketch.spline` per grid row through plain numbers (F-011:
  expressions are refused there, so `make.py` writes numbers and the vertical exaggeration is applied in
  `make.py`, or by a scale of the solid if 3DCraft has one), `feature.loft` of the rows into a sheet,
  `feature.boolean` subtract from a block; 60 × 40 grid opens in 1.1 s. Contours: `measure.section` at a
  level; DXF per level from a copy intersected with a block above it, `file.export` with `faces` (one layer
  per face). Data: the Tilezen/Mapzen skadi tile
  `https://s3.amazonaws.com/elevation-tiles-prod/skadi/N44/N44E005.hgt.gz` (int16 hgt, gzip + struct in
  the standard library; attribution per github.com/tilezen/joerd docs/attribution.md), or Copernicus DEM
  GLO-30 (float COG, harder to decode). Route: OpenStreetMap (ODbL, "© OpenStreetMap contributors", a
  produced work) or IGN BD TOPO (Licence Ouverte 2.0). Starting points: `plan/probes/q21-*.json` (local).

## Palette

| # | Example | Line |
|---|---|---|
| 1 | Socket head cap screw | black oxide |
| 2 | T-slot profile | clear anodised aluminium |
| 3 | Wall clock | birch and black |
| 4 | Turned bowl | walnut |
| 5 | Hex key stand | orange PLA |
| 6 | Steel bookend | teal powder coat |
| 7 | V-block pair | ground steel and black |
| 8 | Square-to-round transition | galvanised |
| 9 | Mailer box | kraft |
| 10 | Headphone stand | sunflower yellow |
| 11 | Splayed stool | oak |
| 12 | FPV drone frame | carbon and purple |
| 13 | Cast handwheel | machine green and bright steel |
| 14 | Solitaire ring | yellow gold and clear stone |
| 15 | Hydraulic cylinder | gentian blue and chrome |
| 16 | Spiral staircase | anthracite and oak |
| 17 | Ship propeller | bronze |
| 18 | Guitar body | candy-apple red |
| 19 | RC yacht hull | white, carbon and lead |
| 20 | Moka pot | aluminium and black |
| 21 | Mont Ventoux relief | marble and walnut |

## Coverage

Across the 21, every modelling command in scope is used at least once (`tools/examples.py coverage`). Where
a family is carried: sketches and constraints (1–21), solids from primitives and extrusions (1, 2, 7, 12),
revolve (1, 4, 14, 15, 20), loft (17, 19, 20), sweep (13, 14, 16, 20), developable and plate (8), unfold (8),
fold (9), sheet metal (6), surfaces (18, 21), fillet and chamfer (most), shell (4, 19, 20), draft (13),
thread (1, 7, 15), pattern and mirror (3, 7, 11, 12, 14, 16, 17), booleans (most), text (3, 5), curves from
formulas (17, 19), tables (1, 5, 19), conditional features (3), named sets (7), datums (11, 16), cut list
(11), section and hydrostatic measures (2, 19, 21), clearance, thickness and draft checks (5, 7, 10, 12, 13),
exports to STEP, 3MF, DXF and SVG (1, 3, 5, 6, 8, 9, 12, 21).
