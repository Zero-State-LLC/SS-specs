# Intent — give the Captain a voice in the captions

**Author:** Claude (audit follow-up)
**Date:** 2026-10-30
**Status:** accepted
**Next stage:** `audio-haptics.md` § Accessibility

Accepted by the user on 2026-10-29 in chat, as part of a standing instruction to keep improving the game: "/loop continue and improve the game until it rocks, merge when green, just keep going". This item is the audit recommendation "express the satire in the game's text".

## Problem

**OBSERVED (runtime `AudioProjector`):**
- Every Captain attack is captioned `Boss telegraph`; the four policy phases are all `Policy phase`.
- The Daemon's attacks are `Query telegraph` and `Dash telegraph`.
- No specification names this copy; the runtime made it up.

The audit found the satire lives mostly in names, while the fight itself reads as mechanics plus a lighting change. These captions are safety-critical: they appear under the default Important setting. So they are the one piece of text guaranteed to be seen in every fight.

## Proposed outcome

- Each attack caption says what the attack **is** first (cone, three bolts, field, ring with one gap). That is the safety information.
- Then it gives the authority's justification, in its own voice.
- Each phase change and the defeat get a line that makes the satire legible.

## Affected users/systems

Players, including caption and VoiceOver users. `audio-haptics.md` and the runtime `AudioProjector`. No rule, cue ID, audio asset, haptic, digest or receipt change.

## Constraints/non-goals

- The attack form stays the first word, and nothing is removed from what a caption tells the player.
- At most 40 characters, so the uppercase caption fits its column.
- Fictional and original: no real organisation, statute, person or slogan.
- No new cues, assets or voice-over.

## Open questions

None.

## Verified claims

- The caption strings are in `AudioProjector.appendBossAndElite`.
- The caption column is 224 points at 8 points uppercase (`HUDRenderer.drawCaptions`).

## Assumed claims

- Players notice satire in the captions during a fight. Assumed until T903/T904.
