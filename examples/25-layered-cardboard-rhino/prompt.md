# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design a layered cardboard sculpture: an original, stylised standing rhinoceros, 300 mm from
   the rump to the upper lip, to be laser-cut from corrugated board. Make the length a parameter that
   scales the whole figure (200 to 300 mm in steps of 10 mm), and the board a choice from a table of two
   real white-faced boards: Ball & Doggett Claycote B flute, 3 mm, 569 g/m², and Claycote E/B twin flute,
   4.5 mm, 826 g/m², both sold in 1240 × 2450 mm sheets.

2. Model the rhino as one smooth solid, lying along x with its feet on the ground and its plane of
   symmetry at y = 0. Draw the body as a lines plan: about 16 stations from the rump to the lip, each a
   closed spline section through its top, its bottom and its widest point. Make the barrel about 91 mm wide at
   its widest, the back about 125 mm high with a hump over the shoulders of about 142 mm, the belly about
   41 mm off the ground, and a long head carried low, the lip about 48 mm off the ground. Add, on the left
   side only, a front and a hind leg (column-like, about 22 mm wide across the board with their sides
   straight up and down, so every layer either reaches the ground or misses the leg; flat soles; their
   centre line about 22 mm from the plane of symmetry), and an upright pointed ear on top of the head; on
   the centre line a long front horn curving back and a shorter rear horn, standing about 10 mm apart on
   the head, and a round tail about 8 mm thick that leaves the rump straight back and bends down. Join
   them into one solid. Only the left half will be used.

3. Cut the left half into layers: as many whole boards as fit in the barrel's half-width (15 of 3 mm at
   300 mm), the first one starting at the plane of symmetry. Each layer is a flat plate of the board's
   thickness whose outline is the figure's section at the middle of that board, with walls square to the
   board, as a laser cuts it: take the sections as flat faces and give each face the board's thickness,
   half to each side. Mirror every layer to the right side, so the stack has an even count with the plane
   of symmetry between the two middle layers. Every layer must be one piece.

4. Instead of dowels, mark where each layer goes: on the outward face of each layer but the outermost,
   the outline of the next layer outward, clipped to the layer. The two middle layers are glued face to
   face on their identical outlines and need no mark between them. Colour the board's faces white and its cut edges kraft brown, and give it
   its density from the grammage. Export, for each layer of both halves, its outline (seen from its
   outward face) and its mark as two DXF files on the same origin, and lay the distinct parts out on a
   1240 mm wide sheet.

5. Add outputs for the board area and the mass, and checks: the layer count, that every layer has exactly
   two flat faces, that the left half's volume is the board thickness times its layers' outward face
   area (straight walls), that the right half's volume equals the left's, that every layer but the middle
   pair has its place marked on its inner neighbour (28 marks at 300 mm on B flute), that the marks
   together cover at least 90 % of the area of the layers placed on them, which layers stand on the ground, that the board's area fits one sheet, and that the centre of mass lies between the hind
   and the front feet. Check it at both boards and a few lengths, give the document a title and description, run a check
   of the whole document, and show me a picture from the front left.

## Acceptance

At 300 mm on B flute the result must have:

- one smooth figure 300 mm from rump to lip, about 91 mm wide and about 144 mm high, with a front and a
  hind leg on flat soles and an ear on its left side, two horns and a tail;
- 30 layer bodies, 15 a side, each a plate of 3 mm (`cut.list`: every layer a plate of thickness 3 mm)
  and each one piece; the stack 90 mm wide with the plane of symmetry between the two middle layers, four
  legs on flat soles, an ear on each side, two horns and a tail; no leg piece that ends above the ground,
  and no notch narrower than the board between the horns or between the tail and the rump;
- 28 marks, one on each of layers 1 to 14 of each half, together covering at least 90 % of the area of the
  layers placed on them;
- a board area of about 0.5 m² and a mass of about 300 g (within 10 %);
- the centre of mass between the hind and the front feet;
- a cut DXF and an engrave DXF per layer that overlay on one origin;
- 20 layers (10 a side) on E/B flute at 300 mm, and every check passing at 200 mm on both boards.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the five turns above: passed
in all but one check, which the turns worded ambiguously. Its rhino has the same build as this example: 15
straight-walled layers a side at 300 mm on B flute (10 on E/B), 0.518 m² of board against 0.519 here, 294.6
g against 295.5 g, the centre of mass between the feet, the left half's volume equal to 3 mm times its
layers' outward faces, and a cut and an engrave DXF per layer on one origin; its checks passed at all 22
lengths and boards. Its one failing check read "the marks cover at least 90 %" layer by layer: the board
inside a leg's first layer has no leg under it, so that layer rests only about 85 % on its mark. The check
here is over the whole stack, and turns 4 and 5 now say "together" and where the marks go. It met two
kernel limits of its own: `feature.thicken` refuses a sheet ([F-173](../../3DCRAFT-FEEDBACK.md#f-173)), and
one plate of its own geometry was refused at 230 mm ([F-169](../../3DCRAFT-FEEDBACK.md#f-169)). About 389
steps, written by a script.
