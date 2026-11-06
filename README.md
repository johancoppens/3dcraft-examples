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
| <img src="examples/09-mailer-box/preview.png" width="240" alt="Mailer box"> | **[Mailer box](examples/09-mailer-box/)**<br>A FEFCO 0427 mailer of single-wall E-flute kraft board, 200 × 150 × 60 mm inside, folded from its die-cut blank: rolled end walls locked by tabs, dust flaps and a tuck-in lid. | Packaging | 7/10 |
| <img src="examples/10-headphone-stand/preview.png" width="240" alt="Headphone stand"> | **[Headphone stand](examples/10-headphone-stand/)**<br>A one-piece headphone stand printed upright in PETG without supports: a slim lofted column flaring into a wide saddle curved like a headband, a swept cable hook, and a round base weighted by an embedded steel disc. | 3D printing, product design | 6/10 |
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
