# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a four-blade fixed-pitch ship propeller of the Wageningen B-series, a B4-55: diameter
   600 mm, pitch ratio P/D 0.8 with the same pitch at every radius, 15° rake aft, right-handed, in
   millimetres with a modelling tolerance of 0.05 mm. Make the diameter (500 to 800 mm), the pitch ratio
   (0.6 to 1.2) and the expanded area ratio (0.40, 0.55 or 0.70) parameters. Put the series' geometry from
   Oosterveld and van Oossanen (1975), Table 1, in a table, one row per r/R from 0.2 to 0.9: the chord
   factor c·Z/(D·AE/A0) = 1.662, 1.882, 2.050, 2.152, 2.187, 2.144, 1.970, 1.582; a/c (leading edge to
   generator line) = 0.617, 0.613, 0.601, 0.586, 0.561, 0.524, 0.463, 0.351; b/c (leading edge to the
   thickest point) = 0.350, 0.350, 0.351, 0.355, 0.389, 0.443, 0.479, 0.500; and the thickness
   t/D = A − B·Z with A = 0.0526, 0.0464, 0.0402, 0.0340, 0.0278, 0.0216, 0.0154, 0.0092 and
   B = 0.0040, 0.0035, 0.0030, 0.0025, 0.0020, 0.0015, 0.0010, 0.0005. The tip, r/R 1.0, is 0.0030 D thick.

2. Add the series' section ordinates (Tables 2 and 3 of the paper) to the table. P runs from the thickest
   point (0) to the leading edge (+1) and to the trailing edge (−1). With an edge thickness te = 0.0030 D,
   the back lies at (V1 + V2)·(t − te) + te and the face at V1·(t − te) above the pitch line. Per row
   (0.2 R to 0.9 R):
   - V1 at P = −1, −0.95, −0.8, −0.6, −0.4: 0.2 R .2826 .2630 .1967 .1207 .0592; 0.3 R .2306 .2040 .1333
     .0623 .0202; 0.4 R .1467 .1200 .0630 .0214 .0044; 0.5 R .0522 .0420 .0190 .0040 0; zero from 0.6 R.
   - V1 at P = 0.4, 0.6, 0.8, 0.95, 1: 0.2 R .0304 .0804 .1685 .2821 .3560; 0.3 R .0148 .0503 .1191 .2186
     .2923; 0.4 R .0033 .0189 .0637 .1467 .2181; 0.5 R 0 .0034 .0211 .0778 .1278; 0.6 R 0 0 .0006 .0169
     .0382; zero from 0.7 R.
   - V2 at P = −0.95, −0.8, −0.4: 0.2 R .0640 .3060 .7984; 0.3 R .0800 .3360 .8265; 0.4 R .0905 .3500
     .8415; 0.5 R .0950 .3569 .8456; 0.6 R .0965 .3585 .8426; from 0.7 R .0975 .36 .84.
   - V2 at P = 0.4, 0.8, 0.95: 0.2 R .8875 .4777 .1560; 0.3 R .8920 .5130 .1890; 0.4 R .8933 .5220 .1935;
     0.5 R .8880 .5039 .1750; 0.6 R .8790 .4620 .1485; 0.7 R .8660 .4140 .1240; 0.8 R .8520 .3765 .1050;
     0.9 R .8400 .36 .0975.
   V1 is 0 and V2 is 1 at P = 0, and V2 is 0 at both edges.

3. Build one blade as a loft through expanded sections. Each section lies on a plane tangent to the
   cylinder of its radius r: through the point on the generator line, which is raked 15° aft from the
   propeller plane, with its chord turned from the plane of rotation by the pitch angle atan(P / 2πr),
   the leading edge forward and the back towards the bow. Draw each section as a closed smooth spline
   through the trailing edge, the back at P = −0.95, −0.8, −0.4, 0, 0.4, 0.8, 0.95, the leading edge, and
   the face at P = 0.95, 0.6, 0, −0.6, −0.95, with both edges rounded off half an edge thickness beyond
   the chord's ends. Besides the eight rows, add a section in the hub at 0.75 of the hub's radius (the
   0.2 R section scaled down just enough to stay 2 mm inside the hub: turned to the pitch angle there,
   its trailing part, (1 − a/c)·c plus an edge thickness, reaches across the blade by that length × cos
   of the angle plus its thickness × sin of it; scale it so that this reach is √(r_h² − r²) − 2 mm),
   one at 0.975 R (chord factor 0.791,
   the 0.9 R outline continued as a parabola, c ∝ √(1 − r/R); thickness falling linearly from 0.9 R to
   0.0030 D at the tip; the 0.9 R ordinates), and a small rounded tip at R, 4 edge thicknesses long and
   one thick. Pattern the blade four times round the shaft axis.

