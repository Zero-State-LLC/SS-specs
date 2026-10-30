# Intent — enemies go round solids

**Author:** Claude (probe follow-up)
**Date:** 2026-10-30
**Status:** accepted
**Next stage:** `enemies-and-encounters.md`, `contracts/combat-content-*.json` if values are data

Accepted by the user on 2026-10-30 in chat: "accept corner steering intent and keep going". The next stage is specify.

## Problem

A chasing enemy cannot find its way round a solid. **OBSERVED** on `ss-rules-010`, runtime `b275ad1`:

- **Pursuit stops at the far face.** `enemies-and-encounters.md` § Autonomous Informant says pursuit "always takes the shortest direct steering vector toward the Player". With the X-then-Y slide, an enemy on the far side of a block slides along the face until it is level with the Player, then stops.
  - Scratch trace: a Correlator starting at (1268, 1282) behind `solid-06-service-yard-a`, with the Player held at (1024, 1380), ends at (1268, 1378) after 600 ticks. It never reaches the Player.
  - An Informant does the same.
- **Attacks fire into the wall.** A Correlator in charge range telegraphs its charge into the wall, because the charge trigger reads range, not line of fire. A Witch in range holds and fires bolts that the solid consumes.
- **This is the main source of the probe's stalls.** In the D-113 confirmation sweep, 29 of 540 legal runs stalled: the pilot spent 180 s on one objective at high Integrity. Stall dumps (12 seeds) found every survivor aware, pursuing or cooling down, and pressed against the far side of `solid-06-service-yard-a` or `solid-10-grid-island-b`, with the block on the line to the Player.

For a player, this reads as broken AI and invites a cheese: stand behind a block and melee enemies never arrive.

## Proposed outcome

- A chasing enemy with no clear line to the Player moves round the blocking solid and arrives, instead of stopping at the face.
- An enemy does not start an attack that needs a clear line (Correlator charge, Witch bolt) without one.
- The rule is deterministic, integer-only and cheap. It is the same for every standard enemy that pursues. The Vendor's placed mine, the Daemon and the bosses are unchanged.
- The probe's stall count falls, and win rates stay inside the D-101 band.

## Affected users/systems

- **Players:** enemy movement around solids.
- **Specs:** `enemies-and-encounters.md` (pursuit, charge, Witch) and new EN vectors.
- **Runtime:** `EnemySystem` steering.
- **Versions:** a ruleset bump. Every golden digest changes.

## Constraints/non-goals

- **Constitution:** one level, the same five archetypes, no new content.
- **No general pathfinding.** No navmesh and no grid search; a corner waypoint against the blocking solid is enough for this arena's convex blocks.
- **No perception change:** awareness, sight cones, alerts and the Transit Patrol are unchanged. Unaware enemies are unchanged.
- **No combat change:** no change to speed, damage, HP, spawn counts or attack timings.

## Open questions

- Should the Vendor reposition for a line too? Its mine is placed at the Player's position, so a solid does not stop it today.
- Must the corner margin be data in `combat-content`, or a fixed simulation constant validated against the contract, as with D-113's fields?

## Verified claims

- The quoted pursuit rule, the X-then-Y slide and "Charge uses normal solid collision and ends on first solid impact" are in `enemies-and-encounters.md`.
- The trace and the stall dumps come from scratch probes on `b275ad1` and are reproducible.

## Assumed claims

- A corner waypoint is enough for `civic-seam-arena-004`. Its solids are axis-aligned boxes. Most stand alone, but some touch: `solid-01`, `-02` and `-03` share edges, and `gate-mc-forward` meets `solid-10` and `solid-11`, as `gate-elite-forward` does `solid-11`. A corner inside a neighbouring box cannot be reached directly, so the rule skips it and picks another. To be verified by the sweep and the stall count.
