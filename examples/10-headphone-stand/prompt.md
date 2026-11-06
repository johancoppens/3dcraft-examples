# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design a one-piece headphone stand, printed upright in PETG without supports: a round, weighted
   base, a slim column that flares into a wide saddle curved like a headband, and a cable hook at the
   back. Two parameters: the height from the desk to the top of the saddle, 250 mm (230 to 310 mm in
   steps of 10), and the saddle's width at its shoulders, 120 mm (100 to 140 mm in steps of 5). Work in
   millimetres with a tolerance of 0.001 mm.

2. The base is a disc Ø 140 × 16 mm with its top edge rounded 5 mm and a 0.6 mm × 45° first-layer chamfer
   round the bottom. It carries a steel disc Ø 100 × 8 mm, dropped in at a pause in the print. Its pocket
   is 0.3 mm larger in radius and 0.2 mm deeper than the disc, with a 2.4 mm floor under it. Model the
   disc as a body of its own, lying on the pocket's floor.

3. The column and the saddle will be one smooth loft through horizontal sections. Make every section a
   smooth closed curve through eight points: four on its axes, at its half-width a (left to right) and
   half-depth b (front to back), and four on the diagonals at k·a and k·b, so k sets how square it is.
   The column has five sections, evenly spaced, k = cos 45° (oval). It starts at a root of a = 15 mm,
   b = 13.5 mm, sunk into the base halfway between the pocket's top and the base's top, and narrows
   evenly to a neck of a = 11 mm, b = 10.5 mm.

4. Above the neck the column flares into the saddle. The saddle's top will be an arc of radius 90 mm
   across its width, highest at the full height, so its shoulders sit lower than the top by the arc's
   sagitta over the saddle's width. There the section is half the saddle's width by 22 mm, with k = 0.8.
   Keep every overhang printable: the flare widens as the 1.5th power of the way up, and is
   1.5 × (half the saddle width − 11 mm) / tan 40° tall, so its steepest side is 40° from upright. Put
   sections at a quarter, half and three quarters of the way up, with k growing evenly from cos 45° to
   0.8. Add a last section 6 mm above the top of the saddle that carries the flare on, k = 0.8: its a
   grows by tan 40° per millimetre above the shoulders, its b by 1.5 × 11.5 mm divided by the flare's
   height per millimetre. It only shapes the loft; the cut takes it off.

5. Cut the top off along that 90 mm arc, all across the saddle, and make sure nothing of the loft is left
   above it, even at the widest saddle. Round the saddle's rim 8 mm, and the column's root into the base
   10 mm.

6. Sweep a 10 mm rod for the cable hook out of the back of the column. It starts on the axis halfway
   between the base's top and the neck, going straight up, and bends towards the back with a 12 mm
   radius until it rises at 50°. It runs 55 mm, bends back upright with 12 mm, and ends 8 mm higher in a
   ball of the rod's radius. Join base, column and hook into one part, round the hook's root 3 mm, and
   call the part Stand.

7. Make it sunflower-yellow PETG with a satin finish (1270 kg/m³) and the disc steel. Report the stand's
   mass in grams, the disc's mass and the height of the stand's centre of mass. Report the angle the
   stand can be tilted to before it tips over the edge of its foot, carrying 400 g of headphones at the
   top of the saddle: once as modelled, and once in the worst case, with all of the stand's plastic
   counted at the top of the saddle too.

8. Add checks: nothing that faces down is flatter than 45° when printed upright, except the bed face and
   the pocket's roof, which bridges over the steel; the pocket's floor and roof are at least 1.2 mm
   thick; the centre of mass lies within 1 mm of the axis both ways; the worst-case tilt is at least
   10°; the base's volume below its top face, worked out by hand; nothing of the loft's top left after
   the cut; and the disc clears its pocket's wall and roof. Give the document a title and description,
   check it all, export the stand alone as a 3MF for printing (within 0.1 mm, facets of at most 8°), and
   show me a picture from the front left, from above.

## Acceptance

At the defaults (250 mm, saddle 120 mm) the result must have:

- a stand of PETG, volume 479 686 mm³ within 1 % (609.2 g as a solid), and a steel disc of 62 832 mm³
  (493.2 g) in a pocket Ø 100.6 × 8.2 mm with a 2.4 mm floor;
- a base volume below its top face of 178 722.1 mm³ (exact to 0.01 mm³);
- a saddle 250 mm high at its crown, 120 mm wide at its shoulders 227.1 mm up, 44 mm deep, its top an arc
  of radius 90 mm, rounded 8 mm;
- a hook whose ball is 41.0 mm behind the axis and 143.3 mm up;
- no downward face below −45° but the bed face and the pocket's roof: the first-layer chamfer at −45°,
  the flare at about −39° and the hook at −40°;
- a centre of mass of stand and disc on the axis (0.00 mm across, 0.17 mm towards the hook), a tilt of
  30.8° as modelled and 22.2° in the worst case;
- a 3MF holding only the stand;
- every check passing, and the same at 230 mm with a 140 mm saddle and at 310 mm with a 100 mm saddle
  (worst-case tilt 23.2° and 18.6°).

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the eight turns above:
passed, with nothing refused. Its stand checks itself with 11 assertions, also at the four corners of the
range, and weighs 609.2 g with a 493.2 g disc; it tilts 30.84° as modelled and 22.20° in the worst case, its
base below the top face is 178 722.1 mm³ and its 3MF has 43 880 triangles, all the same as this example's.

