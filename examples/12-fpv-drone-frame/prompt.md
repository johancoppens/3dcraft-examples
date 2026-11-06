# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design a 5-inch true-X freestyle FPV quadcopter frame, CNC routed from carbon fibre sheet, in
   millimetres with x forward, y to the left and z up, the flight controller's centre on the origin. Two
   parameters: the prop diameter, 5.1 in (5 to 5.3 in, in steps of 0.1 in), and the thickness of the sheet
   the arms are cut from, 5 mm (4 to 6 mm, in steps of 1 mm). The four motors sit on the diagonals at 45°,
   so far out that neighbouring prop tips are 30 mm apart: the wheelbase is √2 × (prop diameter + 30 mm).
   Plates and camera plates are 2 mm sheet; holes for M3 are 3.2 mm and for M2 2.2 mm.

2. The bottom plate lies on z = 0: a rectangle from 56 mm behind to 62 mm in front of the centre, 40 mm
   wide, corners rounded 6 mm. It has the flight controller's four M3 holes on a 30.5 mm square, four M3
   standoff holes at x ±34, y ±14, four more M3 holes at x ±25, y ±9 for a third bolt through each arm,
   and two slots for the camera plates' bottom tabs (below).

3. On it lie four separate arms, one in each quadrant, their roots 1 mm apart along the centre lines. Draw
   the front-left one, then mirror it for the other three. It is a bar 13 mm wide along the diagonal that
   ends in a motor pad of Ø 30 mm centred on the motor, blended into the pad with 6 mm fillets. Its root
   fills the quadrant: from the centre lines out to x = 39.5 mm in front, round a 5.5 mm boss about the
   standoff hole, which runs into the bar's lower edge with a 10 mm fillet; the root's three convex corners
   are rounded 2 mm (the one at the centre, the front one and the one where the bar's upper edge meets the
   centre line). Holes: the stack hole, the standoff hole and the third bolt's hole at x 25, y 9 (all M3,
   through the bottom plate too), a 7 mm centre hole under the motor, and four M3 slots at 45° to the arm that reach from the 16 mm to the
   19 mm motor bolt circle.

4. Stand 25 mm aluminium standoffs, Ø 5 mm with a 2.5 mm bore for the M3 thread, on the four arm roots at
   the standoff holes, and put the 2 mm top plate on them: a rectangle 116 × 36 mm about the centre,
   corners rounded 10 mm, with the four standoff holes, two 21 × 3 mm slots for a battery strap along x at
   y ±13, two windows 8 mm along x by 16 mm along y at x ±24 with round ends, and the slots for the camera
   plates' top tabs.

5. The camera cage: two 2 mm carbon plates, standing on the bottom plate under the top plate, their inner
   faces 19 mm apart for a micro camera. Each runs from x = 41 to 58 mm, its corners rounded 2 mm, with a
   7 mm tab from x = 46 mm going 2 mm down into the bottom plate and one going 2 mm up into the top plate,
   flush with their outer faces. Give each tab root a relief notch of radius 1.2 mm cut into the plate's
   edge, so the plate seats on the slot's sharp edge. The slots in the plates are 2.2 mm wide with round
   ends as long as the tab plus their width. An M2 hole at x = 46 mm, halfway between the plates, is the
   camera's pivot.

6. Break every edge of every carbon part 0.3 mm, outline and holes, top and bottom, and the standoffs'
   ends. Then add stand-ins that are not part of the frame and carry no mass: a 19 × 19 × 13 mm camera
   with corners rounded 2 mm and a Ø 12 × 7 mm lens, held between the cage plates and tilted up 25° about
   the pivot; and generic 2306 motors on the pads (a Ø 25 × 3 mm base, a Ø 28 mm bell up to 19 mm above
   the arm with its top edge chamfered 1.5 mm, and a Ø 5 mm shaft 12 mm above the bell).

