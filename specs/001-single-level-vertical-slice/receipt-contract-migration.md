# Receipt contract migration

Status: CANONICAL
Contract version: `run-receipt-002`
Decision: D-123. Intent: [accepted receipt reconciliation](../../intent/2026-11-15-receipt-contract-reconciliation.md).

## Observable contract

New terminal diagnostic writes MUST declare `run-receipt-002` and conform to [the strict v2 schema](../../contracts/run-receipt-002.schema.json). Success, failure and invalid outcomes are covered when state can be serialized. A missing selection is `upgrade: null`; a selection is exactly `{ "id": "signalJammer", "contractVersion": "upgrades-003" }`, with `ricochetPulse` and `ghostStep` the other permitted IDs. A string selection is not v2.

The gameplay identity remains exactly `ss-rules-014`, `civic-seam-content-009`, `civic-seam-arena-004`, `runtime-kernel-001`. No replay, digest, gameplay ordering, Camera behavior, upgrade effect or Extraction predicate changes. Network Blackout remains optional and does not gate Extraction. FR-027, FR-045, Camera destruction §16, encounter objectives §6 and upgrade Selection all bind this shape.

## Complete serialized shape

Every field below is required. Closed objects reject undeclared properties, including nested objects. The schema defines exact types and enums. `defeatsByArchetype` is the one dynamic-key map, with nonempty archetype names and nonnegative integer counts. Counts are nonnegative, Camera counts are 0–8, and UInt64 numbers are bounded to 0–18446744073709551615. Final Integrity is signed to retain terminal evidence, including serializable invalid states.

| Path | Shape |
|---|---|
| `schemaVersion` | constant `run-receipt-002` |
| `identity` | exact `rulesetVersion`, `contentVersion`, `arenaVersion`, `replaySchemaVersion` above |
| `seed`, `elapsedTicks` | UInt64 integers |
| `outcome`, `finalDigest` | success/failure/invalid, lowercase 64-hex digest |
| `player` | integer `finalIntegrity`, counts `damageTaken`, `integrityRestored` |
| `exposure` | counts `final`, `peak`, Detection State `finalState`, boolean `lockdownEntered` |
| `combat` | count `damageDealt`, count map `defeatsByArchetype` |
| `objectives.combatAuthority` | `mobEncountersComplete` 0–3, `mobEncountersRequired` 3, `currentNode`, `elite`, `boss`, boolean `complete` |
| `objectives.combatAuthority.currentNode` | M-A/M-B/M-C/improperSearchDaemon/algorithmicModerate/extraction |
| `objectives.combatAuthority.elite` | `id` improper-search-daemon, boolean `defeated` |
| `objectives.combatAuthority.boss` | `id` algorithmic-moderate, boolean `defeated`, phase array `phasesReached` |
| `objectives.networkBlackout` | Camera count `camerasDestroyed`, `camerasTotal` 8, boolean `complete` |
| `objectives.extractionArmed` | boolean, no replacement `extraction` object |
| `cameraPlacement` | `version` camera-placement-001, UInt64 `placementSeed`, array `selectedSockets` |
| `cameraPlacement.selectedSockets[]` | nonempty string `socketId`, UInt64 numeric `cameraEntityId`, housing enum `housingFamily` |
| `cameraDestructions[]` | decimal-string `cameraId`, UInt64 `tick`, housing enum `housingFamily`, boolean `wasDetectingPlayer`, nonempty string `source`, counts `exposureBefore`/`exposureAfter`, boolean `triggeredLockdown` |
| `camerasDamaged`, `camerasDestroyed`, `tamperExposureApplied` | Camera counts and cumulative Tamper Exposure count |
| `cameraObjective` | Camera count `destroyed`, `total` 8, boolean `complete` |
| `upgrade` | null or exact ID/contract-version object above |
| `boss` | phase array `phasesReached`, boolean `defeated` |
| `diagnostics` | array of DiagnosticCode raw strings defined by the schema |
| `presentation` | booleans `tutorialsEnabled`, `reducedMotion`, `reducedFlash`, `reducedSensory`, `hudScale` 1000/1150/1300, `handedness` right/left |

