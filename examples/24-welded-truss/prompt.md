# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a welded steel truss as a parametric part: a parallel-chord Warren truss (diagonals only,
   no verticals) of cold-formed circular hollow sections in S355J2H, EN 10219-2 sizes, both chords the
   same section. Span 6000 mm between the top chord's end nodes, depth 600 mm between the chord axes, six
   panels along the top chord with two diagonals each. Put four section pairs in a table, each with its
   mass per metre: chords 88.9 × 5.0 (10.3 kg/m) with diagonals 48.3 × 3.2 (3.56), 114.3 × 6.3 (16.8)
   with 60.3 × 4.0 (5.55), 139.7 × 6.3 (20.7) with 76.1 × 4.0 (7.11), 168.3 × 6.3 (25.2) with
   88.9 × 5.0 (10.3). Make these public parameters: Span, 4800 to 7200 mm in steps of 300; Depth, from a
   fourteenth to an eighth of the span in steps of 50 mm; Panels, 4 to 8 but limited so that diagonals
   set out on the chord axes lean between 30° and 55°; Section pair, a choice from the table, the second
   row by default. Work at a modelling tolerance of 0.001 mm.

2. Size the diagonals' welds for full strength: throat a ≥ √2 × 0.9 × (355 / 470) × 1.25 × t of the
   diagonal (the directional method with the section's own tensile strength), rounded up to 0.5 mm
   (a5 here); the welds will be drawn with equal legs of 2a (10 mm here). Set out gap K-joints: every
   diagonal's axis passes through the middle of its half panel at half the depth. Put the diagonals on the
   chord axes, unless that leaves less than 2 (t + 2a) between the heels of two diagonals on a chord; then
   turn them about that middle point until the gap is exactly that. Tell me the diagonals' angle, the gap
   and the eccentricity of the nodes.

3. Build the members. Both chords are tubes. The top chord runs one chord diameter past each end node;
   the bottom chord runs past its outermost nodes by half the gap, plus the diagonal's diameter divided
   by the sine of its angle, plus half a chord diameter. Make one diagonal as a tube square to its axis,
   from the bottom chord's axis to the top chord's, and cope both ends by subtracting solid cylinders of
   the chords' outside diameter, so it sits on the chords with no gap. Mirror it for the falling diagonal
   and repeat the pair along the span. Lay the coped diagonal's outside flat as a coping template,
   hide it, and keep it for a DXF export.

4. Now the plates and the welds, each weld a body of its own. Round each end of every diagonal, a
   flat-faced fillet weld with equal legs of 2a (10 mm) on the chord and on the diagonal. At the top
   chord's ends, 15 mm end plates, centred on the chord: four 18 mm holes for M16 bolts at the corners of
   a bolt square of the chord's diameter plus two hole diameters, rounded up to 5 mm (155 mm); the plate
   is the bolt square plus three hole diameters, rounded up to 10 mm (210 × 210 mm). Round every edge of
   the plates 2 mm, and weld each to the chord all round with a full-strength fillet weld on the chord
   wall, by the same rule (a8, legs a√2). Close the bottom chord's ends with 8 mm discs of the chord's
   diameter plus two seal-weld legs each side, rounded up to 1 mm (132 mm), rims rounded 2 mm,
   seal-welded all round with a3 (legs 3√2 mm).

5. Make everything steel, 7850 kg/m³, in a matt red-oxide primer. Give me a bar list as outputs: the cut
   lengths of the two chords, the number of diagonals, and two lengths of a diagonal's blank before
   coping: sawn with both ends mitred parallel to the chords, measured along any line of the tube, and
   sawn square, from toe to toe along its axis. Add the nominal mass of the tube to buy (the mitred blanks
   nested end to end), the steel mass, and the weld metal's volume and mass.

6. Add checks: the volumes of the chords, the coped diagonals, the plates and the plate welds in closed
   form (a tube cut by a cylinder of radius R at each end: (h A − 2 ∫∫ √(R² − w²) dA) / sin θ over its
   annulus); two diagonals per panel and a weld at each end; the gap between two diagonals measured; the
   EN 1993-1-8 validity range for CHS gap K-joints (at least 30° to the chords and between the diagonals,
   gap at least t1 + t2, eccentricity between −0.55 and 0.25 chord diameters, 0.2 ≤ d1/d0 ≤ 1,
   10 ≤ d0/t0 ≤ 50, d1/t1 ≤ 50, Class 2 sections); the weld throats against the full-strength rule; the
   masses per metre against the table; the bolt holes' edge distance against 1.2 times the hole. Give the
   document a title and description, run a check of the whole document, and show me a picture from
   three-quarters above, looking along the truss from one end.

## Acceptance

At the defaults (6000 mm span, 600 mm deep, six panels, 114.3 × 6.3 chords with 60.3 × 4.0 diagonals) the
result must have:

- diagonals at 50.93° to the chords, a 28.0 mm gap at every K-joint and the nodes 7.93 mm eccentric
  (away from the diagonals);
- a top chord of 6228.6 mm (13 313 879 mm³ within 1 %), a bottom chord of 5297.6 mm (11 323 920 mm³), and
  12 identical diagonals from blanks of 647.8 mm on every line with both ends mitred parallel to the
  chords (674.6 mm square-cut, toe to toe), coped at both ends to the chords' outside (5 391 546 mm³
  together, within 1 %);
- two end plates (1 289 498 mm³ together) and two cap plates (217 542 mm³), and a steel mass of 247.6 kg
  within 1 %;
- 24 diagonal weld beads with 10 mm legs, 8.0 mm of bare chord between the weld toes in each gap, and
  about 286 cm³ of weld metal in all;
- a coping template that is one closed outline: a band 189.4 mm round (π × 60.3) with a cope at each end;
- every check passing, and the same at 7200 mm, 600 mm deep, seven panels and 139.7 × 6.3 chords.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above: passed.
Its truss has the same set-out as this example (diagonals at 50.93°, a 28.0 mm gap at every K-joint, the
nodes 7.93 mm eccentric), the same chords (6228.6 and 5297.6 mm), 247.55 kg of members (247.56 here) and
2.243 kg of weld metal, with its own 36 assertions passing at the defaults and at the other section pairs. It
read "the longest line along the tube" as the coped diagonal's length from toe to toe (674.6 mm, a
square-cut blank) where this example meant a blank mitred at both ends (647.8 mm); that showed the README's
hand route sawing 25 mm short, and turn 5 now asks for both lengths. It met two kernel limits: a 2 mm round
on a disc rim of 93 mm radius or more is refused ([F-147](../../3DCRAFT-FEEDBACK.md#f-147)), and three of
its weld bodies could not be checked against the diagonals
([F-149](../../3DCRAFT-FEEDBACK.md#f-149)). About 216 steps, written as a script.
