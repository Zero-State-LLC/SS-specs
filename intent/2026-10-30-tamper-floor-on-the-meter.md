# Intent — show the Tamper floor on the Exposure meter

**Author:** Claude (audit follow-up)
**Date:** 2026-10-30
**Status:** accepted
**Next stage:** `hud-tutorial.md` § Exposure presentation

Accepted by the user on 2026-10-29 in chat, as part of a standing instruction to keep improving the game: "/loop continue and improve the game until it rocks, merge when green, just keep going". This item is the audit recommendation "teach the cost of tampering".

## Problem

D-084/D-086 make Camera destruction permanent: each destroyed Camera adds +150 Exposure and raises the floor that Exposure can never recover below, by 150 per Camera. It is the game's sharpest piece of satire: vandalism makes you a permanent suspect.

**OBSERVED:** the HUD never shows the floor. `+150 TAMPER` appears beside the bar, but nothing tells the player that the bar can no longer drain past a point. So a player who destroys three Cameras sees Exposure stall at 450 for the rest of the run and cannot tell why.

## Proposed outcome

Once a Camera has been destroyed, the Exposure bar shows where the floor is, and the marker moves up with each further destruction. It reads without colour.

## Affected users/systems

Players (HUD readability). `hud-tutorial.md` and the runtime HUD. No rule, content, digest or receipt change.

## Constraints/non-goals

- Presentation only, derived from the number of destroyed Cameras the snapshot already carries.
- No new tutorial line: tutorial progress is authoritative state.
- `+150 TAMPER` and the threshold notches are unchanged. One level.

## Open questions

None.

## Verified claims

- The floor rule (`exposure.md` § Tamper floor, D-084).
- The existing HUD draws threshold notches at 200, 450, 700 and 1000, and no floor marker (`HUDRenderer.drawExposure`).

## Assumed claims

- Players read a marker on the bar faster than a caption. Assumed until T903/T904.
