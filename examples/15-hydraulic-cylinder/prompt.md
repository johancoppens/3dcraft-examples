# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a double-acting tie-rod hydraulic cylinder to ISO 6020-2, the 160 bar compact series: bore
   40 mm with the 28 mm rod, a fixed clevis at the rear (MP1), a rod clevis at the front, stroke 200 mm,
   axis along x with the rod coming out towards +x. Make three parameters: the stroke (25 to 320 mm), the
   extension (0 to 100 % of the stroke, 50 by default) and a cutaway switch (on by default). Use the
   standard's sizes for bore 40: head and cap 63 mm square, head 45 and cap 38 mm long, tie rods M8 × 1 on
   a 41.7 mm square; the rod shoulder, when retracted, 35 mm in front of the head (WF), 153 + stroke from
   the cap's rear face (ZJ) and 172 + stroke from the rear clevis pin (XC), so the pin sits 19 mm behind
   the cap; the clevis has a 20 mm slot between two 10 mm cheeks, a Ø 14 pin hole and ends in a 17 mm
   radius round the pin, the slot stopping 17 mm from the pin. G 3/8 ports on top: the head's 62 mm behind
   the retracted rod shoulder (Y), the cap's 73 + stroke behind that (PJ).

2. Build the cylinder body. A honed tube 40 × 50 between head and cap, on 3 mm pilots of both, its bore
   with a 20° lead-in 0.5 mm deep at both ends. Under each end of the tube an O-ring of 1.6 mm cord in a
   face groove 1.2 deep and 2.3 wide (25 % squeeze), its inside at Ø 40.8. In the head an oil gallery Ø 34
   round the rod from the pilot to 9 mm in front of the port's axis, then a Ø 44 bore for the gland to the
   front face; tie-rod clearance holes Ø 9. In the cap, tapped holes for the tie rods (Ø 7, 19 deep, the
   tie rods screwed in 16 mm) and a Ø 16 pocket in its inner face, from the pilot back past the port.
   Each port: a Ø 25 spot face 0.5 mm deep, the mouth countersunk to Ø 16.9, the tapping hole Ø 14.95
   (G 3/8's minor diameter) 15.5 deep with a 118° point, then a Ø 9 passage down into the pocket (in the
   head the tapping hole already breaks into the gallery). Round the long edges of head and cap 4 mm,
   chamfer their faces 1 mm, round the clevis cheeks' outer edges 4 mm.

3. Now the gland and the moving parts. The gland is screwed into the head: Ø 44 inside, a Ø 42 boss 10 mm
   in front of the head, bore 28.5 for the rod, holding from the inside out a bronze-filled PTFE guide ring
   5.6 × 2.5, a polyurethane U-cup 6.3 × 5 with its lips towards the oil and a double-lip wiper 4.5 × 4;
   the land behind the U-cup twice as long as the other three, which are equal. Give it an O-ring of 1.6
   mm cord in a groove 1.2 deep and 2.3 wide on its outside, next to the inner land, and four spanner slots
   4 wide and 2 deep in the rim of its boss. The piston fills what the pilots leave
   (29 mm), sits on a Ø 20 spigot of the rod, its lands 0.25 mm under the bore and chamfered 0.5 mm at
   the outside, with two wear rings 5.6 × 2.5 and a 9.4 mm compact seal 5.5 deep between them, the four
   lands equal. The rod is Ø 28, chamfered to Ø 26 at 20° at the shoulder, with an M14 × 1.5 end 18 mm long and
   two 22 mm wrench flats, 12 mm long, midway between the boss and the shoulder. Everything moving follows
   the extension.

4. Add the rest: the ISO 8133 rod clevis for M14 × 1.5 on the rod end (38 mm from its face to the pin, 40
   wide, 30 high with its end rounded round the pin, a 20 mm slot 19 mm deep from the pin, Ø 14 pin hole,
   tapped M14 × 1.5 to the slot), Ø 14 pins 45 mm long in both clevises, four tie rods Ø 8 from 16 mm
   inside the cap to 2 mm past their nuts, and M8 × 1 nuts (13 across flats, 6.8 high, chamfered at 30°
   from Ø 11.6) on the head. Mark the rod end and the clevis as M14 × 1.5 threads. With the cutaway on, take the top quarter
   that faces the viewer out of the tube, the head, the cap, the gland and its seals, and leave out the
   tie rod and nut in it.

5. Finish it: paint the outside of the tube, head, cap and rod clevis gentian blue (RAL 5010) and keep every
   machined face bare steel (bores, ports, holes, slots and the cut faces); the rod hard chrome, tie rods,
   nuts and pins zinc-plated, the gland bright steel, the seals black and the guide rings bronze-filled PTFE,
   each with its density. Add outputs measured from the geometry: the oil in the cap end and in the rod end
   of the bore (bore less piston, seals and rod, split at the piston seal's middle), the pin-to-pin length,
   the moving mass (piston with its seal and wear rings, rod and rod clevis, not the pin); and the push and pull forces at 160 bar and the rod's buckling safety at full extension
   (whole pin-to-pin length, pinned both ends, Euler above π √(2E/Re) and Johnson below, E 210 GPa, Re
   305 MPa).

6. Check it: both oil volumes against a closed form (the swept volume plus the piston's dead volume),
   pin to pin = 172 + stroke + extension + 38, the ports 73 + stroke apart, the buckling safety at least
   3.5, the push force within the rod clevis's 26.4 kN, and four tie rods, three with the cutaway. Export
   the cylinder without the cutaway as STEP. Give the document a title and description, check
   it at stroke 25 and 320, extension 0 and 100, cutaway on and off, and show me a picture from three
   quarters above.

## Acceptance

At stroke 200, extension 50, cutaway on, the result must have:

- fourteen visible bodies (tube, head, cap with clevis, gland, seals, guide ring, piston, piston seal, wear
  rings, rod, rod clevis, pins, tie rods, nuts) plus the hidden *Oil*; three tie rods and nuts with the
  cutaway and four without;
- pin to pin 510 mm, and 410 mm retracted, 610 mm extended;
- oil in the cap end 125.8 cm³ and in the rod end 64.2 cm³, each within 1 % (0.15 cm³ left at the end of
  each stroke; a full stroke out takes 251.3 cm³, back 128.2 cm³);
- push 20.1 kN and pull 10.3 kN at 160 bar; buckling safety 6.7;
- moving mass 1.89 kg within 2 %; with the cutaway off, the cylinder 6.08 kg within 2 %;
- every check passing, and the same at stroke 25 and 320, extended and retracted, cut away or not.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed, with one gap. Its cylinder has the same oil volumes (125.810 and 64.235 cm³, both against the closed
form), pin-to-pin length (510 mm), forces (20.106 and 10.254 kN), buckling safety (6.73; 4.3 by Euler at
stroke 320) and port spacing (258.05 mm) as this example, its seven checks pass at all eight corners of
stroke, extension and cutaway, and its piston, rod and head have this example's volumes to 0.01 %. Its moving
mass, 1.951 kg, counted the rod clevis's pin, which this example leaves to the load (1.89 kg): turn 6 now
names the parts. It drew every seal, ring, tie rod and nut as a body of its own (26 bodies) and selected the
machined faces with `madeBy` queries. About 306 steps, written by a Python generator.

