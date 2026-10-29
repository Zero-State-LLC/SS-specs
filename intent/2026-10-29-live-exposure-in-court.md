# Intent — keep Exposure live through the Captain Court

**Author:** Claude (audit follow-up)
**Date:** 2026-10-29
**Status:** accepted
**Next stage:** `exposure.md`, `bosses.md`, `encounter-objectives.md`

Accepted by the user on 2026-10-29 in chat: "accept, and merge". The next stage is specify; open questions stay open until the specification answers them.

## Problem

Exposure is the game's defining system: surveillance as an active threat (constitution, spec.md). But for most of a run it does nothing.

**OBSERVED in the spec:**
- M-C's activation sets Exposure to 1000 and latches Lockdown for the rest of the run (`exposure.md` § Quiet approach, step 6–8 of the Exposure order). "Recovery never exits Lockdown."
- Once latched, later positive pulses do not change the value.
- So in the Captain Court:
  - the Temporary Order Observation pulse (`bosses.md`, BO-005) has no effect;
  - Signal Jammer's 25% pulse reduction (BO-006) has no effect;
  - the Z-06 Camera cannot raise anything;
  - Ghost Step's Camera immunity has no value.
- `arena.md` § 7 describes the Court as where the Player "masters Captain interactions with known Camera behavior". That is unreachable while Exposure is pinned.

**OBSERVED in a 540-run legal probe** (runtime `heatD083StyleSweep`, SS_HEAT_SEEDS=20, SS_HEAT_LEGAL_SEEDS=60, runtime `5b36566`, run on 2026-10-29):
- Lockdown is entered at a median of **89 s**.
- In winning runs, **72%** of the run (p10 65%, p90 78%) passes with Exposure latched at 1000. That includes the whole 91 s median boss fight.

## Proposed outcome

- The Captain Court is a surveillance fight.
  - Exposure can rise and fall during the boss. Temporary Order, the Z-06 Camera and Fog pulses visibly matter.
  - Signal Jammer and Ghost Step keep a reason to exist after M-C.
- Lockdown remains a real, frightening state during M-C (the Lockdown Ring) and still has teeth in the Court. Reaching 1000 in the Court should cost the player something readable, not only a number.
- The run still reads as one escalation: Lockdown is the climax of M-C, and the Court is a new, legible surveillance regime.

## Affected users/systems

Players (boss fight). Specs: `exposure.md`, `bosses.md`, `encounter-objectives.md`, `upgrades.md` (vectors only), `audio-haptics.md` music states if Lockdown can end. Runtime: Exposure order, Detection State projection, heat, HUD caption. **Ruleset and fixture versions change** (complete-run vectors, kernel vectors, replay matrix), which needs a fixture review per D-061.

## Constraints/non-goals

- No new enemy, attack, weapon, upgrade or zone. Use the existing Temporary Order, Z-06 Camera, Fog pulses and heat reinforcement archetype.
- Quiet approach (D-101) and the GHOST medal keep their meaning: decided before the Court.
- Deterministic and versioned: ruleset bump, golden vectors regenerated and reviewed.
- One level.

## Open questions

- Where does Exposure start in the Court? Candidate: Lockdown ends when the Daemon is defeated (`EliteDefeated`) and Exposure is set to 700 (`hunted`), so the player enters the Court already watched but able to recover behind the Court's cover.
- What does reaching 1000 in the Court do? Candidates:
  - (a) "Emergency Order": 2 Informants from existing spawn sockets, at most once per boss phase;
  - (b) the Captain's Observation ratio rises for that phase;
  - (c) both.
- Does music return from `lockdown` to `boss`? (`audio-haptics.md` already has a boss bed per phase, so probably yes.)
- Does the court restore (D-096, 50%/60%) need retuning once Exposure has a cost? Answer by probe and by human playtest.

## Verified claims

- The latch rules, quoted above, are in `exposure.md`. The Temporary Order pulse and BO-005/BO-006 are in `bosses.md`.
- The 89 s and 72% figures come from the probe report above (`lockdownEntered` and `ticks` milestones over 322 wins).

## Assumed claims

- A live Court will raise boss-fight difficulty. Assumed until probed; win rates are expected to need retuning toward the ~53–65% band D-101 used.
- Players notice and value a surveillance boss over a pure damage boss. Assumed until T903/T904 playtests.
