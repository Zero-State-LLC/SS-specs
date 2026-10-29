# Exposure Contract

Status: CANONICAL  
Contract version: `exposure-001`

## Purpose

Exposure is the one authoritative surveillance-pressure value. It is deterministic, integer-valued, bounded, and independent of rendering.

## Constants

| Constant | Value |
|---|---:|
| Scale | 0–1000 integer points |
| Starting Exposure | 0 |
| First detecting Camera | +2 points/tick |
| Each additional detecting Camera | +1 point/tick |
| Contact gain cap | +5 points/tick |
| Recovery delay after last contact | 60 ticks |
| Recovery | −2 points/tick |
| Camera Tamper Spike | +150 points/destruction (D-086) |
| Tamper floor | 150 points × Cameras destroyed this run (D-084) |

**Tamper floor (D-084).** Recovery never takes Exposure below
`150 × destroyedCameras`, the number of Cameras destroyed this run. It limits
recovery only: it never raises Exposure, never adds to a Tamper Spike, and
never triggers a Detection State event by itself.

Because each Tamper Spike adds exactly the floor increment (+150, D-086), and
nothing but recovery ever lowers Exposure, Exposure after `k` destructions is
always at least `min(1000, 150 × k)`. After three destructions the Player is at
or above 450 (`tracked`) for the rest of the run. A destroyed Camera is a lasting
mark, not a spike that fades in two seconds.

At 60 ticks/second, one Camera adds 120 points/second. Recovery begins only after 60 complete no-contact ticks and removes 120 points/second. Tamper is instantaneous and is not modified by contact count.

## Detection states

| State | Exposure |
|---|---:|
| `hidden` | 0–199 |
| `observed` | 200–449 |
| `tracked` | 450–699 |
| `hunted` | 700–999 |
| `lockdown` | 1000 |

There is no threshold hysteresis. State is a pure projection of Exposure after all deltas for the tick. `lockdown` latches and fixes Exposure at 1000 while it holds. Recovery never exits Lockdown. The latch is released once, when the Improper Search Daemon is defeated (§ Court release, D-109). Lockdown entered again after that latches for the rest of the run.

## Contact aggregation

After same-tick destruction removes dead Cameras, collect distinct surviving Camera IDs detecting the Player. Sort IDs ascending. For count `n`:

```text
contactDelta = n == 0 ? 0 : min(5, 2 + n - 1)
```

Overlapping fields add pressure; multiple samples from one Camera never do. Occlusion, range, and fixed field-angle tests belong to the arena/camera geometry contract.

## No-contact clock

- A contact tick sets `noContactTicks` to 0.
- A no-contact tick increments it by 1.
- Recovery applies when the incremented value is greater than 60.
- Therefore, the first recovery delta occurs on the 61st consecutive no-contact tick.
- Any new contact resets the clock before recovery is considered.

## Tick resolution

1. Camera contact is sampled.
2. Projectile damage and destruction resolve.
3. Contacts from Cameras destroyed this tick are removed.
4. Surviving-contact delta or no-contact recovery is calculated.
5. Ordered Tamper Spikes are added by Camera stable ID.
6. Apply eligible Fog Analytics Cloud pulses in source entity-ID order, then Algorithmic Moderate Observation pulses. Apply their existing Signal Jammer modifiers exactly once (upgrades.md). Clamp each stage to 0–1000. Once 1000 is reached, later positive pulses do not change the value. A previously latched or forced Lockdown stays at 1000.
7. Project Detection State once from the final value; emit one `DetectionStateChanged` from the tick's starting state to its final state if different, including downward changes. Then resolve the quiet-approach latch from that final state.
8. If 1000 is first reached, emit `LockdownEntered` once in phase 14 with the reason that reached the cap. Forced Lockdown takes precedence as the reason.

D-102: named pulses are eligible only if the Player survived phase 12. On a lethal tick, surviving Camera contact/recovery and Tamper still resolve, but fog and Observation pulses do not apply; failure remains terminal. M-C activation exempts that tick and later ticks from quiet-approach loss as in D-101. Exposure changes retain phase-13 before/after/reason records for each changed stage, but intermediate thresholds never publish extra Detection State transitions.

Tamper and continuous contact may cross several thresholds in one tick. Emit one `DetectionStateChanged` event containing old and final state, not an event for every skipped state.

## Upgrade hook

`Signal Jammer` reduces the continuous contact delta as described here; its separate 25% Fog/Observation pulse reduction is defined in upgrades.md. Its modifier is applied after aggregation and before Tamper, using integer arithmetic. It cannot reduce a positive contact delta below 1 and never changes Tamper, recovery, thresholds, or Lockdown latching. Its exact value belongs to the upgrade contract.

## Court release (D-109)

Lockdown is the climax of M-C. The Captain Court is a new surveillance regime, not a continuation of it, so the latch is released when the Daemon falls:

