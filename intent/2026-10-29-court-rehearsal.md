# Intent — rehearse the Court after a boss death

**Author:** Claude (audit follow-up)
**Date:** 2026-10-29
**Status:** accepted
**Next stage:** `run-shell.md`

Accepted by the user on 2026-10-29 in chat: "accept, and merge". The next stage is specify; open questions stay open until the specification answers them.

## Problem

Almost every death happens at the boss, and retrying it means replaying four minutes of identical content.

**OBSERVED** (540 legal probe runs, `heatD083StyleSweep`, runtime `5b36566`, 2026-10-29):
- 218 runs failed. **194 of them (89%) died after the Captain activated.** D-093 recorded the same pattern, 198 of 203.
- A boss death costs the player a median **236 s** of play to get back to the Court, which they then survived for a median **54 s**.
- Waves, patrol and boss are deterministic, and the Daily seed only varies Camera sockets. So the four minutes before the Court are largely the same each time.

**OBSERVED in the spec:** after any terminal outcome the only action is Restart, which begins a new run from tick 0 (`run-shell.md` § 6). There is no way to practise the part of the game that decides the outcome.

On a phone a 4:1 replay-to-retry ratio is where players quit. The boss telegraphs (D-096) are designed to be learned, and learning them needs repetitions.

## Proposed outcome

- After a run ends in failure inside the Captain Court, the terminal surface also offers **Rehearse the Court**. It starts at the moment the Captain activated in that run, with the Player at the court-threshold Integrity that run received.
- A rehearsal is visibly not a run. It earns no medals, never becomes today's best or the ghost, and its card says REHEARSAL. Share is either unavailable or says so.
- Restart still begins a real Daily Run from tick 0.

## Affected users/systems

Players who die to the boss. Specs: `run-shell.md` (§ 4 terminal surface, § 6 Restart, § 11 card, § 12 medals, vectors), possibly `events-receipts-replays.md` for how a rehearsal is recorded. Runtime: snapshot of authoritative state at `bossActivated` and the terminal surface. **No ruleset change** if rehearsal restores an exact authoritative snapshot of the same run.

## Constraints/non-goals

- No meta-progression. A rehearsal grants nothing that carries into a Daily Run.
- The legal Daily Run stays intact: its seed, receipts, medals, best and ghost are unaffected by rehearsals.
- No checkpoints anywhere else, and no continue after death in a real run.
- One level.

## Open questions

- Restore an exact snapshot of the run at `bossActivated`, or re-simulate the recorded commands to that tick? A snapshot is instant; re-simulation reuses replay tooling but costs seconds on device.
- Offer it after every Court death, or only after the first death of the day?
- How is a rehearsal receipted? Candidates: no receipt, or a receipt marked non-legal that the replay tools reject as a Daily Run.
- Is the terminal surface's single-control narrowness (`run-shell.md` § 6, § 8.1) worth a second control here? The owner already left a "return to title" control OPEN for the same reason.

## Verified claims

- The failure counts and times come from the probe report named in Problem (`bossActivated` milestone and terminal tick).
- `run-shell.md` § 6 and § 12 are as described.

## Assumed claims

- Faster boss repetitions raise human retention and boss win rates. Assumed until T903/T904.
