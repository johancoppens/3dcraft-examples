# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a DIN 950 spoked handwheel in grey cast iron as a parametric part, Ø 200 mm with a 20 mm
   bore by default. Put the standard's sizes in a table, one row per diameter d1, with the rim width b,
   the hub diameter d3, the hub length l1, the overall depth l2 (hub back face to rim front), the radius
   r of the handle, the number of spokes, the first and last bore offered and the catalogue weight in
   grams, plus the DIN 98 revolving handle (type E) each size takes: grip diameter and length, collar
   diameter and length, thread and its length:

   | d1 | b | d3 | l1 | l2 | r | spokes | bores | weight g | grip | grip length | collar | thread | thread length |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | 80 | 14 | 24 | 16 | 29 | 27 | 3 | 10–12 | 302 | 16 | 49 | 10 × 5.5 | M6 | 11 |
   | 100 | 15 | 26 | 17 | 33 | 36 | 3 | 10–12 | 506 | 16 | 49 | 10 × 5.5 | M6 | 11 |
   | 125 | 16 | 28 | 18 | 36 | 47 | 3 | 12–14 | 695 | 20 | 61 | 13 × 6 | M8 | 13 |
   | 140 | 17 | 30 | 19 | 39 | 52 | 3 | 14–16 | 930 | 20 | 61 | 13 × 6 | M8 | 13 |
   | 160 | 18 | 33 | 20 | 40 | 62 | 3 | 14–16 | 1081 | 25 | 75 | 16 × 8 | M10 | 14 |
   | 200 | 22 | 38 | 24 | 45 | 80 | 3 | 18–22 | 1920 | 25 | 75 | 16 × 8 | M10 | 14 |
   | 250 | 26 | 48 | 28 | 50 | 101 | 5 | 22–26 | 3794 | 32 | 95 | 20 × 10.5 | M12 | 21 |
   | 315 | 28 | 53 | 33 | 56 | 132 | 5 | 26–30 | 5900 | 32 | 95 | 20 × 10.5 | M12 | 21 |
   | 400 | 32 | 65 | 38 | 63 | 171 | 5 | 30–34 | 10000 | 32 | 95 | 20 × 10.5 | M12 | 21 |
   | 500 | 34 | 78 | 45 | 72 | 220 | 5 | 34–40 | 14800 | 32 | 95 | 20 × 10.5 | M12 | 21 |

   A second table holds the bores 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36 and 40 mm with
   their DIN 6885-1 hub keyway, width × depth over the bore: 3 × 1.4 for 10, 4 × 1.8 for 12, 5 × 2.3 for
   14 and 16, 6 × 2.8 for 18 to 22, 8 × 3.3 for 24 to 30, 10 × 3.3 for 32 to 36 and 12 × 3.3 for 40.
   Make the diameter a choice from the first table and the bore a choice from the second, limited to the
   diameter's own bores. Every size should come from the tables.

2. The wheel's axis is vertical, the hub's back face at the bottom. The hub is a cone d3 across at its
   front face, drafted 2° narrower toward the back over its length l1, with the outer edges of both end
   faces chamfered by 0.04 d3 and the bore chamfered 0.05 d2 at both ends. The rim is a ring of round
   section, b across, its outside at d1 and its crown at l2. The handle sits on a cast lug on the rim's
   inside, its axis at r from the wheel's axis and halfway between two spokes, kept inside the rim's
   turned envelope: a barrel 0.6 times the collar's diameter in radius at the rim's mid-plane (its sides
   curved with a radius of 2 b), from 0.15 b below the rim's back to 0.05 b below the crown. Join it to
   the rim; spot-face its seat 0.15 b below the crown, half a root-fillet radius wider than the lug (the
   cutter notches the edge of the crown), and drill it through at the tap drill; then round the lug into
   the rim and at its foot with half the spokes' root radius (below).

3. The spokes are oval: 0.5 b thick and 0.65 × π × d3 / (number of spokes) wide, drawn as six tangent
   arcs: on each side an edge arc of 0.35 times the thickness, split at the widest line, and a top and a
   bottom arc joining them. Each spoke's centre line starts inside the hub wall, runs out level at a
   height of l1 less the hub chamfer, half the thickness and 1.2 root-fillet radii, bends up 1.5
   root-fillet radii outside the hub over a radius of 0.4 times the remaining run to the centre of the
   rim's section, and runs straight into that centre. Sweep the section along it, repeat it round the axis
   for the table's number of spokes with the boss halfway between two of them, join hub, spokes and rim,
   and round every spoke's root at the hub and at the rim with 0.3 times the spoke's thickness (the
   large sizes have five spokes: round theirs too).

4. Machine it: mark the boss's hole as the table's ISO metric thread for the thread length, and cut the
   keyway right through the hub, in line with the handle. Then add the handle as its own part: a stud at
   the thread's minor diameter in the hole, the collar on the spot face, and an olive-shaped grip of
   the table's diameter and length, narrow at its foot and ending in a blunt dome.

5. Finish: grey cast iron at 7200 kg/m³ painted a satin machine green; the rim turned on its outside
   where a lathe can reach and polished bright all round, and the hub's end faces, chamfers and bore, the
   keyway, the spot face and the hole left bright. The handle is zinc-plated steel. Give me the masses of
   the casting and of the handle. It is moulded in a two-part mould with a dished, profiled joint along
   the spokes' widest line (a coped joint or a follow board), so the spokes need no draft there; the hub
   is drafted toward the drag.

6. Add checks: the area of a section through the hub below the spokes (halfway between the back chamfer
   and the lowest point of the root fillets) against its closed form from the cone, the bore and the
   keyway; the wheel's diameter d1 and overall depth l2; the hub length l1; the keyway width; the number
   of spokes; the hub's draft at least 1° toward its back; the spokes' faces above their widest line releasing upward and
   those below it downward; and the casting's weight within 15 % of the table's weight. Give the document
   a title and description, run a check of the whole document, and show me a picture from three-quarters
   above.

## Acceptance

At Ø 200 mm with the 20 mm bore the result must have:

- a casting of volume 276 404 mm³ within 1 % (mass 1.990 kg in grey cast iron) and a separate handle;
- three oval spokes that climb from the hub to the rim, rounded at every root;
- a hub 24 mm long, an outside diameter of 200 mm, a rim 22 mm across with its crown at 45 mm;
- a hub cone drafted 2° toward its back face;
- a 6 mm keyway 22.8 mm from its floor to the far side of the bore;
- a lug at 80 mm from the axis between two spokes, nothing of it above the rim's crown, its seat
  spot-faced 3.3 mm below the crown and drilled through for M10, with the handle's Ø25 grip and its tip
  about 80 mm in front of the rim's crown;
- every check passing, and the same at Ø 80 mm with a 10 mm bore and at Ø 500 mm with a 40 mm bore (five
  spokes).

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed, with one gap. Its wheel has the same diameter (199.999 mm), depth (44.99996 mm), section area
(715.87 mm² against the closed form) and masses (casting 1.990 kg, +3.6 % on the catalogue's 1.920 kg; handle
0.241 kg) as this example, its handle's stud ends where this one's does, and nine of its ten checks pass; its
check of the spokes' upper faces is not proven ([F-102](../../3DCRAFT-FEEDBACK.md#f-102)). It named the root
fillets' edges for three spokes only, so at the five-spoke sizes two spokes stayed sharp without any check
noticing; turn 3 now says so. It split the table's compound cells (bores, collar, thread) into numbers,
because a text cell cannot be used in an expression, and found that a choice whose labels are numbers must be
set by its row. About 130 steps.
