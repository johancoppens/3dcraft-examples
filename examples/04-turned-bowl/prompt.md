# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a turned walnut serving bowl as a parametric part: 220 mm across and 85 mm high overall,
   with an even 7 mm wall. Make the diameter, the height and the wall thickness public parameters
   (160 to 300 mm in 5 mm steps, 55 to 120 mm in 5 mm steps, 5 to 10 mm in 0.5 mm steps). Set the
   document's tolerance to 0.001 mm: that is plenty for wood. Work out the blank too: add a 6 mm turning
   allowance on every face and round the diameter and the thickness up to whole inches, as walnut blanks
   are sold, and show the blank's diameter and thickness in inches as outputs.

2. Draw the half section and revolve it about the vertical axis in one go. The bowl stands on a foot ring
   6 mm high, 0.36 of the diameter across, but never less than the chuck recess plus 8 mm of ring on each
   side. The recess inside it is a fixed size for 50 mm dovetail jaws: Ø 56 mm at the mouth, the full
   6 mm deep, its wall leaning out 10° so it is wider at the floor, with sharp corners. The flat of the
   base reaches 0.04 of the diameter beyond the foot ring on each side. The outside rises from the edge
   of the base in one cubic spline to the rim, flaring out 12° at the top. Place its two inner control
   points like this, the spline ending where the wall meets the rim's bead: the lower one level with the
   base (so the curve leaves it tangent), 0.55 of the way out from the base's edge to the wall's end; the
   upper one 0.55 of the wall's rise (base to wall's end) below the wall's end, on the 12° line of the
   flare (so the curve arrives along it). The rim is fully rounded: a half circle as wide as the wall,
   tangent to both faces. The inside must be the exact offset of the outside, the wall thickness square to
   it everywhere, flat across the bottom.

3. Round the outer bottom edge of the foot ring with 2 mm and cove the corner where it meets the base
   with 3 mm; leave the recess sharp. Make it oiled walnut: the walnut material in a cool chocolate
   brown with a thin satin sheen, its grain placed as in a face-grain blank, the pith just above the
   bowl, so the rings make an eye in the bottom and sweep up the walls, about 4.5 mm apart.

4. Add outputs: the volume of wood, the mass in grams and the brimful capacity in millilitres (everything
   inside the bowl up to the top of the rim). Then add checks: the foot ring's volume in closed form; the
   wall's volume against Steiner's formula for a parallel wall, from the measured areas of the outer and
   inner wall; the capacity between the cone from the inside of the base to the inside of the rim and the
   cylinder over the inside depth; and that the bowl's measured diameter and height are as drawn.

5. Give the document a title and description, run a check of the whole document, export the half section
   as an SVG I can cut a profile template from, and show me a picture from three-quarters above.

## Acceptance

At the defaults the result must have:

- one body, 453 735 mm³ of wood within 1 % (290 g of walnut at 640 kg/m³);
- a capacity of 1840 mL within 1 %;
- an overall size of Ø 220 × 85 mm, a foot ring Ø 79.2 mm outside, 6 mm high, round a recess Ø 56 mm at
  the mouth and Ø 58.1 mm at the floor;
- a wall 7 mm thick everywhere, the rim rounded over its full thickness;
- a blank of 10 × 4 in (254 × 101.6 mm);
- every check passing, and the same at Ø 160 × 120 mm with a 10 mm wall and at Ø 300 × 55 mm with a 5 mm
  wall.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the five turns above:
passed. Its bowl checks itself with 7 assertions at five points of the range and has 453.735 cm³ of wood,
1839.68 mL brimful and a foot ring of 14 493.1773 mm³, the same as this example's; its Steiner check agrees
to 0.03 mm³. It measured the capacity through a hidden helper body (an open vessel's capacity is not a
measure, F-047) and its grain shows nested stripes rather than a full eye.

