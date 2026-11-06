# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a 30 × 30 mm B-type aluminium profile with an 8 mm T-slot in each face, as a parametric part
   lying along the x axis. Make every size a variable: the 30 mm width, the slot opening of 8.2 mm, the slot
   depth of 9 mm from the face to the slot floor, one 2 mm wall thickness for the lips and the diagonal
   ribs, an undercut 16.5 mm wide under the lips, a 1.3 mm minimum wall, a 6.8 mm core bore, a 1.5 mm radius
   on the outer corners and 0.5 mm on the lips at the slot mouth. Publish the length (300 mm, from 100 to
   3000 mm) and the depth of the tapped thread at the ends (20 mm, from 12 to 30 mm) as parameters.

2. Draw the cross section with symmetry: draw one face only, from the middle of one rounded corner to the
   middle of the next, with the slot mouth, the undercut, and below it 45° flanks down to a flat slot floor.
   Make the floor as wide as it can be while the diagonal rib between two neighbouring slots keeps the 2 mm
   wall. Hold every point with the variables, then repeat that run four times round the centre so it closes
   into the outline. Add the core bore, and a round chamber in each corner block that leaves a 1.3 mm wall
   to the undercut and to the outside.

3. Extrude it to the length, and round every corner inside the slots, the lip tips included, with 0.3 mm, as
   the extrusion die makes them, along the whole length. Tap the core M8 at both ends to the thread depth,
   as cosmetic threads, and countersink both entries at 90° to the thread's major diameter.

4. Make it clear anodised 6063: aluminium for its density, a cool light grey, satin rather than polished.
   Add outputs for the area and the second moment of area of the section half way along, and the mass per
   metre in kg/m from the area and the density.

5. Add checks: the section's area and its second moment of area worked out in closed form from the pieces
   (square, roundings including the die corners, bore, chambers and slot cavities; use the fourfold
   symmetry, Ix = J/2), the area and the second moment within 3 % of Misumi's HFS6-3030 (332 mm², 28 300
   mm⁴), and at least 1.3 mm of core left between the M8 thread and the slot floor. Give the document a
   title and description, run a check of the whole document, and show me a picture from three-quarters
   above, with the end of the profile towards me.

## Acceptance

At the defaults (300 mm long, thread depth 20 mm) the result must have:

- one body, section area 333.4 mm² within 1 %, Ix = Iy = 28 675 mm⁴ within 1 %, both within 3 % of
  Misumi HFS6-3030 (332 mm², 28 300 mm⁴);
- mass per metre 0.900 kg/m within 1 % (0.270 kg for the 300 mm piece);
- four slots 8.2 mm wide and 9 mm deep, their inner corners rounded 0.3 mm; a Ø 6.8 mm core bore with
  cosmetic M8 threads 20 mm deep at both ends and a 90° countersink to Ø 8 mm at each entry; four corner
  chambers;
- a sketch with no degrees of freedom left, its outline made from one face's run repeated four times;
- Length and Thread depth as public parameters with the ranges above;
- every check passing, and the same at 100 mm and at 3000 mm long.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the five turns above:
passed. Its profile checks itself with 5 assertions and has a section of 333.3533 mm² and Ix = 28 674.86 mm⁴,
the same as this example's to about 13 digits, and 0.900 kg/m; it derived the closed forms itself. It held
the mirrored points of the run by expressions, not by the sketch's `symmetric` constraint.

