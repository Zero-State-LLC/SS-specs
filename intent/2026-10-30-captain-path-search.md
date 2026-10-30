# Intent — a path search for the Captain

**Author:** Claude (follow-up to D-116)
**Date:** 2026-10-30
**Status:** accepted
**Next stage:** `bosses.md`

Accepted by the user on 2026-10-30 in chat ("lets do a", choosing option (a) on SS-runtime#163). This supersedes the "no path search" constraint of `2026-10-30-captain-goes-round-solids` for the Captain only. The next stage is specify.

## Problem

D-116 gave the Captain the D-114 single-waypoint corner rule. It was never adopted by the runtime, because it froze the Captain in new places.

**OBSERVED** on scratch builds of the D-116 rule and of a body-clearance amendment (D-117, not merged):
- **D-116:** the debug `boss` scenario, with the Player standing still at the far spawn, never ends. The Captain stops for good under `solid-11-court-column-a`: its line to a corner is clear, but its radius-30 body is not. It also cannot pass the 52-unit gap under `solid-06`.
- **D-117:** requiring a body-clear leg removed that freeze, but two new ones appeared in a 540-run sweep (seeds 34 and 46). In one, the orbit cancels the slide off the corner of `solid-08`. In the other, the Player is at the top edge, every corner is rejected, and the rule falls back into a wall.

The overall win rate fell to 51.3%, under the D-101 band. A single waypoint without memory keeps finding new edges for a body this wide.

## Proposed outcome

- The Captain reaches the Player whenever a path wide enough for its body exists, and never freezes against a solid.
- It finds the shortest route round the live solids, recomputed every tick, deterministic and integer-only.
- Standard enemies keep D-114, and the Daemon is unchanged.

## Affected users/systems

- **Players:** the climax.
- **Specs:** `bosses.md` § Corner pursuit (replaced) and BO vectors.
- **Runtime:** `BossSystem` steering and a memoised corner graph.
- **Versions:** ruleset `ss-rules-013` (D-116's identity, never adopted).

## Constraints/non-goals

- **Captain only.** No path search for standard enemies or the Daemon.
- **No change** to telegraphs, attacks, phases, speed or damage. No leash.
- **Determinism:** the search, its tie-breaks and its geometry are integer-only, and any cache is a pure memo of its inputs.

## Verified claims

- The freezes above are reproducible on the scratch builds named, with scratch traces (SS-runtime#163 comments).

## Assumed claims

- A corner graph of the live solids is enough for this arena, because every solid is an axis-aligned box. To be verified by the sweep, the boss scenario and the freeze vectors.
