# Intent — Share as an incident report

**Author:** Claude (audit follow-up)
**Date:** 2026-10-30
**Status:** accepted
**Next stage:** `run-shell.md` § 11

Accepted by the user on 2026-10-29 in chat, as part of a standing instruction to keep improving the game: "/loop continue and improve the game until it rocks, merge when green, just keep going". This item is the audit recommendation to write the result as an incident report.

## Problem

**OBSERVED:** Share sends the game's name and the card rows as plain `LABEL value` lines (`run-shell.md` § 11, `RunCard.shareText`). It is the only thing a player sends to someone else, and it reads like a stats dump. The satire, that the system documents you, is absent from the one artefact that leaves the device.

## Proposed outcome

The shared text reads as the surveillance state's own paperwork about the player:
- an incident report header;
- an outcome in the authority's terms (subject extracted, detained, or report void);
- the same facts, phrased as observation and tampering.

It still carries every card row and no identifier.

## Affected users/systems

Players who share, and the people who receive it. `run-shell.md` § 11 and the runtime `RunCard.shareText`. The on-screen card is unchanged.

## Constraints/non-goals

- RS-016 holds: the game's name first, every row's label and value present, and no seed, digest, version or identifier.
- The medal line stays last, without `NEW`.
- Original and fictional wording.

## Open questions

None.

## Verified claims

- The current format is in `RunCard.shareText`, and RS-016 plus `MedalTests` pin its invariants.

## Assumed claims

- A themed share is shared more. Assumed; there are no analytics by design.
