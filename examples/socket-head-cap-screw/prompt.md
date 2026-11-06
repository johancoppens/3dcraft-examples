# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model an ISO 4762 socket head cap screw, M8 × 30, as a parametric part. Put the standard's
   dimensions for M3 to M12 in a table: thread diameter, coarse pitch, head diameter and height, socket
   width across flats (its minimum and maximum), minimum socket depth t, thread length b, minimum underhead
   radius, minimum bearing face diameter dw, the longest length that is threaded to the head, and the
   shortest and longest length of each size. Put the standard's series of lengths (5, 6, 8, 10, 12, 16, 20
   … 120 mm) in a second table. Make the size a choice from the first table and the length a choice from
   the second, limited to the size's own lengths. Every dimension of the screw should come from the tables.

2. Build the body as one revolved half section: the shank at the nominal diameter with a 45° tip chamfer
   down to just below the thread's minor diameter (ISO 4753), the cylindrical head, and a 120° countersink
   at the socket's mouth. Then round the corner under the head with the standard's radius, the top edge of
   the head with about 0.08 times the diameter, and the bearing edge a little, keeping the bearing face
   wider than dw.

3. Make the socket the way it is cold headed: a hexagon punch, the middle of the standard's width band
   across flats, with a 120° conical point that starts at the hexagon's corners at depth t; subtract it from
   the head. Then cut a real, modelled ISO metric coarse thread from the tip, not a cosmetic one: as long as
   the standard's thread length b, or, for the lengths the standard threads to the head, up to two pitches
   under the head.

4. Make it black-oxide steel: steel for its density, with a dark, satin, non-metallic finish. Add outputs
   for its volume, the volume under the head and its mass in grams.

5. Add checks: the volume of the head (everything above the bearing face) worked out in closed form, the
   threaded shank against the ISO 68-1 basic thread profile within one pitch of groove, the socket's width
   across flats within the standard's band, and the head's height. Give the document a title and
   description, run a check of the whole document,
   and show me a picture from three-quarters above.

## Acceptance

At M8 × 30 the result must have:

- one body, volume 2161 mm³ within 1 % (mass 17.0 g in steel);
- a hexagon socket between 6.02 and 6.14 mm across flats, at least 4 mm deep at full width, with a conical
  bottom;
- a modelled thread (a grooved shank, not a smooth one) of pitch 1.25 mm;
- an overall length of 38 mm and a head of Ø 13 × 8 mm;
- tables with the seven sizes and the standard's lengths, and Size and Length as choice parameters, Length
  limited to the size's lengths (M8: 12 to 80 mm);
- every check passing, and the same at M4 × 20 and M12 × 60.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the five turns above:
passed. Its screw checks itself with 9 assertions; at M8 × 30 it has a volume of 2163.3 mm³ (0.12 % from
this example's), a socket 6.06 mm across flats, a 13 × 8 mm head and a modelled thread, and its Length is
limited to each size's lengths. It took the table's values from memory, so check them against the standard,
and at M3 it had to deepen the tip chamfer to get the thread cut (F-006).

