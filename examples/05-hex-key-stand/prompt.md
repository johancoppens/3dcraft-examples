# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. I want to 3D print a desk stand for my metric hex key set, ISO 2936, sizes 1.5, 2, 2.5, 3, 4, 5, 6, 8
   and 10 mm. Put the keys in a table: the width across flats and the length of the long arm of the
   standard's normal series (46.5, 52, 58.5, 66, 74, 85, 96, 108 and 122 mm). Add three parameters a
   maker would change: the print clearance per side (0.15 mm, from 0.1 to 0.4), how far the embossed
   labels stand proud (0.6 mm, 0.4 to 1.2) and the share of each long arm that goes into the stand (0.35,
   0.25 to 0.45).

2. Make the stand a staircase of nine steps side by side, 16 mm wide each, 32 mm deep, smallest key on the
   left. Each step is as high as a 2 mm floor plus that key's share of its long arm, so the bigger keys
   stand taller and go deeper. Round the four vertical corners with 4 mm, the top edges of every step with
   1 mm, and give the bottom edge all round a 0.4 mm first-layer chamfer.

3. Cut a hexagonal socket for each key in the middle of its step, 20 mm from the front, the key's width
   across flats plus the clearance on each side, with a corner pointing to the front. Every socket goes
   down to the 2 mm floor. All sizes should come from the table.

4. In front of each socket, 6.5 mm from the front edge, emboss its size in 6 mm figures, standing on that
   step by the label height, taken from the table too. Keep the labels as a separate body, so they can be
   printed in a second colour.

5. Call the stand's body Stand. Make it orange PLA, matte, and the labels black PLA (PLA is 1240 kg/m³). Report the stand's
   volume and the total mass in grams.

6. Add checks: nine sockets; walls and floors around the sockets at least 1.2 mm; no overhang below 45°
   when printed flat (every face but the bottom); the area of a horizontal cut halfway up the lowest step,
   worked out by hand from the footprint, the rounded corners and the nine hexagons; and the height of the
   top step. Give the document a title and description, check the whole document, and show me a picture
   from the front left, above.

## Acceptance

At the defaults the result must have:

- a stand 144 × 32 × 44.7 mm, volume 126 545 mm³ within 1 %, and nine hexagonal sockets whose depth is 0.35
  of the long arm (16.28 mm for 1.5, 42.7 mm for 10), all ending 2 mm above the bed;
- sockets 1.8 to 10.3 mm across flats (the key plus 2 × 0.15 mm);
- labels 1.5 to 10 standing 0.6 mm proud on their steps, in a separate body;
- a section halfway up the lowest step of 4344.41 mm²;
- walls at least 1.2 mm, no face below −45° except the bed face, rounded corners and rims, a first-layer
  chamfer;
- every check passing, and the same with clearance 0.4 mm, insertion 0.25 and label relief 1.2 mm.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above: passed.
Its stand checks itself with 5 assertions and has a volume of 126 544.836 mm³ and a section of
4344.4085 mm² halfway up the first step, the same as this example's. Its wall check was not proven over the
chamfered and filleted edges at first (F-020) and passed once it measured the sockets' faces only.

