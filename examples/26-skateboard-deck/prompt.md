# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model an original street skateboard deck and the mould it is pressed in, in inches. Put the
   origin on the deck's top surface, on its centre line, in the middle of its length: x along the deck
   (nose toward +x), y across, z up. The deck is 8 in wide and 31.75 in long tip to tip in plan, centred
   on the origin, with a 14.25 in wheelbase between the inner truck holes. The nose is 1/4 in longer than
   the tail, so the trucks are centred 1/8 in toward the tail (x = −1/8 in). Make width
   (7.5 to 8.5 in, steps of 1/8 in), wheelbase (13.75 to 14.75 in, steps of 1/8 in), concave depth (3/8
   to 5/8 in, steps of 1/16 in, default 1/2 in) and kick angle (18° to 24°, steps of 1°, default 20°)
   public parameters.

2. The top surface:
   - A radial concave: a circular arc across the deck, 1/2 in deep at the rails. Keep the same arc along
     the whole deck, kicks included.
   - Along the deck, the top's centre line lies on z = 0 between the trucks, to 1/2 in past the outer
     holes. There it bends up over a 3 in radius into straight kicks at the kick angle, and it runs on to
     21 in from the origin each way.
   - Build every layer as a sweep of its cross-section along that centre line. That way the flats and
     kicks are exact cylinders and every layer is concentric with the one above.
   - The deck is seven 1/16 in hard-maple plies: face, core, crossband, centre core, crossband, core,
     face. Model it as five layers: the top face and core as one body, a crossband, the centre core, a
     crossband, and the bottom core and face as one body. Each layer lies between its two concentric
     arcs, and runs well past the deck on every side, like the veneers as they come out of the press.

3. Cut the deck out of that pressed stack straight down, as a router following a template would.
   - The outline: straight rails at the full width, and at each end a 5 in radius tip arc blended into
     the rails by 3 in corner arcs.
   - In the same cut, drill eight 13/64 in truck holes in the new-school pattern: 2-1/8 in along by
     1-5/8 in across per truck.
   - Then round the top and bottom rails of the outer layers with a 5/64 in round-over.

4. Now the press mould, two halves of MDF. Each starts as a block 36 in along x by 10.5 in across y,
   centred on the origin in plan, with its outer edges chamfered 1/8 in.
   - The upper block runs from z = −1/2 in to z = 6.5 in. Cut away everything below the deck's top
     surface (the stack's top skin, swept on to the block's edges), so the upper half's face is that
     surface.
   - The lower block runs from z = −3 in to z = 6.5 in. Keep only what lies below the deck's bottom
     surface (the stack's bottom skin, 7/16 in under the top and concentric with it, swept on to the
     block's edges), so the lower half's face is that surface.
   - Keep the upper half in this closed position for the checks, and hide it. Show a copy of it turned
     face up: rotated 180° about the x axis, then moved 14.5 in in +y (a 4 in gap between the two
     halves) and up until its back sits on z = −3 in, like the lower half's.

5. Materials: hard maple at 12 % moisture, with a specific gravity of 0.63. Work the density out from
   that, and give every layer of the deck that material. Run the grain along the deck in the face pairs
   and across in the crossbands. Dye the centre core a clear blue, so it shows as a line on the rails.
   Make the mould MDF brown. Add outputs for the deck's mass in kilograms and its volume.

6. Add checks:
   - **Layers.** Each layer is the right number of plies thick.
   - **Mould gap.** The closed halves are exactly the stack's 7/16 in apart between the trucks and along
     the nose kick, and the deck touches both.
   - **Holes.** All eight holes go through every layer. The inner holes are a wheelbase apart and the
     pattern is right.
   - **Kick.** The kick angle, from two sections in the straight nose kick.
   - **Concave.** The centre core's height and area at mid-length, in closed form from the concave.
   - **Curvature.** The centre core's largest Gaussian curvature, in closed form for the bend's torus, and
     its flat and kick faces developable.
   - **Milling.** The lower half's tightest concave radius, from its largest Gaussian curvature, in
     closed form.

   Give the document a title and description, run a check of the whole document, and show me a picture
   of the deck in the open mould from the front, three-quarters above.

## Acceptance

At the defaults the result must have:

- five deck bodies, 0.125, 0.0625, 0.0625, 0.0625 and 0.125 in thick, together 0.4375 in;
- a deck volume of 109.27 in³ within 1 % and a mass of 1.263 kg within 1 % (density 705.6 kg/m³);
- eight 13/64 in holes through every layer, the inner holes' walls 14.046875 in apart (the wheelbase less
  one hole), the pattern's walls 1.921875 in along and 1.421875 in across;
- the closed mould faces 0.4375 in apart between the trucks and along the nose kick;
- a 20° kick, and the centre core's section at mid-length 0.5566 in tall and 0.5051 in² in area;
- the lower mould's tightest concave radius 2.729 in;
- every check passing, and the same at width 7.5 in with a 24° kick and at width 8.5 in with a 3/8 in
  concave.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the turns above: passed. Its
deck has the same mass (1.2635 kg), volume (109.27 in³), 20° kick, core section (0.556619 in high,
0.505051 in²) and bend curvature (0.0219084 per in²) as this example, five bodies of 2, 1, 1, 1 and 2 plies,
the bolt pattern wall to wall as here, the mould halves 7/16 in apart and touching the deck, and its own 37
assertions passing at the four corners of the parameters. Its mould's tightest milling radius came out
2.763 in against 2.729 here: turn 4 left the mould blocks' position open ("the deck's centre" was not
defined), so turns 1, 2 and 4 now give the origin, the centre line and the blocks' sizes and places. It also
found that the bends are freeform faces, not tori ([F-159](../../3DCRAFT-FEEDBACK.md#f-159)), and that a
chamfer round a mould half's swept rim is refused ([F-158](../../3DCRAFT-FEEDBACK.md#f-158)); it cut those
rims with swept strips. About 198 steps, written as a script.
