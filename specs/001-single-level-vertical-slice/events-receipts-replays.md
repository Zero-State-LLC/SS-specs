# Events, Receipts, and Replays

Status: CANONICAL  
Contract version: `events-receipts-replays-001`

Machine contracts:

- `contracts/event-001.schema.json`
- `contracts/run-receipt-001.schema.json`
- `contracts/runtime-kernel-001.json`

## Event envelope

Every authoritative event contains:

`schemaVersion, tick, ordinal, sequence, type, primaryEntityId, secondaryEntityId, payload`

- `tick`: UInt64-compatible non-negative integer.
- `ordinal`: fixed event-type ordinal.
- `sequence`: zero-based index after final phase-18 sorting.
- Entity IDs are decimal strings to preserve UInt64 across JSON environments; absent ID is null.
- Payload uses only the fields defined for its type.
- Events are immutable after publication.

## Event ordinals

| Ordinal | Type |
|---:|---|
| 10 | `runStarted` |
| 20 | `upgradeSelected` |
| 30 | `dodgeStarted` |
| 40 | `weaponFired` |
| 50 | `projectileHit` |
| 60 | `cameraIntegrityChanged` |
| 70 | `cameraDestroyed` |
| 80 | `entityDamaged` |
| 90 | `entityDied` |
| 100 | `playerDamaged` |
| 110 | `exposureChanged` |
| 120 | `detectionStateChanged` |
| 130 | `lockdownEntered` |
| 140 | `waveStarted` |
| 150 | `mobEncounterCompleted` |
| 160 | `eliteActivated` |
| 170 | `eliteDefeated` |
| 180 | `bossActivated` |
| 190 | `bossPhaseChanged` |
| 200 | `bossAttackStarted` |
| 210 | `bossDefeated` |
| 220 | `allCamerasDestroyed` |
| 230 | `extractionArmed` |
| 240 | `extractionCountdownChanged` |
| 250 | `extractionReset` |
| 260 | `runSucceeded` |
| 270 | `runFailed` |
| 280 | `diagnosticFailure` |

Ordinals are append-only within schema version. Renumbering or changing payload meaning requires a schema-version change.

## Receipt

The terminal receipt includes replay identity, outcome, ticks, state digest, Player result, Exposure, combat totals, objective graph, selected Camera layout/destructions, upgrade, boss phases, and diagnostics. Arrays are ordered by their contract-defined key. A failed or invalid run still produces a receipt when state can be serialized.

The receipt is written atomically to application support as canonical JSON. Filename:

`run-<UTC basic timestamp>-<first 12 digest chars>.json`

UTC filename time is metadata only and excluded from digest. Keep the newest 50 receipts; deletion order is creation metadata ascending then filename. No cloud sync or analytics upload exists.

## Replay

A replay contains the four-part version identity, seed, normalized commands, and optional expected final digest. Commands are strictly increasing by tick with no duplicates. Upgrade choice is present only on the protected selection tick. Replays contain no touch positions, render frames, wall time, audio, haptics, or tutorial presentation.

Execution fails before tick 1 for unknown versions, invalid JSON/schema, unsupported integer range, or invalid seed. Mid-run digest mismatch terminates with `diagnosticFailure`; it never attempts repair.

## Result screen

FR-045 separates diagnostic receipt evidence from player-facing presentation.
The receipt fields above remain required by the schema; they are not a list of
required visible fields. D-081's terminal card (run-shell.md § 11) shows the
date, time, Camera count/Network Blackout, highest Detection State and eligible
success-only ghost comparison under the outcome. D-095 adds the earned-medal
row and NEW marking (§ 12). Numeric Exposure, seed and replay/version identity
remain evidence-only, not additional card rows or a required replay/digest copy
control. Share is limited to the D-112 incident-report fields (§ 11), with no
seed, receipt or identifier. Court rehearsal follows D-107 (§ 14.3): Court-time
card only, no medals, no Share and no receipt archive.

## Acceptance vectors

| ID | Scenario | Expected |
|---|---|---|
| ER-001 | same replay on supported devices | identical ordered events and digest |
| ER-002 | UInt64 entity ID | lossless decimal string round-trip |
| ER-003 | unknown version | reject before tick 1; typed diagnostic |
| ER-004 | duplicate command tick | invalid replay |
| ER-005 | failed run after Camera destruction | destruction retained in receipt |
| ER-006 | 51st stored receipt | oldest receipt deleted only after new atomic write |
| ER-007 | audio/tutorial/settings change | authoritative receipt/digest unchanged except declared presentation metadata |
| ER-008 | canonical JSON round-trip | byte-identical canonical form |

## D-103 — combat causality

See [combat-causality.md](combat-causality.md) for collision, damage evidence, weapon anchor, upgrade clarity and bounded history. CC-001–CC-007 cover phases 1–2; CC-008 remains phase 3.
