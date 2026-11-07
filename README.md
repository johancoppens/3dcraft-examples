# 3DCraft examples

Twenty-one models built in [3DCraft](https://github.com/johancoppens/3dcraft), the open-source parametric
CAD modeller built for AI, from simple to fairly complex: machine parts, sheet metal, 3D prints, laser and
CNC work, furniture, packaging, jewellery, architecture, boats and art. Every one is real (sized to the
standards of its trade), makeable (its process checks are part of the model), parametric (a few public
parameters to play with) and light (it opens in seconds).

Each example lives in its own numbered folder under [`examples/`](examples/), from simple to complex, with:

- **`<id>.3dcraft`**: the model; open it in 3DCraft.
- **`build.json`**: the 3DCraft commands that build it, step by step, ending with the checks that prove it.
- **`README.md`**: what it shows, the real thing behind it, how to make it.
- **`prompt.md`**: a conversation you can have with an AI connected to 3DCraft to build it yourself.
- **`exports/`**: files for the workshop (STEP, 3MF, DXF, SVG) where they make sense.

## Gallery

Ordered by difficulty (scored out of 10 by a reviewer). Work in progress: the list of what is planned is in
[`CATALOGUE.md`](CATALOGUE.md).

<!-- gallery:start -->
| | Example | Domain | Difficulty |
|---|---|---|---|
| <img src="examples/01-socket-head-cap-screw/preview.png" width="240" alt="Socket head cap screw"> | **[Socket head cap screw](examples/01-socket-head-cap-screw/)**<br>An ISO 4762 socket head cap screw, M3 to M12 in the standard's lengths, with a rolled thread, in black-oxide steel. | Machine building | 4/10 |
| <img src="examples/02-t-slot-profile/preview.png" width="240" alt="T-slot aluminium profile"> | **[T-slot aluminium profile](examples/02-t-slot-profile/)**<br>A 30 x 30 mm B-type aluminium profile with four 8 mm T-slots and a core bore tapped M8 at both ends, cut to length, in clear anodised EN AW-6063. | Machine building | 4/10 |
| <img src="examples/03-wall-clock/preview.png" width="240" alt="Plywood wall clock"> | **[Plywood wall clock](examples/03-wall-clock/)**<br>A Ø 300 mm wall clock laser cut and engraved from 6 mm birch plywood for a quartz sweep movement, Roman or Arabic numerals, a laminated keyhole hanger and foot at the back and black hands set to the time. | Laser cutting, art | 4/10 |
| <img src="examples/04-turned-bowl/preview.png" width="240" alt="Turned walnut bowl"> | **[Turned walnut bowl](examples/04-turned-bowl/)**<br>A face-grain serving bowl turned from a 10 × 4 inch walnut blank: an even 7 mm wall from a rounded rim to a foot ring with a dovetailed chuck recess, with its capacity in millilitres. | Woodturning | 4/10 |
| <img src="examples/05-hex-key-stand/preview.png" width="240" alt="Hex key stand"> | **[Hex key stand](examples/05-hex-key-stand/)**<br>A stepped desk stand for a metric hex key set to ISO 2936, 1.5 to 10 mm, printed in PLA without supports, sizes embossed in black. | 3D printing | 4/10 |
| <img src="examples/06-steel-bookend/preview.png" width="240" alt="Steel bookend"> | **[Steel bookend](examples/06-steel-bookend/)**<br>A bookend laser cut from 2 mm DC01 cold-rolled steel with an ogee-arch window, bent once on a press brake and powder coated deep teal. | Sheet metal | 3/10 |
| <img src="examples/07-v-block-pair/preview.png" width="240" alt="V-block pair with clamps"> | **[V-block pair with clamps](examples/07-v-block-pair/)**<br>A matched pair of hardened and ground 90° V-blocks, 45 × 40 × 35 mm, for shafts of 6 to 30 mm, with black-oxide U-clamps holding a ground test pin. | Toolmaking | 5/10 |
| <img src="examples/08-square-to-round-transition/preview.png" width="240" alt="Square-to-round transition"> | **[Square-to-round transition](examples/08-square-to-round-transition/)**<br>A four-piece transition from a 400 x 300 mm rectangular duct to a 250 mm round duct in 0.8 mm galvanised steel: flat triangles and developable cone corners with straight ends, one piece unfolded into the flat pattern cut four times, with a lapped collar, a P20 angle frame and a sealed spigot. | Sheet metal, HVAC | 7/10 |
| <img src="examples/09-mailer-box/preview.png" width="240" alt="Mailer box"> | **[Mailer box](examples/09-mailer-box/)**<br>A FEFCO 0427 mailer of single-wall E-flute kraft board, 200 × 150 × 60 mm inside, folded from its die-cut blank: rolled end walls locked by tabs, dust flaps and a tuck-in lid. | Packaging | 7/10 |
| <img src="examples/10-headphone-stand/preview.png" width="240" alt="Headphone stand"> | **[Headphone stand](examples/10-headphone-stand/)**<br>A one-piece headphone stand printed upright in PETG without supports: a slim lofted column flaring into a wide saddle curved like a headband, a swept cable hook, and a round base weighted by an embedded steel disc. | 3D printing, product design | 6/10 |
| <img src="examples/11-splayed-stool/preview.png" width="240" alt="Splayed-leg stool"> | **[Splayed-leg stool](examples/11-splayed-stool/)**<br>An oak sitting stool, Ø 340 mm seat at 450 mm, on four legs splayed and raked 10°, tenoned through the seat and wedged with walnut, with two shouldered side stretchers; proven in closed form and against the stool stability test of IS 5416-2. | Woodworking | 6/10 |
| <img src="examples/12-fpv-drone-frame/preview.png" width="240" alt="5-inch FPV drone frame"> | **[5-inch FPV drone frame](examples/12-fpv-drone-frame/)**<br>A true-X freestyle quadcopter frame for 5 to 5.3 inch props, CNC routed from 2 mm and 5 mm carbon fibre sheet, with purple anodised standoffs, a 30.5 mm stack, a cage for a 19 mm camera and real 5.1 x 4.3 x 3 props lofted at their pitch. | CNC, RC | 7/10 |
| <img src="examples/13-cast-handwheel/preview.png" width="240" alt="Cast handwheel"> | **[Cast handwheel](examples/13-cast-handwheel/)**<br>A DIN 950 spoked handwheel in grey cast iron, 80 to 500 mm, with cranked oval spokes, a turned and polished rim, a keyed bore and a DIN 98 revolving handle on a boss at the standard's radius, painted machine green. | Machine building | 6/10 |
| <img src="examples/14-solitaire-ring/preview.png" width="240" alt="Solitaire ring"> | **[Solitaire ring](examples/14-solitaire-ring/)**<br>An 18 ct yellow-gold solitaire in ISO 8653 ring sizes 44 to 72: a comfort-fit court shank and a four-prong basket head holding a round brilliant of 0.25 to 2 ct, cut to Tolkowsky's proportions and sized from its weight. | Jewellery | 6/10 |
| <img src="examples/15-hydraulic-cylinder/preview.png" width="240" alt="Hydraulic cylinder"> | **[Hydraulic cylinder](examples/15-hydraulic-cylinder/)**<br>A double-acting ISO 6020-2 tie-rod cylinder, bore 40, rod 28, with clevises at both ends, a rod that moves with a parameter and a cutaway that shows the piston, the seals and the gland. | Hydraulics | 8/10 |
| <img src="examples/16-spiral-staircase/preview.png" width="240" alt="Spiral staircase"> | **[Spiral staircase](examples/16-spiral-staircase/)**<br>A steel spiral staircase with oak treads, Ø 1600 mm and 2800 mm floor to floor, on a Ø 114.3 mm column, with a helical handrail and a landing, checked against DIN 18065. | Architecture, steel construction | 8/10 |
| <img src="examples/17-ship-propeller/preview.png" width="240" alt="Ship propeller"> | **[Ship propeller](examples/17-ship-propeller/)**<br>A four-blade Wageningen B4-55 ship propeller, Ø 600 mm, pitch ratio 0.8, 15° rake, its blades from the series' published tables, in polished nickel-aluminium bronze. | Marine | 8/10 |
| <img src="examples/18-guitar-body/preview.png" width="240" alt="Electric guitar body"> | **[Electric guitar body](examples/18-guitar-body/)**<br>An original double-cutaway solid body in red alder with a carved top, a bolt-on neck pocket, two humbucker routes, a rear control cavity and a string-through bridge placed by the scale length, finished in candy-apple red. | Lutherie | 7/10 |
<!-- gallery:end -->

## Rebuild and check

You need `craft3d-cli` from 3DCraft (the commit in [`tools/pin.json`](tools/pin.json)) and Python 3.

```sh
tools/examples.py build socket-head-cap-screw     # build.json -> .3dcraft and exports
tools/examples.py check                           # rebuild every example and check it
craft3d-cli run --new '{"units":"mm"}' --script examples/01-socket-head-cap-screw/build.json --out screw.3dcraft
```

## For contributors and agents

Read [`AGENTS.md`](AGENTS.md). Things 3DCraft could do better, found while building these, are collected in
[`3DCRAFT-FEEDBACK.md`](3DCRAFT-FEEDBACK.md).

## Licence

MIT, see [`LICENSE`](LICENSE). Third-party data used by an example is listed in
[`ATTRIBUTION.md`](ATTRIBUTION.md).
