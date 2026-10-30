# Intent — the Captain goes round solids too

**Author:** Claude (probe follow-up to D-114)
**Date:** 2026-10-30
**Status:** draft
**Next stage:** `bosses.md`, `enemies-and-encounters.md` § Corner pursuit

`draft` until the owner accepts.

## Problem

D-114 taught standard enemies to go round solids. It left the bosses unchanged, so the Algorithmic Moderate (the Captain) still pursues by the direct vector.

**OBSERVED** on the D-114 code (seed 21, stealth pilot, Ricochet; scratch boss trace every 300 ticks):
- **The fight leaves the Court.** The Captain pursues the Player from the Court at (1993, 686) to the service yard.
- **Then it pins.** From tick 12 600 to 21 300, about 2.5 minutes, it stands at x = 1278 against the east face of `solid-06-service-yard-a`. That is the face plus its radius 30, and its state stays `pursue`. The Player stands below and behind the block.
- **The fight never ends.** The Player chips the Captain from 1180 to 770 Integrity, and the probe stalls.

This is one of the two stalls left after D-114, and it is the D-114 cheese in the climax: put a block between you and the Captain.

## Proposed outcome

- In pursuit, the Captain uses the same approach point as standard enemies (§ Corner pursuit), with its own radius.
- Its telegraphs, attacks, phases and damage are unchanged.
- The probe's boss-fight stalls fall to zero or near it. The Court win rate stays within noise of D-114/D-115.

## Affected users/systems

- **Players:** the climax.
- **Specs:** `bosses.md` (pursuit) and an extension to `enemies-and-encounters.md` § Corner pursuit.
- **Runtime:** the boss steering. One `CornerPursuit.waypoint` call.
- **Versions:** a ruleset bump. Every golden digest changes.

## Constraints/non-goals

- **Constitution:** one level, no new content.
- **No change** to boss HP, phases, attack timings, telegraphs or the Court Lockdown rule (D-109).
- **No leash:** whether the Captain may leave the Court is a separate question (see Open questions).

## Open questions

- Should the Improper Search Daemon get the same rule? No stall was observed for it.
- Is it intended that the boss fight can be kited out of the Court and across the map? A leash would be a different intent.

## Verified claims

- D-114's text excludes the bosses, and the boss pursues by the direct vector.
- The trace above is reproducible on the D-114 code with the scratch probe (seed 21, stealth, Ricochet).

## Assumed claims

- The same corner rule is enough for a radius-30 body in this arena. To be verified by a sweep.
