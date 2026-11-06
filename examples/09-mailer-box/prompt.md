# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a FEFCO 0427 mailer box, the roll-end tuck-front style, die-cut from one sheet of single-wall
   E-flute kraft board 1.6 mm thick and 340 g/m², 200 × 150 × 60 mm inside (length × width × height). Draw
   the flat blank as one sketch on the board's inside face, with the base 200 × 150 mm at the origin, and
   fold it later as thick panels hinged on that face, so the inside sizes are the sketch's. Every size must
   be a formula of the inside length, width and height, the board thickness t and a gap g of 0.5 mm between
   layers that fold over each other. Make length (100 to 450 mm), width (60 mm up to the length) and height
   (25 mm up to the length, at most 150 mm) public parameters.

2. The walls. The front wall, t higher than the inside height, and the back wall, the inside height, hang on
   the base's long sides. Each has an ear at both ends, folding in on a crease t + 2g beyond the base's end:
   half the width less g long, the height less 2t + 3g high, its lower edge 2g above the base crease with a
   45° cut to the crease's end. Chamfer the front wall's top corners at 45° down to its ear tops, and the
   back wall's top corners straight from the ear tops to the ends of the lid's hinge.

3. The rolled ends. The end walls are rolled double walls on creases 2t + 3g beyond the base's ends, t + g
   shorter than the base at each side, the base's corners cut at 45° between the ear creases and the end
   creases: an outer wall the height less t + g, a top panel t + 3g wide, and an inner wall g shorter than
   the outer, carrying two locking tabs a sixth of the width wide, centred at a quarter and three quarters
   of the width, t + g long. Cut a slot in the base for each tab, from t + 2g outside to g inside the inside
   length and g wider than the tab on each side.

4. The lid. It hangs on the back wall's top edge between creases t + g inside the length and is the width
   less t + g deep. Its ends carry dust flaps as deep as the ears (or half the width less g, if that is
   less), cut at 45° from the hinge and slanted at the front so that every point stays within the width less
   1 mm of the hinge; the lid's front corners are cut at 45° between the dust-flap creases and the tuck
   flap. The tuck flap at the front runs between creases 2t + 2g inside the length and is as high as the
   ears, or (the lid's depth − 2t) / √2 if that is less. Its ears are half the tuck's height wide, with a
   45° lead from the lid's crease and the far top corner rounded with half the ear's width, drawn as three
   chords.

5. Fold it with thick panels, t thick and 0.05 mm back from each crease, every crease folding towards the
   inside face. Add a Fold parameter from 0 (flat) to 1 (closed) that plays the folding sequence from a
   table: front and back walls with their ears (0 to 0.15), both end walls up (to 0.25), the left end rolled
   (to 0.37: the top panel to 50°, the inner wall swung down until plumb, then the top panel's last 40° with
   the inner wall kept plumb, so the tabs drop straight into their slots), the right end the same (to 0.5),
   the tuck flap and its ears (to 0.55), the dust flaps (to 0.6) and the lid closing (to 1), the tuck flap
   tilting back past square by half the lid's angle over the lid's first 60° and hanging plumb after that.
   Leave it at 0.71. Give it a matte kraft colour, and the board's density from its weight and thickness.

6. Prove the closed box while it shows half open, with a hidden copy folded closed and a hidden flat sheet
   of the blank: check the blank's length, width and area in closed form, the inside length, width and
   height when closed, the clear space between the lid's dust flaps and behind the tuck flap, the outside
   size when closed, and the number of panels. Add outputs for the board per box and its mass. Export the
   blank's cut and crease lines as DXF. Give the document a title and description, run a check of the whole
   document, try the parameters across their ranges, and show me a picture from the front right with the lid
   half open.

## Acceptance

At the defaults the result must have:

- one visible body of 19 panels, 1.6 mm thick, folded from one blank, that builds without two panels
  meeting at every Fold from 0 (flat) to 1 (closed);
- inside 200 × 150 × 60 mm when closed, and outside 212.6 × 153.2 × 63.2 mm;
- a blank of 450.4 × 474.8 mm, area 0.1613 m² within 1 %, and board mass 54.8 g within 1 %;
- two locking tabs in slots at each end, rolled double end walls with the ears inside them, dust flaps and
  a tuck flap with ears on the lid;
- clear space under the closed lid of 195.8 mm between the dust flaps and 147.9 mm behind the tuck flap;
- a DXF of the blank with its 18 creases on their own layer;
- every check passing, and the same at the corners of the parameters' ranges.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its box checks itself with 12 assertions, also at 22 fold amounts and nine sizes, and has the same
inside (200 × 150 × 60 mm), outside (212.6 × 153.2 × 63.2 mm), clear spaces and 19 panels as this example;
its blank area is 0.1622 m² (0.56 % over, within the 1 % of the Acceptance). It found that the back wall's
top corners cannot be cut at 45° with these sizes (3DCraft refuses the step a 45° cut would need at the
hinge), which the second turn now says.

