# Build it with an AI

Paste these turns one at a time into a chat with an AI connected to 3DCraft (Help › Connect an AI agent).
Each turn says what you want, the way you would tell a colleague; the AI picks the commands.

## The conversation

1. Let's model a solitaire engagement ring in 18 ct yellow gold as a parametric part, in millimetres.
   Give it two public parameters: the ring size as ISO 8653 has it (the inner circumference in mm, whole
   sizes from 44 to 72, default 54) and the stone's weight in carats (0.25 to 2 ct in steps of 0.05,
   default 1). The finger runs along the y axis and the stone sits on top, its axis along z.

2. First the stone: a round brilliant cut to Tolkowsky's ideal. Table 53 % of the girdle diameter,
   measured to the corners of the table's octagon; crown angle 34.5° and pavilion angle 40.75°, both on
   the bezel and pavilion main facets; a girdle 3 % of the diameter thick where the bezels meet it; star
   facets reaching half way from the table's edge to the girdle; lower girdle facets reaching 75 % of the
   way from the girdle to the culet; a pointed culet, so 57 facets. Cut it from a cylinder, one plane per
   facet group through three of the facet's corners, repeated eight times round the axis, with the
   mirrored girdle facets made by mirroring. Size it from the carat: work out its volume in closed form
   as a number times the girdle radius cubed, and solve for the radius that weighs 0.2 g per carat at
   3.515 g/cm³.

3. Now the shank: a comfort-fit court band 1.7 mm thick and 2.2 mm wide, or 0.32 times the stone's
   diameter where that is wider, its section a four-centre oval with 0.4 mm radii at the edges, revolved
   about the finger axis, its inner crest exactly on the ring size's circumference.

4. The head is a four-prong basket with the prongs on the diagonals. The prong wire is 0.17 times the
   stone's diameter but at least 1 mm, and the prongs' centres lie on a circle whose radius is the
   girdle's plus a sixth of the wire, so a seat a third of the wire deep holds the girdle. Each side's two
   prongs are one wire bent in a U in a plane across the band, the U's bend a half circle whose bottom is
   centred on the band's outer surface. Round the tips with balls of the wire's diameter, centred on each
   prong's axis at the height where the crown meets the prong's inner face, so the ball's inner side just
   touches the crown. Add a gallery wire 0.6 times the prong wire but at least 0.8 mm, under the girdle,
   0.1 mm outside it and 0.1 mm below it, and round its joints with the prongs with a fifth of the prong
   wire. Set the stone so its culet is at least 0.5 mm above the band and the gallery's underside at
   least two of those fillet radii above where the U's bend begins: take the higher of the two. Cut the
   seats by subtracting the stone from the prongs, join the head to the band, and round the joints where
   the U-bottoms run into the band with a fifth of the prong wire too, for stones up to 1.2 ct.

5. Make the ring 18 ct yellow gold, 750 with equal silver and copper, 15.4 g/cm³, polished, and the stone
   a diamond of 3.515 g/cm³ that reads as a white faceted stone, its star and bezel facets visible. Give me outputs for the gold's mass in
   grams and the stone's diameter and depth.

6. Add checks: a hidden ISO ring gauge, a cylinder of the size's circumference on the finger axis, that
   touches the ring without overlapping it; the stone weighing its carat; 57 flat facets; the trade's
   weight estimate (diameter² × depth × 0.0061) within 3 % of the carat; the shank's volume below the
   finger axis by Pappus; the gallery at least 0.1 mm from the stone; the culet at least 0.5 mm above
   the shank; the thinner of the prong and gallery wires at least 0.8 mm, the casting minimum.
   Give the document a title and description, check the whole document, and show me a picture from
   three-quarters above.

## Acceptance

At size 54 and 1 ct the result must have:

- a stone of 57 flat facets and a girdle, 6.44 mm across within 0.5 % (6.437 mm), 4.01 mm deep
  (62.2 % of the diameter), weighing 0.2 g, volume 56.90 mm³;
- an inner diameter of 17.19 mm (circumference 54 mm), the ring gauge touching the ring;
- a shank whose half below the finger axis has a volume of 83.53 mm³ within 0.5 %;
- four prongs of 1.09 mm wire with ball tips, a gallery of 0.8 mm wire, the culet 0.68 mm above the
  shank and the table 6.39 mm above the finger;
- one gold body of about 3.06 g (within 5 %: the head's details vary), one diamond body;
- every check passing, and the same at size 44 with 0.25 ct (1 mm prongs) and at size 72 with 2 ct
  (a 2.6 mm shank).

## Tested

2026-11-07, Claude Sonnet 5.5 (medium effort) through `craft3d-cli`, given only the six turns above:
passed. Its ring has the same stone (57 facets, 6.437 mm across, 4.006 mm deep, 56.90 mm³, 0.2 g), shank
(83.53 mm³ below the finger axis), wires (prongs 1.095 mm, gallery 0.8 mm), culet clearance (0.684 mm) and
gold (3.056 g) as this example, and its nine checks pass over the carat range at size 54 and at four sizes.
It cut the facets with planar cutters on datum planes through three points, read the upper girdle facets'
and lower girdles' positions as this example does, and drew the stone opaque, as this one does. Its seat cut
was refused at 1.25 ct until it tightened the tolerance to 1e-7 mm
([F-109](../../3DCRAFT-FEEDBACK.md#f-109)). About 160 steps.