Housing values remain municipalDome/storefrontCamera/trafficReader/ornamentalCivicCamera/temporarySensorMast. Phase arrays retain canonical publicSafety/civilLiberties/temporarySafeguard/independentReview order without duplicates. Destructions sort by tick then numeric Camera ID; socket entries sort by UTF-8 socket ID. Decimal Camera IDs must fit UInt64. The numeric placement ID representation is preserved, not silently changed to a string.

Semantic checks supplement structural schema validation: duplicated Camera summary counts and objective counts agree with their authoritative projections, both boss phase projections agree, and no Camera completion requirement is added to Extraction. The schema is not a substitute for these existing assertions or deterministic replay evidence. It does not invent fixed eight-item placement requirements for serializable invalid states.

## Archive compatibility

The historical `run-receipt-001.schema.json` bytes MUST remain unchanged. Archive reads preserve original bytes and declared identities. A v1 archive is readable with `formatStatus: .historicalUnverified` (**historical-unverified**), including legacy receipts that do not conform to that historical schema. It is never relabeled, repaired, or certified as v2.

A v2 archive read returns `formatStatus: .currentUnverified` and recognizes the identity only. Reading alone does not certify schema conformance. Unknown, malformed, non-string or missing schema identities, malformed JSON and non-object roots are reported with `formatStatus: .unrecognized` (**unsupported/unrecognized**), with original bytes untouched. Recognition is not validation. No automatic conversion, deletion or rewrite is authorized by this migration. Normal existing retention still applies.

New archive writes accept only the current v2 identity. A caller-mutated v1, unknown or missing writer identity is rejected, not normalized or silently stamped v2. Keep canonical JSON, existing atomic write behavior, filename convention, and newest-50 retention, including eviction only after a successful new write. No general JSON Schema engine is required in Swift. Independent schema validation of real serialized output supplies conformance evidence, not archive-read classification.

## Acceptance matrix

| ID | Required evidence |
|---|---|
| RC-001 | Actual runtime serialization for success, failure and serializable invalid runs validates against the exact bundled v2 schema. |
| RC-002 | Each of three selections validates as exact ID plus upgrades-003, and no-selection validates as null. Strings, unknown IDs, missing contractVersion and extra fields fail. |
| RC-003 | Missing root/nested evidence, extra root/nested keys, malformed types/enums, unknown schema/gameplay identities and UInt64 overflow fail independent validation. |
| RC-004 | Camera summaries, partial and complete Network Blackout, ordered destructions, extractionArmed and both boss phase projections retain existing semantic assertions. No Extraction gameplay condition changes. |
| RC-005 | Legacy v1 bytes read with `formatStatus: .historicalUnverified`, including the recorded nonconformant legacy shape; v2 reads use `.currentUnverified`, not certification. Unknown/malformed/missing identities report `.unrecognized` without rewriting bytes. |
| RC-006 | New writes use v2 only; caller-mutated unsupported writer identity fails before archive creation or retention mutation. Atomic writes and the 51st-receipt eviction contract pass unchanged. |
| RC-007 | Existing replay/golden-state and settings-separation tests pass without changed expected gameplay digests, identities or weakened assertions. |
| RC-008 | v1 schema bytes remain identical to the historical baseline; registry and bundled v2 schema match. Consumer inventory covers writer, local archive reader, contract loader/parity and diagnostic validators. External consumers remain NOT_COMPUTABLE until inspected. |

## Implementation order and evidence status

Specification and schema precede runtime adoption. Update serializer and registry bundle, classify archive identity without certification, then independently validate actual output across RC-001–RC-008. Runtime acceptance remains unproven until evidence is recorded. This diagnostic repair does not close device, art, playtest or expansion gates.
