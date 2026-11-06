# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a square-to-round transition for ventilation ductwork, as a parametric part in mm: from a
   rectangular duct 400 × 300 mm (inside dimensions a × b, EN 1505) to a round duct of 250 mm (EN 1506),
   300 mm long overall from the flange face to the end of the round spigot. Put the EN 1505 side lengths
   100, 150, 200, 250, 300, 400 and 500 mm in a table. Put the round sizes in a second table with, per
   size, the spigot's outside diameter band, the round duct's largest inside diameter, the spigot's length
   and the smallest side allowed (the round size plus 50 mm, taken up to the EN 1505 series): 125 mm
   (123.8 to 124.3, 125.5, 36, 200), 160 (158.7 to 159.3, 160.6, 36, 250), 200 (198.6 to 199.3, 200.7,
   36, 250), 250 (248.5 to 249.3, 250.8, 55, 300) and 315 (313.4 to 314.3, 315.9, 55, 400). Publish four
   parameters: width and height as choices from the first table, at least the round size's smallest
   side; the round size as a choice from the second; and the overall length, 300 to 800 mm in 10 mm steps.

2. It is 0.8 mm galvanised sheet, made in four identical pieces with the seams down the middles of the
   four sides. From the flange face up: a straight rectangular collar, the duct's inside size with 8 mm
   inside corners, 30 mm long to where the transition starts. Then the transition: a 15 mm straight, the
   slanted part, and a 15 mm round straight. Last comes a round spigot as long as the table says, its
   outside diameter in the middle of its band. Model one piece of the slanted part as half of a flat end
   triangle, a cone-shaped corner and half of a flat side triangle, sewn together. Draw it as the
   transition's inside surface, inside the collar and outside the spigot with 0.3 mm clearance. Make the
   corner a ruled surface between its two arcs, so that it is developable and stays light.

3. Give the piece its 0.8 mm outward from that inside surface, mirror it into the other three pieces, and
   add the two straights as 0.8 mm bands. For the flat pattern, draw the same piece again at the middle of
   the metal, 0.4 mm further out, with its corner as a true developable between the arcs. Add the
   straight's flaps along its two flat sides and unfold it in one piece. Lay the pattern on the floor in
   front of the fitting, at the level of the flange face and clear of the frame. I'll want it as a DXF.

4. Now the ends. Let the collar run up over the rectangular straight and the spigot down inside the round
   straight, 15 mm on parallel faces, so both can be riveted. Around the collar's bottom put a flange frame
   like a P20 sheet angle: 1 mm sheet, a 20 mm leg up along the collar and a 20 mm flange outward with
   square outer corners, bent with a 1 mm inside radius. Put a 9 mm hole for an M8 bolt in each corner of
   the flange, in the middle of its width. On the spigot, swage the last 5 mm in by 1 mm as a lead-in.
   Put a black double-lip EPDM seal round the middle of its exposed length: 10 mm wide, 1.5 mm thick, with
   two lips reaching 2 mm beyond the round duct's largest inside diameter.

5. Make the transition, the straights, the collar and the spigot galvanised steel: light grey, metallic,
   fairly smooth. Give the frame and the flat pattern a duller, cooler mill finish, and the seal EPDM at
   1160 kg/m³. Add outputs for the pattern's area, the volume of one transition piece and the mass of all
   the steel parts in kg.

6. Add checks: both sheets of the piece are developable, with zero Gaussian curvature; the flat pattern
   has the middle sheet's area; the flat triangles and flaps in closed form; the corner's area against a
   numerical integral of the ruled surface (rulings join the points of equal angle on its two arcs); the
   piece's volume divided by the thickness matches the pattern's area less its flaps within 0.2 %; the
   sheet is at least the 0.7 mm EN 1507 class S minimum; the collar and the spigot do not overlap the
   straights they lap; the spigot is within its band; the seal reaches past the duct's wall; the overall
   length; four bolt holes at least 2.5 t + r from the bend; and the pattern clear of the frame. Give the
   document a title and description, check the whole document, and show me a picture from the front, a
   little to the right and above, with the pattern in front of the fitting.

## Acceptance

At 400 × 300 to 250, 300 mm long, the result must have:

- four transition pieces of 0.8 mm, each a flat half triangle, a curved corner and a flat half triangle,
  meeting at seams in the middles of the sides, with 15 mm straights at both ends;
- a developable middle sheet of 58 833 mm² within 1 % (flaps included), with zero Gaussian curvature;
- one flat pattern in one piece with exactly that sheet's area;
- one transition piece of 43 072 mm³ within 1 %;
- the collar and the spigot lapping the straights 15 mm on parallel faces; a spigot of 248.9 mm outside
  diameter and 0.8 mm wall; an overall length of 300 mm; a frame with four 9 mm holes;
- steel parts of 2.72 kg within 3 %;
- the four parameters, every check passing, and the same at 300 × 250 to 200 and at 500 × 400 to 315,
  500 mm long.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its fitting checks itself with 26 assertions and has the same flat pattern (58 832.87 mm²), piece
(43 072.29 mm³), spigot (248.90 mm) and length (300.000 mm) as this example; its steel weighs 2.737 kg
(0.6 % more). It measured the pattern's clearance from the frame by its box, since `clearance` and
`distance` refuse sheets (F-105).

