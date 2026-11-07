# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's design a steel spiral staircase with oak treads for a house, to DIN 18065, as a parametric model
   in millimetres. Two public parameters: the floor-to-floor height (default 2800 mm, 2400 to 3200 mm in
   steps of 50 mm) and the outside diameter of the treads (default 1600 mm, 1400 to 2000 mm in steps of
   100 mm). Work out the stair from them with formulas:
   - Treads are 40 mm thick. Split the height into the largest number of equal risers whose rise is still at
     least (2000 mm + 40 mm) / 11, so that with twelve treads to a full turn there is 2000 mm of headroom
     under the tread a turn above. The landing is the top step, so there is one tread less than risers.
   - The handrail is a 42.4 mm tube whose centre runs 30 mm inside the treads' edge. The usable width runs
     from the radius where the going is 50 mm out to the handrail's inside. The walking area is the band from
     50 % to 70 % of the usable width out from its inner edge, and the walking line runs in its middle, at
     60 %.
   - Use twelve treads to a turn, or more on a wide stair: the whole number of treads per turn that brings
     the going at the walking line nearest to 630 mm less two rises. (With the inner edge at 50 mm of going,
     the going there is 20 mm plus 0.6 times the handrail's inside radius times the tread angle.)
   - The landing is as many tread angles wide as keeps 2000 mm of headroom over the treads below it, at most
     90°.

2. The central column is an EN 10220 tube, 114.3 × 4.0 mm, standing 930 mm above the upper floor, closed by
   an 8 mm disc welded flush into its top (nothing wider than the tube, so parts slide over it), its top
   edge rounded 3 mm. It stands on a solid Ø 300 × 15 mm base plate with a 3 mm chamfer on its top edge and
   four Ø 18 mm anchor holes on a Ø 230 mm circle. Make the column and plate one revolved section.

3. Each tread is a sector of solid 40 mm European oak from 3 mm outside its collar (below) out to the
   outside radius, spanning the tread angle plus a nosing overlap that is 30 mm at the walking line, with
   all eight edges of its top and bottom rounded 3 mm. The first tread's nosing lies along the x axis at one
   rise up, and the treads turn counter-clockwise as they rise. Each sits on a steel carrier: a
   collar, 100 mm of EN 10220 139.7 × 12.5 mm tube bored to Ø 115.3 mm, its outer edges chamfered 2 mm, top
   level with the tread's underside; and a T-section bracket under the middle of the tread, a 60 × 8 mm flat
   under the tread on a 10 mm blade, 100 mm deep overall at the collar and 30 mm at its end, 80 mm inside
   the edge, the blade's bottom corner rounded R10. Drill the flat for four Ø 7 mm screws, 20 mm either side
   of the blade, at a third and two thirds of its length. Between the collars, and from the base plate to
   the first one, put spacer tubes 139.7 × 6.3 mm, each centred on the column by a 10 mm ring bored Ø 115.3
   mm in each end (one revolved section). Repeat tread and carrier up the stair with a screw pattern (each
   copy turned one tread angle and raised one rise), and the spacers with a straight one.

4. Now the railing. Sweep the handrail, a 42.4 × 2.6 mm tube, along a helix that keeps its top 900 mm above
   the nosings, from the first nosing to the landing's front edge, and close both ends with a 3 mm plug
   centred on the end. Give each tread as many Ø 16 mm round bar balusters, evenly spaced on the handrail's
   line, as keep every gap under 100 mm all the way up. They pass through Ø 17 mm holes in the tread, stand
   20 mm out below it, and are cut square to the handrail's slope 0.5 mm under it.

5. The landing is a 40 mm oak sector whose front edge is where a fifteenth tread's would be (the tread
   angle times the number of treads round from the x axis), its top at the floor-to-floor height, running
   round by the landing angle; its edges rounded 3 mm like the treads. Carry it on a collar and T-bracket
   like a tread's under its first tread angle, the collar 8 mm taller, and on a second carrier: a 60 × 8 mm
   flat along the guard line (below), let into a groove in the landing's underside so it costs no
   headroom, from the collar to under the post. Along the landing's back edge put a guard on a line 45 mm
   inside it: a 60 × 8 mm base flat on the landing from 10 mm outside the collar to the far side of the
   post, Ø 16 mm balusters evenly spaced from the column to a 48.3 × 2.6 mm tube post 50 mm in from the
   outside edge, every gap (also from the column) under 100 mm, and a 42.4 × 2.6 mm tube rail with its top
   900 mm above the landing, welded to the column with its end coped 0.5 mm clear of it. Let the post
   stand 15 mm above the rail, capped with a 4 mm disc and its top edge rounded 5 mm.

6. Make the steel anthracite powder coat (steel for its density, RAL 7016, non-metallic, satin) and the
   treads and landing oiled oak with the grain running out from the column. Then add checks: one tread per
   riser below the landing; the first tread one rise up, the last one rise below the landing and the
   landing at the floor-to-floor height; rise, going at the walking line and 2 rises + going against DIN
   18065's limits for a stair that is not the required one in a house; the usable width at least 500 mm;
   2000 mm tall gauges standing on the floor and on every tread over the walking area that touch nothing
   above them; no part running into another; the baluster gaps on the stair and on the landing and the
   gap from the column to the first landing baluster at most 100 mm; a tread's plan area and the treads'
   oak volume worked out in closed form; and the column tube's mass per metre within 0.5 % of EN 10220's
   10.9 kg/m. Hide the gauges, give the document a title and description, run a check of the whole
   document and show me a picture from above the landing's side.

## Acceptance

At the defaults (2800 mm, Ø 1600 mm) the result must have:

- 15 risers of 186.67 mm: 14 treads and the landing; 12 treads to a turn (30°), the landing 60° wide;
- the walking line at 487.5 mm from the axis, a going of 255.2 mm there and 2 s + a = 628.6 mm; a usable
  width of 653.3 mm; a headroom of 2013.3 mm behind each nosing;
- four balusters per tread (56 on the stair), 84.7 mm apart in the clear;
- oak 87.2 kg and steel 341.0 kg within 1 % (oak at 750 kg/m³, steel at 7850 kg/m³; each part solid or a
  tube as said above);
- every check passing, and the same at 2400 mm with Ø 2000 mm and at 3200 mm with Ø 1400 mm.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its stair has the same 15 risers of 186.667 mm, 14 treads at 30° and a 60° landing, the same walking
line (487.5 mm), going (255.24 mm), step measure (628.58 mm) and usable width (653.3 mm), four balusters per
tread 84.72 mm apart, the column at 10.88 kg/m and carriers of 128.5 kg, as this example; its checks pass at
five points of the range and `document.interference` finds no overlap. Two refusals it worked round: joining
the 3 mm end plug to the swept rail ("an imprinted curve that does not fit the edges it should coincide
with", at the edge of tolerance; it made the plug 0.1 mm larger), and the landing's 3 mm round-over at
3200 mm × Ø 1400 mm, where the landing ends at exactly 180° (as [F-113](../../3DCRAFT-FEEDBACK.md#f-113); it
sketched the landing at 0° and turned it). About 311 steps, written by a Python generator.

