# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design an injection-moulded enclosure for a 100 × 70 × 1.6 mm circuit board with its corners
   rounded 4.5 mm, as two parts, a base and a lid, meeting at a horizontal parting plane, both moulded in
   straight-pull tools without slides. Make the board length and width, the inside height (floor to
   ceiling, 20 mm) and the wall thickness (2 mm) public parameters: board 60 to 160 by 40 to 100 mm in
   5 mm steps, inside height 17 to 24 mm, wall 2 to 3 mm in 0.25 mm steps. Leave 1 mm all round between
   the board and the inner walls; round the plan corners 5.5 mm inside, the bottom and top edges 1 mm
   inside and one wall more outside. Draft the base's sides 1.5° about the parting plane so it narrows
   downward, the lid's 1° so it narrows upward, and shell each open at the parting plane.

2. The board sits on four posts at its mounting holes (Ø 3.2 mm, 4 mm in from its edges) with 4 mm under
   it, and the parting plane runs through the axis of a USB-C receptacle on the board's top, 1.58 mm above
   it. Each post is Ø 6 mm with a Ø 3 mm locating pin that ends 0.2 mm under the board's top with a
   0.3 mm chamfer, drafted 1.5° about the floor's top, rounded 0.4 mm at its foot and cored from below to
   leave a wall of 0.4 of the nominal wall and a top 0.6 of it thick. Give the base a lip of half the wall,
   2 mm high, on the inside, with a 0.3 mm lead-in chamfer, and cut the lid a matching step that clears it
   by 0.1 mm at the side and 0.2 mm on top, both drafted 1.5°. Over each post the lid has a hold-down
   tube, Ø 5.2 mm, 0.4 of the wall thick, drafted ½° on both sides and cored to the ceiling, ending 0.21 mm
   above the board, with three radial crush ribs on its end (0.6 mm wide, 0.15 mm flat tips, drafted ½°)
   that reach 0.16 mm into the board.

3. Now four U-shaped snap latches on the lid's long walls, at a quarter and three quarters of the length,
   catching under lugs on the base. Each latch has two legs, 2.5 mm wide and 0.4 of the wall thick, 1.1 mm
   off the wall (so the mould's steel behind them stays at least 1 mm thick), hanging from root blocks
   7 mm above the parting plane, joined at the bottom by a bar 1.5 mm thick. Each lug is 5 mm wide with
   0.5 mm clear to the legs, sticks out 1.9 mm, has a 1.2 mm high outer face below the parting plane and
   an underside rising outward at 20°; the bar's top lies on it,
   and the bar's inner bottom edge has a 30° lead-in over 0.9 mm below a 0.3 mm land. Draft every latch
   and lug face 1.5° toward the tool half that forms it, the legs' window and end faces 3°, and recess
   the lid's wall behind each leg, drafted ½° the other way, so the core can draw the slot.

4. Put a USB-C receptacle at one short end, centred on the board's width: the specification's shell
   opening, 8.34 × 2.56 mm, in a 0.3 mm shell, 7.35 mm long, its front 0.6 mm past the board's edge. Cut
   the opening for the plug in that end wall, half in each part: the plug's overmold is at most
   12.85 × 7.0 mm, so give it 0.25 mm all round at the opening's narrowest, draft its sides 1.5° away from
   the parting line and round its inner corners 1 mm. Add three flat chips on the board.

5. Make the base matt white ABS and the lid translucent smoke-grey polycarbonate (1200 kg/m³); the board
   green, the receptacle steel. Add outputs for the masses, the latch strain ε = 1.5 y h / l² (y the bar's
   0.8 mm reach under the lug, h the leg thickness, l from the roots to the lug's lower edge), and the
   forces to spring one latch open and push it shut (secant modulus 1815 N/mm², friction 0.5).

6. Add checks: each part's draft over the faces its cavity forms and over those its core forms, each in
   its own pull (base outside at least 1.5°, lid outside at least 1°, the rest at least ½°); for every
   retaining face, a column along its pull that its own part must not enter (above each bar, below each
   lug, down the slot behind each leg); at least 1 mm of mould steel between each leg and the wall behind
   it; the walls at 2 mm; the latch strain within 60 % of polycarbonate's
   4 %; the crush ribs' depth in the board; the plug opening; no other parts overlapping; and a section of
   each part in closed form. Give the document a title and description, check it all, and show me a
   picture from three-quarters above.

## Acceptance

At the defaults the result must have:

- a base and a lid as two bodies, with the board, the chips and the receptacle; only the lid's crush
  ribs overlap the board (about 0.18 mm³), nothing else overlaps;
- an outside of 106.0 × 76.0 mm at the parting plane, 9.18 mm above the bottom, 24.0 mm high, the latches
  standing 2.7 mm off the long walls;
- a base of 21,004 mm³ and a lid of 23,988 mm³, each within 2 % (21.8 g of ABS, 28.8 g of polycarbonate);
- four latches with legs of 8.2 mm and a strain of 1.43 %, at most 2.4 %;
- every retaining face open along its pull: no column rising from a bar, falling from a lug or running down
  a slot behind a leg enters its own part, and the mould steel between each leg and the wall behind it is
  at least 1 mm thick (1.04 mm);
- walls of 2 mm, a draft of at least 1.5° on the base's outside, 1° on the lid's and ½° on every other face
  in its part's pull;
- a plug opening at least 12.95 mm wide and 7.1 mm high;
- every check passing, and the same at a 160 × 100 mm board with 24 mm inside and 3 mm walls, and at a
  60 × 40 mm board with 17 mm inside and 2 mm walls.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above: passed.
Its enclosure has the same walls (2.000 mm), latch strain (1.428 % against 2.4 %), release and closing forces
(1.685 and 2.553 N), crush (0.160 mm into the board) and drafts (1.5° base, 1° lid, ½° cores) as this
example, masses within 0.4 % (21.76 and 28.89 g), its three tooling columns clear and more than 1 mm of core
steel behind each latch leg, with its own 20 assertions passing at six corners of the parameters. It first
drafted the USB opening narrowest at the parting line, an undercut its own draft check found. It proved the
walls by distances, since `measure.thickness` reported 0.104 mm at the rim
([F-020](../../3DCRAFT-FEEDBACK.md#f-020)). About 325 steps, written by a script.
