# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design an International One Metre radio-sailing yacht to the IOM Class Rules 2026, in millimetres, at a
   modelling tolerance of 0.02 mm. Put x along the hull from the bow (0) to the transom (1000 mm), y across, z up
   with the design waterline at z = 0. Keep the class limits as variables: hull length at most 1000 mm, draft 370
   to 420 mm and hull depth at most 60 mm with the boat floating in fresh water (1000 kg/m³), a boat weight of
   4000 g, a keel of 2200 to 2500 g, a rudder with its stock of at most 75 g, a keel no wider than 20 mm above its
   lowest 60 mm, and an elastomer bumper as the forward 10 mm of the hull. Two public parameters: the bulb mass
   (default 2300 g, 2100 to 2320 g in steps of 10 g) and the keel depth, the depth of the bulb's underside below
   the design waterline (default 415 mm, 375 to 418 mm).

2. Loft the hull through seven stations from a table. Each station is a section across the hull at x: a deck
   from sheer to sheer cambered by 6 % of the sheer half-breadth (a parabola), and below it one cubic B-spline
   given by its control points: the starboard sheer, a topside point, a bilge point, a keel point on the centre
   line, then the bilge, topside and sheer points mirrored to port.

   | x | sheer half-breadth | sheer height | topside half-breadth | topside height | bilge half-breadth | bilge height | keel height |
   |---|---|---|---|---|---|---|---|
   | 10 | 10 | 75 | 12 | 30 | 9 | −6 | −12 |
   | 120 | 40 | 66 | 45 | 15 | 24 | −26 | −38 |
   | 280 | 70 | 58 | 76 | 8 | 46 | −42 | −56 |
   | 450 | 82 | 53 | 87 | 5 | 56 | −46 | −58 |
   | 620 | 81 | 49 | 86 | 6 | 58 | −42 | −52 |
   | 790 | 72 | 46 | 77 | 10 | 54 | −22 | −30 |
   | 1000 | 55 | 43 | 58 | 18 | 46 | 2 | 0.5 |

   Add an eighth section at the bow for the bumper, at x = 0: each of station 1's numbers carried on along the
   straight line from station 2 through station 1 (one eleventh of their difference beyond station 1). Loft all
   eight into one closed, hidden envelope, and cut it at x = 10 mm: aft of the cut is the hull's form, forward of
   it the bumper, in black elastomer (1150 kg/m³), its nose rounded 3 mm round the sides and bottom. Make the
   hull, the deck and the transom 0.6 mm of glass/epoxy laminate (1800 kg/m³) laid behind the hull form's surface,
   three plates: the deck set inside the hull's sheer, the transom inside hull and deck, hull and deck ending on
   the plane x = 10 mm so no glass reaches into the bumper. Finish the hull in white gelcoat and paint the deck
   grey-blue. On the deck, as separate small parts sitting on its camber and sheer: at x = 350 mm a white acetal
   mast step, a 40 × 20 × 2 mm plate with rounded corners and a Ø 16 mm tube 10 mm tall bored 11.4 mm for an
   11 mm mast, with the class's deck limit mark, a black dot 6 mm across, on its plate forward of the tube; and at
   station 4 a black hatch cover 60 mm across and 1.5 mm thick, its top edge rounded 1 mm.

3. Now the keel. The bulb is lead (11340 kg/m³), a body of revolution with the NACA four-digit thickness form
   of Abbott and von Doenhoff as its radius, 42 mm in diameter, its axis 21 mm above the keel depth. Make its
   length follow the bulb mass in closed form (its volume is 25π times the diameter squared times the length
   times the integral of the square of the thickness polynomial), so the public mass sets it. The fin is solid
   carbon/epoxy (1600 kg/m³, as a variable), NACA 0007, its leading edge straight up at x = 443 mm, 90 mm in
   chord at station 4's keel (54 mm below the design waterline) tapering straight to 75 mm at its foot, which
   runs 3 mm into the top of the bulb; carry the taper up to a root section at z = 0. The bulb's thickest station
   (30 % of its length) sits under the middle of the foot. Cut the fin's top off where it meets the hull's
   outside. The rudder is solid carbon too, the same thickness form at 6.5 %, 81 mm in chord at z = 0 with its
   leading edge at x = 880 mm, tapering to 60 mm at its tip at z = −195 mm, the tip's leading edge 10 mm
   further aft, and cut off at the hull the same way.

4. Weigh the boat. Measure the masses and the centre of gravity of everything modelled, and add what is not: a
   rudder stock of 8 g at the rudder root's quarter chord on the design waterline, the rig at 300 g with its
   centre of gravity at x = 350 mm, z = 550 mm, and radio gear and fittings at 400 g at x = 420 mm, z = −30 mm.
   A corrector weight on the fin box (x 45 mm aft of the fin's leading edge, z = −45 mm) makes up the 4000 g.
   Give me the masses of the laminate, fin, bulb, rudder and keel, the corrector weight and the boat's centre of
   gravity as outputs.

5. Float it. The hidden envelope with the fin, bulb and rudder is what displaces the water. Find the waterline
   at 4000 g in fresh water, the draft, the waterline's length and beam, the metacentric height upright (KB plus
   the waterplane's moment over the displacement less KG) and the trim the boat settles at floating free. Then
   add checks: hull length, draft and hull depth against C.4.1 at that waterline; a corrector weight of at least
   0 g; the keel's and the rudder's mass against C.6.4; the fin at most 20 mm wide and the bulb at most 60 mm
   tall (E.4.1); the bumper 10 mm long at the waterline; the bulb's measured mass equal to the bulb mass within
   0.01 g; the fin's section halfway down equal to the NACA area for its chord there; a trim within a quarter of
   a degree; and a positive GM. Give the document a title and description, run a check of the whole document and
   show me a picture from high on the bow quarter, so the deck and the sheer show.

## Acceptance

At the defaults (bulb 2300 g, keel depth 415 mm) the result must have:

- a bulb 265.8 mm long and 2300.0 g; a fin of 168.8 g and a rudder of 65.5 g within 1 %; hull, deck, transom and
  bumper together 443.0 g within 2 %; a keel of 2468.8 g and a corrector weight of 315 g within 10 g;
- the waterline at 4 kg within 0.3 mm of 0.49 mm above the design waterline: a draft of 415.5 mm, a hull depth of
  54.5 mm, both within 0.3 mm; a waterline length of 994 mm within 5 mm (the transom sits just clear of the water,
  so the length moves with the waterline) and a waterline beam of 157.8 mm within 1 mm;
- a GM of 201.7 mm within 2 % and a trim within ±0.25°;
- every check passing, and the same at 2100 g with 375 mm and at 2320 g with 418 mm.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the five turns above:
passed. Its yacht has the same bulb (2300.0007 g), waterline at 4 kg (0.50 mm above the design waterline),
draft (415.5 mm), hull depth (54.50 mm), waterline length (994.4 mm) and beam (157.8 mm), GM (201.5 mm,
`floatingGM` 201.48) and keel (2467.7 g) as this example, within the Acceptance; its corrector weight is
306.4 g (its own fittings' masses) and its 14 checks pass. Its laminate of 426.6 g leaves out the bumper.
It could not thicken the deck's cambered face by 8 mm for the mast step ("the freeform face has a pole …
where its normal and so its offset are not defined"; 7 mm works), so it typed the deck's height there from a
`measure.ray`, and `document.interference` of hull and bumper came back unknown
([F-130](../../3DCRAFT-FEEDBACK.md#f-130)). About 250 steps.