7. Now real props, 5.1 × 4.3 × 3 like HQProp's: 4.3 in pitch (the diameter is the prop parameter), a
   polycarbonate hub Ø 13 × 6.8 mm with a 5 mm bore on each motor, three blades, and an M5 nyloc nut on
   top (DIN 985: 8 mm across flats, 5 mm thick). Loft one blade through six sections square to its
   radius: at 5 mm and 14 mm from the shaft, chords 8.5 and 9 mm, thicknesses 3 and 2.5 mm; then at 0.45,
   0.75, 0.95 and 1.0 of the prop's radius, chords 0.245, 0.225, 0.15 and 0.05 of the radius, thickness
   ratios 0.13, 0.095, 0.10 and 0.15. Every section is the same flat-bottomed airfoil, a smooth closed curve
   through eight points (u along the chord from the leading edge, v across the thickness from the bottom,
   both as fractions): (1, 0.12) at the trailing edge, (0.7, 0.5), (0.3, 1), (0.06, 0.7), (0, 0.3) at the
   leading edge, (0.08, 0), (0.45, 0) and (0.85, 0). Stack the sections on a line through mid-chord and
   0.3 of the thickness, at the hub's mid-height, and turn each to the pitch angle atan(pitch / (2π r)) with
   the leading edge raised, but at most 38° (the root's washout, so it fits the hub). Pattern the blade
   three times round the hub and join blades and hub into one prop, then mirror the prop for the others so that they turn props-out: front-left
   and rear-right counter-clockwise seen from above, the leading edges facing the rotation. Give each prop
   a hidden swept cylinder, its diameter and 14 mm high about the hub's mid-height, for checking.

8. Make the carbon parts carbon fibre at 1.6 g/cm³ with the weave lying flat in each plate, the standoffs
   purple anodised aluminium at 2.7 g/cm³, the props translucent purple polycarbonate at 1.2 g/cm³, the
   motors, nuts and camera dark. Add outputs for the wheelbase and the masses of the frame (carbon parts
   and standoffs) and of the props, and checks: the swept cylinders clear every frame part and the camera
   by at least 3 mm; the blades stay inside them and reach the full diameter; the blade's angle at 75 % of
   the radius is the pitch's; the blade root, where it leaves the hub, stays below polycarbonate's 65 MPa
   yield under the centrifugal pull at 44 100 rpm (a 1750 KV motor on a full 6S battery, unloaded); a Ø 2 mm router bit reaches every inside corner and slot of each carbon part (prove it, for
   instance by growing the outline by the bit's radius and comparing its area with Steiner's formula); the
   flight controller holes are 30.5 mm apart; the motor slots reach both bolt circles; the camera touches
   both cage plates; no two parts overlap. Export each carbon part's outline as DXF, run a check of the
   whole document, also at the corners of the range, and show me a picture from the front left, above.

## Acceptance

At the defaults (5.1-inch props, 5 mm arms) the result must have:

- four identical arms of 5 mm sheet (two turned over), a bottom plate, a top plate and two identical
  camera plates of 2 mm sheet, and four standoffs 25 mm long;
- a wheelbase of 225.6 mm, and the motor centre holes of opposite arms 218.6 mm apart wall to wall;
- the stack holes on a 30.5 mm square, three M3 bolt holes in each arm's root, the motor slots' inner
  walls 12.8 mm apart across the pad and their outer arcs centred on the 19 mm circle;
- a frame mass of 104.7 g within 2 % (carbon at 1.6 g/cm³, aluminium at 2.7 g/cm³);
- a least clearance of 3.72 mm between the props' swept cylinders and the frame, at the top plate's
  corners (3.31 mm at 5-inch props, 4.54 mm at 5.3-inch);
- every inside corner and slot of the carbon parts reachable by the Ø 2 mm bit, proven, and the cut
  outlines in DXF;
- the camera touching both cage plates, and no overlaps;
- four three-blade props of 129.54 mm, each one piece with its Ø 13 × 6.8 mm hub and 5 mm bore, under an
  M5 nut, 4.13 g each within 5 %, roots 9 mm wide and 2.5 to 3 mm thick at 38°,
  blades at 19.7° at 75 % of the radius, turning props-out;
- a root stress of 48 MPa within 5 % at 44 100 rpm, below 65 MPa;
- every check passing, and the same at 5 and 5.3 inch with 4 and 6 mm arms.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the eight turns above:
passed. Its quad checks itself with 32 assertions over its range and has the same wheelbase (225.62 mm),
frame mass (104.71 g), props (4.13 g each), prop clearance (3.717 mm) and root stress (47.8 MPa) as this
example; its router checks are exact. It read the camera plate's relief notch and the camera's pivot a little
differently: its first notch had a mouth narrower than the bit, which the Steiner check caught.

