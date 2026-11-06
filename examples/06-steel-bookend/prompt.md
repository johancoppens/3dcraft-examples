# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design a bookend as a sheet-metal part: laser cut from 2 mm DC01 cold-rolled steel and bent once,
   90°, on a press brake. Make the overall height (from the shelf to the top of the upright) and the width
   public parameters: height 180 mm, from 120 to 240 in steps of 10; width 120 mm, from 80 to 200 in steps
   of 10. The foot is height / √2 deep, measured outside. It is air bent in a V-die 8 times the thickness
   wide, so the inner bend radius is 16 % of that opening (2.56 mm); take the K-factor from DIN 6935,
   (0.65 + 0.5 log10(r / t)) / 2.

2. Make the foot the flat base, lying on the shelf, with its two front corners rounded R10, and bend the
   upright up from its back edge as one flange whose outline you draw yourself, so it can have its own
   shape: its two top corners rounded R15. So the outside of the bend lines up with the sizes, the foot's
   flat is the foot depth less r + t, and the upright's flat the height less r + t.

3. Cut an ogee-arch window in the upright, centred, of a fixed shape so it reads as an arch at every
   size: twice as tall as it is wide. Its height is the smaller of 0.8 × the width and 58 % of the
   upright's flat; its half-width is a quarter of its height. Its middle sits at 51 % of the upright's flat
   above the bend's tangent line. The sill has R6 corners; the straight sides stop 1.8 half-widths below
   the apex, where the arch springs. Draw each half of the arch as one cubic spline through four control
   points: from the top of its side; straight above it, 0.45 of the arch's height up; then 0.3 half-widths
   out from the centre line, 0.45 of the arch's height below the apex; ending at the apex on the centre
   line. All of it in formulas, so it follows the parameters.

4. Make it steel for its density, powder coated RAL 6004 blue green: a satin, non-metallic finish (around
   #0e4243). Add an output for its mass in grams, and export the flat pattern as a DXF.

5. Add checks: the overall height and the foot depth; the flat pattern's area in closed form (width times
   the flat length with the bend allowance, less the four corners and the window, the arch's halves by the
   area under a cubic Bézier); the folded volume from that area, corrected for the K-factor; the inner
   radius at least the thickness; the window at least 2.5 t + r from the bend; and that it can be bent on
   a press brake: an 88° punch with an R2 tip, its flanks rising 30 mm to a straight body 100 mm high, and
   an 88° V-die 16 mm wide with R2 shoulders. Give the document a
   title and description, run a check of the whole document, and show me a picture from the front, three
   quarters above, with the foot towards me.

## Acceptance

At the defaults (height 180 mm, width 120 mm) the result must have:

- one sheet-metal body with one bend of 90° up, inner radius 2.56 mm, K-factor 0.3518, bend allowance
  5.126 mm;
- an overall height of 180 mm and a foot 127.28 mm deep outside;
- a flat pattern 120 mm wide and 303.29 mm long with an area of 32 554 mm² within 1 %, and a volume of
  65 221 mm³ within 1 % (mass 512 g in steel);
- one window, an ogee arch 48 mm wide and 96 mm tall, 41.47 mm from the bend's tangent line;
- a DXF of the flat pattern with the outline and one bend line on separate layers;
- every check passing, and the same at height 120, width 200 mm and at height 240, width 80 mm.

## Tested

2026-11-06, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the five turns above:
passed, with nothing refused. Its bookend checks itself with 7 assertions, also at the four corners of the
range, and has a flat area of 32 605.73 mm² and a volume of 65 323.20 mm³ (0.16 % over this example's, from
reading the arch's spring point a little differently), r 2.56 mm, K 0.3518, the window 41.47 mm from the
bend, and a DXF of the flat pattern with its bend line.

