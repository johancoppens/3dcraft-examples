# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design an electric guitar body for a CNC router: an original double cutaway with a carved top
   and a bolt-on neck. Put the tail's centre at the origin, the neck pointing along +y, the treble side
   at +x and the top facing +z. Make the scale length (648 mm, from 610 to 686 mm) and the body thickness
   at the top's level plateau (45 mm, from 44 to 50 mm) public parameters. Draw the outline as one
   closed, smooth spline: lower bout 331 mm wide around y = 125, a waist about 272 mm wide around
   y = 270, upper bout about 295 mm wide around y = 345. The body ends square to the neck at y = 380,
   between two cheeks beside the neck pocket that are 14 mm thick (outer faces at x = ±42) with their
   outer corners rounded 12 mm. From the cheeks the cutaways are open C-curves: down to their bottoms at
   (±62, 328), the 20th fret's place, then out and up to the horns. The horns taper from about 74 mm
   wide at their roots to about 42 mm near their tips and lean in: the treble tip a round of 18 mm
   radius centred at (114, 396), the bass tip one of 18 mm centred at (−113, 430), so the bass horn ends
   by the 12th fret. Keep every inside curve above 12.7 mm radius and every outside curve above 8 mm.
   Extrude a blank 5 mm thicker than the body.

2. Carve the top as a surface through a network of curves and cut the blank with it. Keep a level
   plateau at the full thickness for |x| ≤ 50 mm from y = 75 mm to the neck end: the neck, the pickups and
   the bridge sit on it, so the neck needs no angle. From there the top falls smoothly, curvature
   continuous and without any bump, by 10 mm to the rim: at the sides between |x| = 50 and 150 mm, flat at
   rim height beyond; toward the tail from y = 75 mm to rim height at y = −45 mm. Build the curves as cubic
   B-splines from control polygons (25 mm apart across, 30 mm along) so the plateau is exactly flat, and
   place the curves of each family at the other family's knots, at the height the B-spline takes there,
   (P[k−1] + 4 P[k] + P[k+1]) / 6, so the two families meet exactly where they cross.

3. Now the neck and the bridge. Rout a Fender-pattern neck pocket 2-3/16 in wide, 3 in long and 5/8 in
   deep, its heel end a 5 in arc blended into 1/4 in corners, the arc's vertex 3 in inside the body's
   edge at y = 380 mm. Drill four 3/16 in neck screw holes through the back, 1-1/2 in by 2 in apart and
   centred on the pocket. The neck has 22 frets and its board ends 1/4 in beyond the 22nd fret, flush with
   the heel end, so place the saddle line at the scale length from the nut by the equal-tempered fret rule.
   The bridge is a string-through hardtail with 10.5 mm string spacing: six 1/8 in string holes through
   the body 25 mm behind the saddle line, and six 5/16 in ferrule bores 11/32 in deep on the back.

4. Pickups and controls. Two humbucker routes 72 by 40 mm with ears 20 mm wide to 87 mm overall, 21 mm
   deep from the plateau, every inside corner cut by a 1/2 in bit: the neck route leaves a 6 mm wall to
   the pocket's heel end, the bridge route is centred 42 mm ahead of the saddle line. Three 3/8 in holes
   for long-shaft pots (3/4 in thread) at x = 105 mm, y = 85, 125 and 165 mm. From the back rout a
   stadium-shaped control cavity of 25 mm radius around the three pots, its ceiling 15.05 mm below the
   plateau (the thread less 4 mm for washer and nut), with a cover recess 2 mm deep and 6 mm wider all
   round, and four 1/16 in pilot holes 10 mm deep in the recess at the cavity's ends and sides. On the
   treble side at y = 135 mm bore a 7/8 in hole for an Electrosocket-type cup jack straight through into
   the cavity, centred on the side's straight part between the two roundovers, so that the cup's flange,
   0.989 in across, sits flat at every thickness. Drill the wiring with 1/4 in bits: one from the neck
   pocket, just above its floor, through the neck route into the bridge route; one 20° up from the open
   cavity into the bridge route's end, entering 6 mm above its floor.

5. After all the cuts, round the back edge with a 3/16 in roundover and the top edge with a 1/8 in one,
   all along the outline. Finish it in candy-apple red: a red car paint over a metallic base with a clear
   coat. The wood is red alder at 450 kg/m³; give me its mass. A tolerance of 0.01 mm is plenty for wood.

6. Add checks: the distance from the pocket's heel arc to the nearest string hole against its closed form
   from the scale length; the pocket floor's height and the pocket's depth to the carved top; the routes'
   depth to the top; the pots' reach through the wood over the cavity, and at least 5 mm of wood there;
   the 6 mm wall between pocket and neck route; no rounded corner face of a radius under the 1/2 in bit's
   and the 18 corners it cuts; the gap between the routes against its closed form; six string holes; the
   back roundover tangent to the back; the jack's flange on the straight side. Check it over the whole
   range of both parameters, give the document a title and description, and show me a picture from
   three-quarters above the treble lower bout.

## Acceptance

At the defaults (648 mm, 45 mm) the result must have:

- one body about 331 × 448 × 45 mm, its mass 1.83 kg within 5 % (the outline is drawn by eye, so its
  volume of 4060 cm³ is matched only roughly), the cutaway bottoms at y = 328 mm;
- a level plateau at 45.000 mm: the pocket floor 29.125 mm above the back and 15.875 mm below the top,
  the route floors 21.000 mm below the top;
- the saddle line 128.31 mm from the tail (string holes at 103.31 mm), the heel arc 198.943 mm from the
  nearest string hole (188.281 mm at 610 mm, 209.605 mm at 686 mm), the route floors 67.489 mm apart;
- 18 concave corner faces of exactly 1/4 in radius and none smaller;
- the cavity ceiling 15.05 mm below the plateau, at least 5 mm of wood over it;
- the jack bore centred on the straight side, at least 1.45 mm of it above and below the bore at 44 mm;
- every check passing, and the same at 610 mm × 44 mm and 686 mm × 50 mm.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its body has the same saddle line (128.31 mm), heel-arc distance (198.943 mm), pocket (floor 29.125 mm,
15.875 mm deep), routes (21.000 mm, 67.489 mm apart), wall (6.000 mm), 18 corner faces of 1/4 in and jack
clearance (2.42 mm) as this example, and its mass is 1.859 kg (+1.7 %, its outline drawn its own way). Its 17
checks pass over the range. It built the carved top first time from turn 2; its plateau came out flat to
0.6 µm, not exactly, so its first pocket cut was refused at the edge of tolerance until it started the cuts
above the plateau, and its back roundover needed the document's 0.01 mm tolerance, as this one does. It found
that `-5/8 in` is a length⁻¹ (write `(5/8) in`) and that `^` takes whole exponents only ([F-131](../../3DCRAFT-FEEDBACK.md#f-131)).
About 164 steps.

