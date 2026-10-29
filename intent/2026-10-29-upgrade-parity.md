# Intent — no dominant upgrade

**Author:** Claude (audit follow-up)
**Date:** 2026-10-29
**Status:** accepted
**Next stage:** `upgrades.md`, `contracts/combat-content-*.json`

Accepted by the user on 2026-10-29 in chat: "accept, and merge". The next stage is specify; open questions stay open until the specification answers them.

## Problem

The run's only build decision is one pick from three upgrades after M-A (`upgrades.md`). Its value depends on all three being live choices. **OBSERVED:** they are not.

540 legal probe runs (`heatD083StyleSweep`, SS_HEAT_SEEDS=20, SS_HEAT_LEGAL_SEEDS=60, runtime `5b36566`, 2026-10-29); win rate, with median winning time in brackets:

| Upgrade | All profiles | competent | stealth | loud |
|---|---:|---:|---:|---:|
| Ricochet Pulse | **68.9%** (4:45) | 70.0% | 63.3% | 73.3% |
| Signal Jammer | 55.0% (5:42) | 56.7% | 70.0% | **38.3%** |
| Ghost Step | 55.0% (5:41) | 53.3% | 58.3% | 53.3% |

Main findings:
- Ricochet is the best or near-best pick for every style. It wins about 55 s faster than either alternative.
- Ghost Step is never the best pick.
- Loud play with Signal Jammer is a trap at 38%.
- No probe has reported per-upgrade results since D-090, so this went unnoticed.

The bots are not players (D-093). The direction of the gap is still large enough to act on, and a human playtest should confirm it.

## Proposed outcome

- Each upgrade is the strongest pick for at least one play style, and none is the strongest for all.
- Spread between upgrades within a play style is small enough that the choice is about style, not correctness. A candidate target is at most 8 points; the owner sets it.
- Every probe report includes per-upgrade win rates, so drift is visible.

## Affected users/systems

Players (the run's one build choice). Specs: `upgrades.md` numbers, the combat content contract version, the UP vectors. Runtime probes: per-upgrade summary. **Content version and golden vectors change.**

## Constraints/non-goals

- Same three upgrades, same roles, same selection rule. More picks per run is a separate decision.
- The `upgrades.md` balance invariants hold: no HP or spawn changes, no Camera exploit, each upgrade wins with zero Cameras destroyed.
- Tuning targets stay inside the existing win band used by D-101 (~53–65% for bots).
- If the Court's Exposure changes (intent `2026-10-29-live-exposure-in-court`), tune after that lands. Signal Jammer and Ghost Step gain value there.

## Open questions

- Which levers? Candidates, all existing parameters:
  - Ricochet: continuation range 160 → ~120, or continuation damage 10 → 6–7;
  - Ghost Step: post-dodge immunity 18 → 30 ticks, extended to patrol and enemy sight;
  - Signal Jammer: also cut heat reinforcements by 1.
- Is the stealth/loud split part of the target, so that each upgrade has a home style?

## Verified claims

- The table above comes from the probe report named in Problem.
- `upgrades.md` permits only one pick per run, and its balance invariants are as quoted.

## Assumed claims

- Human players' upgrade win rates track the bot ordering. Assumed until T903/T904.