1. On the tick `EliteDefeated(improperSearchDaemon)` is emitted (phase 16), clear the Lockdown latch and set Exposure to 700. Do not change the Detection State on that tick.
2. The next tick's Exposure resolution (phase 14) runs normally from 700. It projects the Detection State and emits one `DetectionStateChanged` from `lockdown` to its final state, normally `hunted`.
3. From then on, contact, Tamper, recovery, the Tamper floor and named pulses apply as everywhere else. The Captain's Temporary Order Observation pulses and the Z-06 Camera can raise Exposure; cover lets it recover.
4. Reaching 1000 in the Court enters Lockdown again: one `LockdownEntered` with the reason that reached the cap. That Lockdown latches for the rest of the run. Its cost is the Captain's faster attack cadence (bosses.md § Court Lockdown).

Notes:
- Setting Exposure to 700 is an assignment. The Tamper floor only limits recovery, so a floor above 700 does not raise it.
- The quiet-approach latch and the `GHOST` medal are decided before M-C and are unaffected.
- M-C's forced Lockdown and its heat rules are unchanged.

## Quiet approach (D-101)

`quietApproach` is `true` at run start. In phase 14, after the Detection State
resolves, it becomes `false` if the state is `tracked` or higher and M-C has
not activated. It is latched: falling back to `hidden` or `observed` never
restores it. M-C's activation sets Exposure to 1000 and latches Lockdown in
that same tick's resolution (enemies-and-encounters.md), so from the
activation tick on the check no longer runs, and the forced Lockdown never
costs it. It is the same condition as
the `GHOST` medal (run-shell.md § 12), and it pays out once, at the Captain
Court threshold (bosses.md).

## Required state

```json
{
  "exposure": 0,
  "detectionState": "hidden",
  "noContactTicks": 0,
  "lockdownEntered": false,
  "quietApproach": true
}
```

## Golden vectors

| ID | Input | Expected |
|---|---|---|
| EX-001 | 100 ticks, one Camera | 200, `observed` |
| EX-002 | one tick, three Cameras | +4 |
| EX-003 | one tick, eight Cameras | +5 cap |
| EX-004 | 60 no-contact ticks from 300 | remains 300 |
| EX-005 | 61 no-contact ticks from 300 | 298 |
| EX-006 | contact on no-contact tick 60 | clock resets; contact gain; no recovery |
| EX-007 | destroy sole detecting Camera at 190 | no contact delta; +150 Tamper = 340, `observed` |
| EX-008 | destroy two detecting Cameras at 850 | +300 clamps 1000; one Lockdown event |
| EX-009 | no contact after Lockdown | remains 1000/`lockdown` |
| EX-010 | delta jumps `hidden` to `hunted` | one old→final transition event |
| EX-011 | 3 Cameras destroyed, Exposure 500, 200 no-contact ticks | stops at 450; never below |
| EX-012 | 1 Camera destroyed, Exposure 120 (below the floor after a same-tick change), no contact | recovery does not apply; Exposure is not raised to 150 |
| EX-013 | Detection State resolves to `tracked` before M-C has started | `quietApproach` becomes `false` |
| EX-014 | after EX-013, Exposure recovers to `hidden` | `quietApproach` stays `false` |
| EX-015 | peak Detection State `observed` until M-C activates, then the forced Lockdown on the activation tick | `quietApproach` stays `true` |
| EX-016 | Detection State reaches `tracked` on the tick before M-C activates | `quietApproach` becomes `false` |
| EX-017 | pre-recovery Exposure 432, no-contact clock >60, one +20 Fog pulse before M-C | final 450/tracked; one observed→tracked event; quietApproach false; next tick 448/observed cannot restore it |
| EX-018 | multiple contact/Tamper/named deltas cross several thresholds | one starting→final DetectionStateChanged; at most one phase-14 LockdownEntered |
| EX-019 | lethal Player damage plus a due Fog pulse | no named pulse applied; contact/recovery and Tamper still resolve; failure wins |
| EX-020 | M-C activation with due named pulses | final 1000/lockdown; one forced Lockdown event; quiet approach preserved if previously true |
| EX-021 | `EliteDefeated(improperSearchDaemon)` while Lockdown is latched | that tick ends at 1000/`lockdown`; the next tick resolves from 700 with one `lockdown`→`hunted` event and no `LockdownEntered` |
| EX-022 | after the Court release, contact raises Exposure to 1000 | one `LockdownEntered`; Exposure stays 1000/`lockdown` for the rest of the run |
| EX-023 | after the Court release, 61 no-contact ticks from 700 with no Cameras destroyed | 698, `tracked` |
| EX-024 | Court release with 6 Cameras destroyed (floor 900) | Exposure is set to 700; the floor does not raise it, and recovery does not apply while Exposure is below the floor (as EX-012) |

## Failure rules

Unknown Camera IDs, duplicate contacts, non-integer deltas, invalid thresholds, or values outside the scale are content/runtime errors. Debug builds fail fast; release builds reject the affected run and produce a diagnostic receipt rather than silently repairing authoritative state.
