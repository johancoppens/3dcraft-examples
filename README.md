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
