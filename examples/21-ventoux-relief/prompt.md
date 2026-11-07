# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands. The data is
in this example's `data/` folder; give the AI access to it.

## The conversation

1. Let's make a relief of Mont Ventoux at 1:70 000 from the elevation grid in `data/elevation.csv`: 37 ×
   29 heights in metres, nodes 350 m apart, one line per column from west to east, each line's values from
   south to north (the header gives the grid's origin in Lambert-93). Put the map's south-west node at the
   origin, so the relief is 180 × 140 mm, and make the heights start at sea level: the underside of the
   relief is sea level. The vertical exaggeration is a parameter, 1 to 3 in steps of 0.1, default 2.1. Draw
   one spline through each column's heights, with the heights written as formulas of the exaggeration so
   that changing it reshapes the terrain, close each column down to sea level, and loft the 37 columns
   into one solid. Keep that terrain as the source and hide it.

2. Mark the climb from Bédoin of the Tour de France Femmes 2026 (stage 7) on it. `data/kilometres.csv`
   gives the climb's kilometres km 0 to km 15 along IGN's road, in Lambert-93 with their altitudes. Put a
   Ø 1.5 mm brass pin at km 1 to km 15 and a Ø 2.5 mm one at km 0, the start (544.4 m). Each pin stands
   in a blind hole 0.1 mm wider all round whose floor is 3 mm above the relief's underside, and reaches
   2 mm above the ground under it.

3. Print the relief in two colours, as the mountain looks: Bambu Lab PLA Matte Dark Green (#656A4D) up to
   the forest's edge at Chalet Reynard, 1419.1 m (the header of `data/kilometres.csv`), and Bone White
   (#D4D1C3) above it, the bald summit. Split the relief at that height into two bodies, keep the forest's
   edge as a named variable, and draw both matte and not metallic. Chamfer the relief's bottom edge 1 mm
   for the first printed layer.

4. Put the summit tower from `data/tower.csv` on top as a symbol at ten times the map's scale: a cylinder
   whose circle has the tower's footprint area (162.3 m²), 44.8 m tall standing on its ground at 1893.5 m,
   with a Ø 0.6 mm mast up to the antenna's top at 1975.5 m, in five bands. Fit its foot to the terrain,
   paint it white and every other band of the mast red, starting at the bottom. Set it all on a walnut
   base with a 15 mm border, 22 mm thick, its top at sea level: corners rounded 8 mm, the top edge rounded
   over 3 mm, the bottom edge chamfered 1 mm.

5. Add a second product as a choice: a stack of laser-cut contour layers instead of the printed relief and
   its pins, one 3 mm sheet per contour interval, so that in this product the sheet sets the vertical
   scale. The interval is a parameter, 100 to 200 m in steps of 50 m, default 100 m, counted from sea
   level. Cut the terrain into one body per layer: the first from sea level up to one interval above the
   highest multiple of the interval below the lowest ground (338 m), then one slab per interval up to the
   one that holds the summit, white and pale grey acrylic in turn.

6. Add checks: the terrain's volume against the map's area times the data's mean height (1026.9 m, the
   trapezoidal rule over the grid) times the vertical scale, within 0.1 %; the terrain at the summit node
   at 1910 m within 2 m; the terrain at the climb's start at 544.4 m within SRTM's 16 m; sixteen pins
   and a hole for every pin; and in the layered product one body per layer. Give the document a title and
   description, check the whole document, and show me a picture from the south-west, low.

## Acceptance

At the defaults (exaggeration 2.1, interval 100 m, printed relief) the result must have:

- a relief 180 × 140 mm whose underside is sea level and whose summit stands 57.3 mm high
  (1910 m × 2.1 / 70 000), with a terrain volume of 776 586 mm³ within 1 %;
- two relief bodies meeting at 42.57 mm (1419.1 m), dark green below and bone white above;
- sixteen brass pins (fifteen Ø 1.5 mm and one Ø 2.5 mm) in sixteen blind holes, Ø 1.7 and Ø 2.7 mm, from
  3 mm up, each pin 2 mm above the ground, km 0 at (49.3, 8.8) mm and km 15 at (96.5, 106.1) mm; the
  ground at km 0 between 15.85 and 16.81 mm high;
- the tower Ø 2.05 mm with its roof 6.4 mm and its mast's top 11.7 mm above its ground at 56.8 mm;
- a walnut base 210 × 170 × 22 mm;
- in the layered product, 17 layer bodies, the first 12 mm thick (four sheets) and the others 3 mm;
- every check passing, and the same at exaggeration 1 and 3 and at an interval of 200 m.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above and the
three data files: passed. Its terrain has the same volume (776 585.5 mm³, +0.032 % on the data's mean
height), summit (1910 m) and start (about 540 m against IGN's 544.4 m) as this example; its 16 pins stand
exactly 2.000 mm above the ground at exaggerations 1, 2.1 and 3, the relief splits into forest and bald
summit, and its laser product has 17, 11 and 9 layers at 100, 150 and 200 m with the exaggeration set by the
3 mm sheet. It measured the ground under each pin with `measure.ray` in a script, since a pin's height above
the ground cannot be a formula, and found that a body can go into only one later feature (it copied the
terrain with `keep`). About 594 steps, written by a Python script from the data files.

