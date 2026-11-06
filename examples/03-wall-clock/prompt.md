# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design a wall clock to laser cut and engrave from 6 mm birch plywood, as a parametric model in
   millimetres. Public parameters: the dial diameter (200 to 360 mm in steps of 10, default 300: a
   standard movement drives a minute hand of about 160 mm at most), the numerals as a choice of Roman or
   Arabic, and the time the hands show as an hour (1 to 12, default 10) and a minute (0 to 59, default
   10). Lay the dial flat with its front facing up and twelve o'clock along +y. It takes a common quartz
   sweep movement, 56 × 56 × 16 mm, with a 5/16 inch threaded bushing, so cut an 8.5 mm hole in the
   centre. Round the front edge over by 2 mm.

2. Engrave the minute track 0.4 mm deep, scaled to the diameter: 60 radial ticks ending at 0.45 times the
   diameter from the centre; the 48 minute ticks 0.025 D long and 0.005 D wide, the 12 hour ticks 0.06 D
   long and 0.013 D wide. Use patterns round the centre rather than drawing ticks one by one.

3. Inside the track, engrave the numerals 0.07 D tall, a gap of 0.02 D inside the hour ticks. Roman
   numerals (with IIII for four) follow a circle, each centred on its hour with its base towards the
   centre, as on a classic dial; Arabic numerals stand upright. Build both and let the numerals choice
   switch between them. Draw the engraving as burnt wood, dark brown, and the laser-cut rim dark too.

4. Add the hands as 0.5 mm black steel: a minute hand from the centre to the middle of the minute track
   and an hour hand stopping 0.02 D short of the numerals (a quarter of the numeral height shorter again
   with Arabic numerals, whose 10 and 11 reach further in), both tapering to a point from a round hub
   (0.02 D in radius) with a short tail of 0.05 D, the hour hand wider. The hour hand sits 4 mm above the
   dial and the minute hand 6.5 mm. Turn them to the time: 6° per minute for the minute hand, 30° per hour
   plus half a degree per minute for the hour hand. Show the movement's bushing from the back of the dial
   up to the hour hand, a 3.5 mm minute shaft from the hour hand to the minute hand, and a small rounded
   cap nut on the minute hand.

5. On the back, a keyhole hanger glued up from three plates of the same plywood, 32 mm wide with round
   ends, 0.3 D above the centre: the wall-side plate has a keyhole (an 11 mm hole and a 6 mm slot 10 mm
   upwards), the two spacers a 13 mm slot for the screw head. Add a foot as deep, three of the same
   spacers as far below the centre, so the clock hangs square. Make the dial and the hanger birch plywood
   (680 kg/m³) with a light birch look.

6. Add checks: the dial's volume below the middle of the round-over worked out in closed form, 60 ticks,
   12 numerals, the hour hand keeping at least half the numeral gap from the numerals as seen from the
   front, each hand pointing at the time, the keyhole slot and every hole at least the sheet thickness,
   the hanger and the foot deeper than the movement and the hanger clear of it, and the shaft hole
   clearing the bushing. Give the document a title and description, check the whole document, export the
   dial's cut line as DXF, each engraving as SVG and the hanger and foot plates as DXF, and show me the
   clock from the front, a little from the side.

## Acceptance

At the defaults (Ø 300 mm, Roman, 10:10) the result must have:

- a dial of Ø 300 × 6 mm with an 8.5 mm centre hole, volume 421 474 mm³ within 1 % (286.6 g in birch
  plywood at 680 kg/m³);
- 60 engraved ticks (48 minute and 12 hour ticks) and 12 Roman numerals, IIII for four, engraved 0.4 mm
  deep; with Arabic chosen, 12 upright Arabic numerals and no Roman ones;
- a minute hand 131 mm long pointing at 60° from twelve and an hour hand 84 mm long at 305° (78.75 mm with
  Arabic numerals);
- a hanger of three 6 mm plates, 18 mm deep, with a keyhole slot 6 mm wide, and a foot of three spacers as
  deep;
- every check passing, and the same at Ø 200 mm Arabic 12:59 and Ø 360 mm Roman 4:37.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its clock checks itself with 15 assertions, also at three other points of the range, and has a dial
of 421 474 mm³ and the same closed form, 353 063.706 mm³, as this example; its hands point within 0.05°. It
took 178 steps. It coloured the engravings by face names on a final always-active feature, since a face's
colour is lost when a later feature is switched off (F-048), and measured the hour hand's clearance seen from
the front through a hidden copy of the hand (F-049).