4. Make the hub as one revolved half section, Ø D/6 at its aft end (the series' boss: the chord factors
   integrate to π/2 from r/R = 1/6), widening forward at a 2° draft. Make it long enough that the 0.2 R
   section's full chord and thickness, turned to the pitch angle at 0.75 of the hub radius, stay inside
   it by the end rounds and 5 mm at both ends. Bore it to a 1:10 taper for a 50 mm shaft (ISO 4566):
   120 mm long, from Ø 50 to Ø 38 mm at the aft face, behind a relief counterbore of Ø 56 mm (3 mm clear of
   the shaft) at least 15 mm deep. Round the hub's outer ends with D/96, chamfer the bore's aft mouth and
   the counterbore's mouth 1.5 mm, and slot a keyway along the taper for a DIN 6885 key 14 × 9: 14 mm
   wide, 3.8 mm deep in the hub. Join the blades to the hub; keep a copy of the hub and of one blade,
   hidden, for measuring.

5. It is cast in nickel-aluminium bronze CuAl10Fe5Ni5-C (CC333G), 7.6 g/cm³, and polished: a warm bronze,
   fully metallic, glossy. Add outputs for the mass, for the expanded area ratio measured on the expanded
   blade outline drawn from the table (from the hub's radius to the tip), and for how much the blade root
   narrows at the hub (section area and least second moment there against 0.2 R). Add checks: the
   expanded area ratio within 2 % of the chosen one, four blades, the blade reaching from its root
   section to exactly the diameter, the section at 0.7 R within 2 % of the area of the series'
   ordinates, the mass within 3 % of the hub and four blades from the series' section areas, the hub's
   cuts at both ends in closed form, the boss's draft of at least 2° pulled aft, and the centre of mass
   within 0.25 mm of the shaft axis. Give the document a title and description, run a check of the whole
   document, and show me a picture from low at three-quarters, no blade facing the camera flat.

## Acceptance

At the defaults (D 600 mm, P/D 0.8, B4-55) the result must have:

- one visible body, the propeller, of 19.23 kg in nickel-aluminium bronze within 2 %;
- four blades reaching exactly to Ø 600 mm, an expanded area ratio of 0.549 (0.55 within 2 %), and a
  section at 0.7 R of 1227 mm² (the series' ordinates give 1229 mm²);
- a hub Ø 100 mm at its aft end with a 2° draft, 158.5 mm long, bored Ø 50 to Ø 38 mm over 120 mm behind
  a Ø 56 mm counterbore 38.5 mm deep, with a 14 mm keyway 3.8 mm deep;
- the root at the hub about 14 % smaller in section than at 0.2 R, and the centre of mass 0.066 mm off
  the axis;
- every check passing, and the same at D 500 mm, P/D 1.2, B4-40 and at D 800 mm, P/D 0.6, B4-70.

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the five turns above:
passed at the defaults, with gaps. Its propeller has the same expanded area ratio (0.5492), section at 0.7 R
(1226 mm² against the ordinates' 1227), four blades to Ø 600 mm and a 2.000° boss draft as this example,
its mass is 19.08 kg (−0.8 %) and its hub cuts match their closed forms. It read "scaled just enough to stay
2 mm inside the hub" without the section's thickness, so its root section was not scaled at all (the root
1 % smaller than at 0.2 R, not 14 %) and its hub came out 155.3 mm long: turn 3 now gives the reach. Its
union of blades and hub was refused at several points of the range (P/D 1.0, B4-40, B4-70: "edge 35 is
3.9 mm away from the surface of face 15", as [F-124](../../3DCRAFT-FEEDBACK.md#f-124)), and so was a
section of its blade near 0.7 R. About 314 steps, written by a Python generator.

