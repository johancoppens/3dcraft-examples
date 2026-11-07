# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design an original flat-pack bookcase to be CNC-routed from one 2500 × 1250 mm sheet of 18 mm
   birch plywood and assembled without screws, glue or tools: the shelves and two back rails pass through
   the sides in tusk tenons locked by tapered wedges. Make four public parameters: the width over the
   sides (750 mm, from 600 mm in 10 mm steps up to the widest whose shelves still meet the sag limit of turn
   6 on the measured sheet), the number of shelves (4, from 3 to 5, top and bottom
   included), the measured sheet thickness (17.6 mm, from 17.1 to 18.7 in 0.05 mm steps, EN 315's limits
   for 18 mm) and the router cutter's diameter (6.35 mm, a ¼ in compression spiral, from 5 to 8 mm in 0.05
   mm steps). Every part is exactly the measured thickness, and every mortise is that thickness or the
   tenon's width plus a 0.4 mm fit clearance. Every inside corner gets a relief of the cutter's radius plus
   0.1 mm.

2. The two sides are 1100 mm high and 300 mm deep, each one sketch with its mortises as holes. The bottom
   edge has a foot 60 mm long at the front and at the back with a 40 mm high arch between them, its two
   inner corners rounded 20 mm, the feet's four corners 5 mm; the top corners are rounded 30 mm. The
   shelves (280 mm deep, flush with the front) are evenly spaced from the bottom one, its underside 90 mm
   above the floor, to the top one, its top face 40 mm below the top of the sides. Each shelf end has two
   tenons 70 mm wide, 35 mm in from its front and back edges; the shelves rest on the floors of their
   mortises. Put a dogbone relief (a half circle through the corner, on the diagonal) in the four corners of
   every mortise in the sides. Make the right side a mirror of the left.

3. Each shelf is one sketch: its tenons go through the side and stand 50 mm proud of it, with 6 mm rounded
   corners at their ends and a T-bone relief (a half circle cut into the tenon, centred on its edge at the
   shoulder) at both sides of each tenon's root. In each tenon cut a wedge mortise, the sheet plus the
   clearance wide, centred on the tenon, from 2 mm inside the side's outer face to 22 mm outside it, with
   dogbones at its near end and, at its far end, where the wedge bears, T-bones along the long walls so
   that the far wall stays straight across its whole width. Make every shelf a separate body, not a
   pattern, so the cut list sees each one.

4. Add two back rails, boards 110 mm high standing on edge between the sides, one right under the top shelf
   and one standing on the bottom shelf, with their back face placed so that their wedges end 5 mm short of
   the sides' back edges. Each end has one tenon 60 mm high, centred, with the shelves' projection, T-bones,
   rounded ends and wedge mortise; cut their mortises into the sides, a slot the sheet plus the clearance
   wide and the tenon plus the clearance high with the tenon resting on its floor, with dogbones. Their
   wedges go in horizontally, from the front.

5. The wedges are cut from the same sheet: a straight edge that bears on the side's face and a slope of 1 in
   8 that bears on the far end of the wedge mortise, 22 mm wide where it enters the tenon, standing 26 mm
   proud of the tenon and 22 mm past it, with 5 mm round corners at the tip and 6 mm at the head. Put one,
   driven home, in every tenon, each a body of its own. Make everything oiled birch plywood, 680 kg/m³,
   with the ply edges showing.

6. Add checks: each part's volume in closed form; every mortise the sheet plus the clearance; the number of
   reliefs and that they are at least the cutter's radius; each wedge touching the side and the far end of
   its mortise and 2 mm from the near end; no two parts overlapping; the shelf's sag under 30 lb of books
   per running foot, simply supported across the clear span with birch plywood's bending modulus of
   10 048 N/mm², within span/600 (the Sagulator's target); and that all parts fit on the one sheet, laid with
   the grain along it. Give me the cut list and a DXF of all parts on the sheet for the router, run a check
   of the whole document, and show me a picture from the front left.

## Acceptance

At the defaults the result must have:

- 28 bodies, each a plate 17.6 mm thick: a cut list of 2 sides of 1100 × 300 mm, 4 shelves of
  850 × 280 mm, 2 back rails of 850 × 110 mm and 20 wedges 65.6 mm long;
- a total plywood volume of 29 681 383 mm³ within 1 % (20.18 kg);
- mortises 18.0 mm wide, 200 relief arcs of 3.275 mm radius;
- no overlap between any two parts (54 pairs touching);
- a shelf sag of 1.164 mm against a limit of 1.191 mm (clear span 714.8 mm), and a widest width of 730 mm
  on a 17.1 mm sheet;
- every check passing, and the same at 3 and at 5 shelves and at widths of 600 and 750 mm.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above: passed.
Its bookcase has the same parts as this example, to the cubic millimetre (side 5 456 124.1, shelf
3 818 560.3, rail 1 508 070.5 and wedge 23 937.6 mm³), the same 20.18 kg, 200 reliefs of 3.275 mm, mortises of
18.0 mm, every wedge on its side and far wall and 2 mm off the near one, no overlaps, and the shelf sag of
1.164 mm against 1.191 mm; it also builds at three and five shelves, both sheet limits, both cutters and both
ends of the width. It made the width's maximum a formula of the sheet, as here. It found that
`cut.export`'s row layout overflows the sheet's 1250 mm at five shelves
([F-162](../../3DCRAFT-FEEDBACK.md#f-162)) and proved a column nest by formulas instead. About 411 steps,
written by a script.
