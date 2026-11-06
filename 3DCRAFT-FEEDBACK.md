# Feedback for 3DCraft

What building these examples showed 3DCraft gets wrong or lacks, collected for the developer to take to
3DCraft in one go (3DCraft is frozen for R1; nothing is fixed from here). Kinds: **Bug** (wrong result, crash,
a valid request refused; with a reproducer in `findings/`), **Missing capability** (phrased for any shape
and anyone), **Performance** (with numbers), **Agent friction** (what made building through commands slow or
error-prone). See `AGENTS.md` §7.

All entries are against 3DCraft `f4b0813c` unless they say otherwise.

| Id | Kind | Title | Found in | Impact |
|---|---|---|---|---|
| [F-001](#f-001) | Performance | The guide's fuel tank takes 55 s to open, the chassis 9 s | calibrating the load budget | start screen |
| [F-002](#f-002) | Agent friction | An extrude with `cut`, `join` or `intersect` cannot name its extrusion | calibrating the name check | history names |
| [F-003](#f-003) | Agent friction | `craft3d-cli --version` does not print the commit | setting up the pin | tooling |

## F-001

**Performance.** `docs/examples/tank.json`, built and saved, takes **54.3 s** to open
(`craft3d-cli info tank.3dcraft`, release build on the developer's laptop, 850 MB peak); without its
assertions still 54.9 s, so the geometry itself costs it, not the checks. The chassis takes 9.0 s, the
bracket 0.04 s. Both the tank and the chassis are on the start screen, where a click builds them.
**Should:** an example on the start screen opens in a few seconds; or the start screen opens a saved
document whose bodies need not be rebuilt in full. Reproduce: `craft3d-cli run --new '{"units":"mm"}'
--script docs/examples/tank.json --out tank.3dcraft && time craft3d-cli info tank.3dcraft`.

## F-002

**Agent friction.** `feature.extrude` with `cut`, `join` or `intersect` adds two features, the extrusion and
the boolean; `name` names the boolean, and the extrusion keeps an automatic name (`Extrude1`). The history
then shows names that say nothing; renaming each costs an extra `feature.rename` step. Seen in
`docs/examples/bracket.json` (`Extrude1`, `Extrude2`). **Should:** a param to name the extrusion too (for
example `toolName`), or derive its name from the boolean's (`Drilled (tool)`).

## F-003

**Agent friction.** `craft3d-cli --version` prints `craft3d-cli 0.1.0`; the commit is built into the binary
(for bug reports) but not printed, so a script cannot check which build it runs without searching the
binary's bytes (what `tools/examples.py` does). **Should:** `--version` prints the commit and the file format
version, e.g. `craft3d-cli 0.1.0 (f4b0813c, format 69)`.
