# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design a splayed-leg sitting stool in oak, as a parametric model in millimetres. Make two public
   parameters: the seat height (the seat's top above the floor), 450 mm by default, from 400 to 650 mm in
   steps of 10 mm, and the splay angle, 10° by default, from 5° to 12° in steps of 0.5°. Each leg leans
   out by the splay angle seen from the front and by the same angle seen from the side, so it really
   leans along the diagonal by atan(√2 · tan splay), about 14°. Start with the seat: a disc Ø 340 mm and
   30 mm thick, centred on the origin with its top at the seat height, its top edge rounded with a 6 mm
   radius and its underside edge bevelled 6 mm up the edge and 12 mm in under the seat. Its boards run
   along x.

2. Now the four legs: 38 mm square, their four long edges chamfered 3 mm, their faces facing x and y:
   tip each leg about the level line square to its diagonal, without twisting it about its own axis.
   Each leg's axis comes up through the seat's top 80 mm from both centre lines (at x and y = ±80 mm) and
   leans outward along its diagonal. Give each leg a through tenon 19 mm square, half the leg, centred on
   its axis and running along it, right through the seat in a matching mortise. The shoulder round the
   tenon must lie flat on the underside of the seat, so it is level, not square to the leg. Cut the feet
   level on the floor and the tenons flush with the seat's top, and chamfer the rim of each foot 2 mm.
   Please build one leg from its own section and repeat it round the centre.

3. Join the legs in pairs with two stretchers running along y, one on each side, 22 mm thick (along x) and
   32 mm high, their four long edges rounded 3 mm, centred on the legs' axes at 0.4 of the seat height
   (180 mm by default). Tenon them into the legs by the rule of thirds: the tenon a third of the leg thick
   (12.67 mm), 22 mm high (5 mm shoulders at the top and bottom), and two thirds of the leg deep (25.33 mm,
   measured on the stretcher's centre line from the leg's face), the tenon a straight, plumb continuation
   of the stretcher. The stretchers' shoulders must sit tight on the legs' leaning faces and their tenons
   fill the mortises in the legs.

4. Wedge the through tenons: a kerf in each tenon, filled by a walnut wedge 4 mm thick at the seat's top,
   tapering to nothing 20 mm down along the leg (two thirds of the seat), across the whole tenon and
   flush with the seat. All four wedges must lie across the seat's grain (their long side along y), so
   they spread the tenons along the grain and do not split the seat. Make the seat, legs and stretchers
   oak with an oiled look, a honey brown with little contrast in the grain, the grain along each part:
   make each diagonal pair of legs a part of its own, with its rings running straight along both legs, not
   across them. The wedges are walnut.

5. Add outputs for the stool's mass, the legs' angle from upright along the diagonal, a leg's length along
   its axis from the floor to the seat's top, the leg blank's length along its axis (from the lowest
   corner of the foot to the highest corner of the tenon), a stretcher's length over its tenons, and the
   span of the feet on the floor. Then add checks: the stool is exactly the seat height tall; the seat's
   volume, the volume of the legs with their wedges above 10 mm from the floor, and the stretchers'
   volume, each worked out by hand from the sizes and the leg angle; at least 7 mm of wood between the
   stretcher mortises' cheeks and the legs' leaning sides and arris chamfers; four wedges
   reaching the seat's top; the legs at least 5 mm clear of the seat's underside bevel; and both parts of
   the stool stability test of IS 5416 (Part 2), clause 7.5. First, with two feet against stops, 600 N
   pressed down 50 mm in from the seat's edge nearest them and 20 N pushed towards them through the seat
   at its top, the stool with its own weight must not tip over the outer edges of those feet. Second,
   tilted about those feet until the far edge of the seat has moved 100 mm (without the loads), its
   centre of mass must still lie inside them.

6. Give the document a title and a description, run a check of the whole document, export the front and
   right side views at full size as SVG with hidden lines dashed, and show me a picture of the stool from
   the front right, from a little above.

## Acceptance

At the defaults (450 mm, 10°) the result must have:

- five bodies: a seat of 2 633 379 mm³, two pairs of legs of 2 481 276 mm³ together, stretchers of
  329 925 mm³ and wedges of 3 048 mm³, each within 1 % (5 447 628 mm³ in all; 4.09 kg with oak at
  750 kg/m³ and walnut at 640 kg/m³);
- the legs leaning 14.00° from upright along the diagonals, 463.8 mm long on their axes (blanks of
  473.3 mm), through the seat with 19 mm square tenons 80 mm from both centre lines, their feet level on
  the floor and spanning 353.7 mm across them, their grain running along them;
- stretchers 267.3 mm long over their tenons, centred 180 mm above the floor, with tenons 12.67 mm thick;
- four walnut wedges across the seat's grain, flush with its top;
- about 7.6 mm of wood beside the stretcher mortises at its thinnest, at the mouth beside a chamfer;
- a moment of about 32.2 N m left against tipping in the stool test, and the centre of mass about
  107 mm inside the feet when tilted 11.9° for the 100 mm;
- every check passing, and the same at 400 mm with 5° and at 650 mm with 12°.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its stool checks itself with 9 assertions, also at 650 mm and 12°, 400 mm and 5°, and 520 mm and
7.5°, and has the same seat (2 633 378.9 mm³), legs and wedges (2 426 663.0 mm³), stretchers (329 924.9 mm³),
least mortise wall (7.57 mm) and mass (4.085 kg) as this example. It gave each pair of legs its own grain
through `face.appearance` on a selection rather than by splitting them into bodies.

