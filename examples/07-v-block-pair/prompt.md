# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a matched pair of hardened, ground 90° V-blocks with U-clamps, the common size for shafts
   of 6 to 30 mm (like Haas 09-0550). Make two parameters: the diameter of a test pin that rests in the
   blocks (20 mm, from 6 to 30 in steps of 1) and the length of each block along its V (45 mm, from 40 to
   100 in steps of 5). Run the Vs along x, z up. A block is 40 mm wide and 35 mm high: a 90° V 25 mm wide on
   top and a 90° V 15 mm wide underneath, each with a relief groove 3 mm wide at its apex whose round bottom
   is 1.5 mm past the apex; on both sides a slot 10 mm high and 3 mm deep, centred on the height, with
   0.5 mm radii in its inside corners. Chamfer the outer corners, the slot mouths and the V mouths 0.5 mm in
   the profile, extrude it, and chamfer every edge of both end faces 0.5 mm too.

2. In the middle of each end face, midway in height between the two V apexes, put an M6 tapped hole: a
   5 mm tap drill 14 mm deep with a 118° point and a 90° countersink to 6.4 mm, threaded 10 mm (a
   cosmetic thread is fine). Then make it a pair: a second, identical block on the same axis with 40 mm
   between them, the pair centred on the origin.

3. Give each block a U-clamp at its middle, cut from 14 mm plate: legs 5 mm thick, 0.5 mm clear of the
   block's sides, ending in hooks 6 mm high that reach into the side slots to 0.5 mm from their bottom and
   bear up against the slot's upper face; a 10 mm crossbar whose underside is 3 mm above the top of a 30 mm
   pin resting in the large V; 3 mm inside and 8 mm outside radii at its corners, 0.5 mm where the hooks meet
   the legs; all edges of its two flat faces chamfered 0.5 mm; and a 6.8 mm hole tapped M8 through the
   middle of the crossbar.

4. Each clamp gets an M8 screw, 50 mm from its flat tip to its head, the tip chamfered 1 mm, a 14 mm round
   head 12 mm high (chamfered 0.5 mm underneath, 1 mm on top) with a 5 mm cross hole for a tommy bar,
   its full thread stopping 3.2 mm under the head (the ISO 3508 run-out). Lay a
   ground test pin of the pin diameter in the large Vs of both blocks so it touches both flanks of each:
   its axis is r√2 above the V's apex. It is as long as both blocks and the gap plus 15 mm at each end, its
   ends chamfered 0.5 mm. Screw each screw down until its tip bears on the pin.

5. Make the blocks bright ground steel, the clamps and screws black oxide, the pin polished steel. Keep the
   tapped holes as a named set. Report the mass of the two blocks in kg and the height over the pin.

6. Add checks: the area of a cut through the middle of a block, worked out by hand; the pin's centre r√2
   above the apex; the pin touching each top flank of each block; the blocks, clamps and pin not
   overlapping, nor the screws the pin or the blocks; the screws bearing on the pin and the clamp hooks on
   the slots; the pin at least 3 mm clear of the clamps; the screw heads at least 1 mm above the crossbars;
   six tapped holes; and at least 2 mm of wall round each end hole (from every face of the hole, its
   countersink included, to every other face of the block but its end faces). Give it a
   title and description, export the end, side and top views as SVG drawings with hidden lines dashed, check
   the whole document and show me a picture from the front right, above, looking at an end of the blocks.

## Acceptance

At the defaults (Ø 20 mm pin, 45 mm blocks) the result must have:

- two blocks of 45 × 40 × 35 mm whose section at the middle is 1114.79 mm² (within 0.1 %) and which weigh
  0.778 kg together in steel (within 1 %);
- the pin's axis 36.642 mm above the base (46.642 mm over the pin), touching all four top flanks
  (distance below 0.001 mm) and overlapping nothing;
- six tapped holes (four M6 in the block ends, two M8 in the clamps), two clamps and two screws, the
  screws touching the pin;
- every check passing, and the same with a 6 mm pin, a 30 mm pin and 100 mm blocks;
- three SVG drawings.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its pair checks itself with 21 assertions, also at pins of 6, 25 and 30 mm and lengths of 40, 70 and
100 mm, and has the same section (1114.7925 mm²), pin centre (36.642 mm) and mass (0.7778 kg) as this
example; the pin touches all four flanks and the screws and hooks bear. Like this example it threaded the
crossbar 9 mm (F-056) and threaded the mirrored block's holes again (F-052).

