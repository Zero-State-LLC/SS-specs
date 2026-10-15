# Implementation Tasks

Status: READY_FOR_REVIEW  
Feature: SS-001

Tasks are ordered. Runtime implementation belongs in the future runtime repository.

## Phase 0 — Specification and repository boundary

- [x] T000 Record iPhone-only, iOS 18, landscape, touch, and device-matrix decisions.
- [x] T001 Record 60 Hz simulation and physical-device frame-time thresholds.
- [x] T002 Reserve `scrimshawlife-ctrl/SS` as the future runtime repository identity.
- [x] T003 Define visual, animation, arena, production, and accessibility baselines.
- [x] T004 Create annotated legacy-repository tag `legacy-multicity-2026-08-24` at accepted SHA `3b20d88d6a6e1fe8f07f45f581359d371fa65d98`.
- [x] T005 Complete cross-artifact consistency and specification-quality review.
- [x] T006 Create the runtime repository and link its first commit to the accepted specification SHA.
- [x] T007 Establish ruleset, level, replay-schema, asset-schema, arena-schema, and save-schema version policies.

- [x] T008 Lock Exposure, controller, base combat, simulation order, and version identities.
- [x] T009 Lock Camera socket randomization, enemy/encounter tables, bosses, and upgrades.
- [x] T010 Lock exact arena coordinates, solids, gates, triggers, sockets, emitters, viewport, and Extraction geometry.
- [x] T011 Lock HUD/tutorial, audio/haptics, event catalog, replay, receipt, and presentation asset identities.

## Phase 1 — Legacy admission

- [x] T100 Record observed immutable legacy paths and evidence limits for LC-001 through LC-010.
- [ ] T101 Recover tests and dependency boundaries for deterministic kernel candidates.
- [x] T102 Classify campaign, procedural district, challenge, and non-SF content as excluded.
- [x] T103 Classify SF assets individually with provenance and runtime relevance.
- [x] T104 Record ADMIT, ADAPT, REWRITE, or REJECT for every candidate.
- [ ] T105 Stop legacy migration when any copied source lacks an approved record.

## Phase 2 — Deterministic kernel

- [x] T200 Implement fixed-step SimulationClock.
- [x] T201 Implement seeded random generator with golden sequence tests.
- [x] T202 Define stable entity IDs and ordered iteration rules.
- [x] T203 Define normalized tick-indexed player commands.
- [x] T204 Implement replay envelope loading and incompatibility errors.
- [x] T205 Implement final state digest and first golden replay fixture.
- [x] T206 Verify restart restores the initial authoritative state.

## Phase 3 — Grayscale arena blockout

- [x] T300 Define arena, zone, collision, Camera, navigation, and spawn schemas.
- [x] T301 Build the 36 × 24-cell baseline arena with seven canonical zones.
- [x] T302 Validate reachability, minimum widths, viewport margins, and Spawn Alley protection.
- [x] T303 Implement collision, Camera, spawn, safe-area, and density debug overlays.
- [x] T304 Build SE-class and standard-iPhone HUD blockouts for both handedness modes.
- [ ] T305 Run first-run and competent-run pacing probes.
- [ ] T306 Freeze the accepted blockout before final environment production.
- [x] T307 Establish diagonal spine, three-grid collision, wedge parcels, and landmark sightlines.
- [x] T308 Validate Civic Seam identity without labels or literal map reproduction.

## Phase 4 — Surveillance and combat blockout

- [x] T400 Implement Camera data, deterministic LOS, and occlusion.
- [x] T401 Implement Exposure, recovery, thresholds, state cues, and Lockdown latch.
- [x] T402 Render Camera fields from authoritative data.
- [x] T403 Implement deterministic target selection, base attack, damage, and death.
- [x] T404 Implement projectile pooling with complete lifecycle reset.
- [x] T405 Implement standard-enemy blockouts with distinct silhouettes.
- [ ] T406 Profile peak density on iPhone 12 and decide D-021 ceilings.
- [x] T407 Validate spawn fairness and visual escape corridors.
- [x] T408 Author at least 18 Camera sockets; deterministically select exactly eight by seed/quota and assert selected transforms/fields remain immutable.
- [x] T408B Exhaustively validate every legal Camera selection and implement CP-001 through CP-010.
- [x] T408A Implement Camera Integrity 3→2→1→0 and exact damage eligibility.
- [x] T409 Implement Camera-aware automatic-target priority and stable tie-breaking.
- [x] T410 Implement destruction contact removal, +100 Tamper, and Lockdown transition order.
- [x] T411 Implement permanent per-run Camera destruction with complete restart restoration.
- [x] T413 Implement Network Blackout counter, eighth-destruction event, partial receipt, and accolade.
- [x] T414 Prove Camera state never enters the Extraction predicate.
- [x] T412 Implement CD-001 through CD-012 golden vectors.

## Phase 5 — Visual language and asset pipeline

- [x] T500 Establish role palette, shape language, contact points, and salience hierarchy.
- [x] T501 Implement asset manifest and provenance validation.
- [x] T502 Implement deterministic naming, dimensions, alpha, sRGB, content, duplicate, and atlas checks.
- [ ] T503 Produce Player, standard-enemy, Improper Search Daemon, Algorithmic Moderate, Camera, objective, and upgrade silhouette sheets.
- [ ] T504 Produce grayscale, color-vision, dense-combat, and reduced-presentation review plates.
- [ ] T505 Establish bounded atlases and preload measurements.
- [ ] T506 Approve the minimum asset inventory before polish assets.
- [x] T507 Produce the six Civic Seam Camera housing families.
- [ ] T508 Produce architectural module sheets and recombination tests.
- [x] T509 Produce the original phoenix, repair, human-counter-signal, and broadcast-glyph motif sheets.

## Phase 6 — Animation and VFX

- [x] T600 Implement clip metadata and authoritative event markers.
- [x] T601 Produce minimum Player clips.
- [x] T602 Produce the five standard-enemy clip families.
- [x] T603 Produce the finite Captain animation and telegraph vocabulary.
- [x] T604 Implement bounded procedural VFX and reduced variants.
- [x] T608 Produce Camera operational, damaged, critical, destroyed, dormant, hit, and field-off presentation.
- [x] T609 Implement first-encounter Camera tutorial, Integrity notches, and +100 TAMPER feedback.
- [x] T610 Integrate Camera hit, critical, destruction, network-tamper, and field-off audio events.
- [x] T605 Verify anchors, mirroring, interruption, cancellation, and event alignment.
- [x] T607 Implement bounded Civic Seam ambient motion with seeded cosmetic scheduling.
- [ ] T606 Measure animation, VFX, draw, and transient-node budgets on iPhone 12.

## Phase 7 — Upgrades, Captain, and Extraction

- [x] T700 Implement protected upgrade selection.
- [x] T701 Implement Signal Jammer, Ricochet Pulse, and Ghost Step.
- [x] T702 Implement Captain phases and defeat.
- [x] T703 Implement the three-mob → Improper Search Daemon → Algorithmic Moderate → Extraction objective graph.
- [x] T703A Implement Extraction locking, countdown, reset-on-exit, and completion.
- [x] T704 Implement terminal precedence and immutable result records.
- [x] T707 Add Camera destruction/Network Blackout receipt summary and ordered destruction entries.
- [x] T708 Add canonical combat-authority and boss-phase receipt fields.
- [x] T705 Add complete-run golden vectors for every upgrade.
- [x] T706 Verify every upgrade completes the level without exploits.

## Phase 8 — Final San Francisco production

- [x] T800 Produce approved Civic Seam P0 modular environment families.
- [x] T801 Integrate only runtime-reachable SS-001 assets.
- [ ] T802 Perform Civic Seam P1 identity pass without weakening affordances.
- [ ] T806 Add P2 polish only after P0/P1 device acceptance.
- [x] T807 Verify no prohibited landmark, seal, logo, copied artwork, or geographically incoherent shorthand ships.
- [x] T803 Complete audio, haptic, HUD, and objective presentation.
- [ ] T804 Pass asset provenance and device acceptance.
- [x] T805 Remove unreachable, duplicate, source, and non-SF assets from the bundle.

## Phase 9 — Acceptance

- [x] T900 Instrument frame time, memory, thermal state, entities, particles, Exposure, damage, and outcomes.
- [ ] T901 Pass deterministic replays across the supported matrix.
- [ ] T902 Pass functional, visual, arena, animation, accessibility, and edge-case gates.
- [ ] T903 Run onboarding comprehension playtests.
- [ ] T904 Run voluntary-replay playtests with at least five external participants.
- [ ] T905 Run three consecutive physical-device complete runs on the performance floor.
- [ ] T906 Fix all severity-one and severity-two defects.
- [ ] T907 Record release-candidate evidence.
- [ ] T908 Decide whether the expansion gate passes.

## Evidence (2026-09-01 reconciliation)

Checked tasks link to the runtime pull request or commit that carries their verification. Tasks whose text is *run*, *record*, *measure*, *pass*, or *decide* stay open until the artifact exists; harnesses for them (T901–T908) exist in SS-runtime #34–#41 but are not evidence.

| Task | Evidence |
|---|---|
| T004 | tag `legacy-multicity-2026-08-24` (`e085ea8`) |
| T006 | SS-runtime `7e04ef1` |
| T007 | SS-runtime `SPEC_BASELINE.md`, `ContractVersions.swift` (`7e04ef1`) |
| T103 | SS-runtime `b8d3467` |
| T200 | SS-runtime `913b62a` |
| T201 | SS-runtime `913b62a` |
| T202 | SS-runtime `913b62a` |
| T203 | SS-runtime `913b62a` |
| T204 | SS-runtime `913b62a` |
| T205 | SS-runtime `913b62a` |
| T206 | SS-runtime `913b62a` |
| T300 | SS-runtime `913b62a` |
| T301 | SS-runtime #83 (`ad4a52a`) — `CanonicalArenaZonesTests`: grid, 64-unit cell, and each zone's id, order, and trigger rectangle against `arena-layout.md` |
| T302 | SS-runtime `11d69ff` |
| T303 | SS-runtime `92fff69` |
| T304 | SS-runtime `92fff69` |
| T307 | SS-runtime `9a937b1` |
| T308 | SS-runtime `9a937b1` |
| T400 | SS-runtime `913b62a` |
| T401 | SS-runtime `92fff69` |
| T402 | SS-runtime `92fff69` |
| T403 | SS-runtime `92fff69` |
| T404 | SS-runtime `92fff69` |
| T405 | SS-runtime #6 |
| T407 | SS-runtime #8, #11 |
| T408 | SS-runtime #7 (`CameraPlacementTests`) |
| T408B | SS-runtime #7 |
| T408A | SS-runtime #2 (`CameraDestructionOrderTests`, `KernelVectorTests`, `GrayscaleSystemsTests`) |
| T409 | SS-runtime #9 |
| T410 | SS-runtime #10 |
| T411 | SS-runtime #12 |
| T412 | SS-runtime #15 |
| T413 | SS-runtime #13 |
| T414 | SS-runtime #14 |
| T500 | SS-runtime `11d69ff` |
| T501 | SS-runtime `b8d3467`, `11d69ff` |
| T502 | SS-runtime `11d69ff` |
| T509 | `asset-catalog-001`: `env_motif_phoenix`, `env_motif_repair`, `env_motif_counter_signal`, `env_motif_broadcast_glyph` — `originalAccepted`, `projectOriginal`, SHA-256 on all four. Delivered as runtime motif assets, not multi-variant sheets |
| T600 | SS-runtime #16 |
| T601 | `asset-catalog-001`: 144 `actor_player_*` frames — idle, move, dodge, recover, hurt, defeat, extraction, complete (the `animation.md` §3 Player machine), each in four directions (D-018). 48 `originalAccepted` + 96 `adaptedAdmitted` (bounded ADAPT, D-065); SHA-256 on all |
| T603 | `asset-catalog-001`: 172 `actor_algorithmicModerate_*` frames — the four `bosses.md` attacks (Safety Rationale, Narrow Tailoring, Temporary Order, Independent Review), phase transition, stagger, defeat, four directions each — plus `telegraph_*` for all four attacks; all `originalAccepted`, SHA-256 on all. `clip-metadata-001` binds all seven clips to authoritative event markers |
| T604 | SS-runtime #17 |
| T605 | SS-runtime #21 |
| T607 | SS-runtime #22 |
| T608 | SS-runtime #18 |
| T609 | SS-runtime #19 |
| T610 | SS-runtime #20 |
| T700 | SS-runtime #83 (`ad4a52a`) — `ProtectedUpgradeSelectionTests`: selection opens from genuine M-A completion through `step()`; neutral-movement, Dodge, and missing-index refusal; frozen clock; one-tick acceptance. Mutation-verified |
| T701 | SS-runtime #23 |
| T702 | SS-runtime #24 |
| T703 | SS-runtime #25 |
| T703A | SS-runtime #26 |
| T704 | SS-runtime #27 |
| T705 | SS-runtime #30 |
| T706 | SS-runtime #30 |
| T707 | SS-runtime #28 |
| T708 | SS-runtime #29 |
| T801 | SS-runtime #33 |
| T803 | SS-runtime #31 |
| T805 | SS-runtime #32 |
| T807 | SS-runtime #32 |
| T900 | SS-runtime #34 |

T301 and T700 were implemented but uncited until SS-runtime #83 (merged 2026-09-23) added verification that exercises what each task claims; with that PR's tests absent, deleting the selection's neutral-movement and Dodge guards left all 420 prior tests passing. Range citation `T303-T404` (`92fff69`) is not accepted for T305/T306, which have no pacing or freeze artifact.

## Open task reconciliation (honest gap)

**Art reconciliation (2026-09-23).** T509, T601, and T603 were recorded `NOT_PRODUCED` on 2026-09-09 (#27) without a cross-check against `asset-catalog-001`, which already held their delivered, admitted, hashed assets. Closed above on that catalog evidence. Its three open observations are resolved: the Captain vocabulary by D-068 (the generic names had already been retired from `animation.md` in #6 on 2026-09-04 — that observation was mistaken), self-referencing reduced-motion clips by D-069, and the retired Guard and Interceptor roles by D-070.

The 25 unchecked tasks above are **not agent-closable**. Each is a *run*, *record*, *measure*, *decide*, or *produce* item whose closure needs an input this specification does not own, and none of them may be closed on the strength of a harness. They group into six kinds, each with its required owner or input:

- **Device (iPhone 12 performance floor / supported matrix)** — T406, T606, T901, T905.
- **Human judgment / decision** — T306, T506, T802, T804, T806, T907, T908 (the expansion gate and any D-register decision require the owner specialist, Danny).
- **Artist / production** — T503, T504, T505, T507, T508, T602, T800.
- **Legacy archaeology** — T101, T105.
- **Developer (defect closure)** — T906.

A harness is a collector of evidence, not evidence. SS-runtime #34–#41 ship the peak-density profiler, replay matrix, playtest loader, gate registry, defect registry, release-evidence store, and expansion-gate report; each stays a collector until it has captured a real device run, a named participant, or a recorded decision. The pending decisions **D-020** (which physical devices are approved equivalents for the four device classes) and **D-021** (the exact measured ceilings) remain `DECISION_PENDING` and MUST NOT be replaced with invented answers; they block the device-class tasks until the owner records them.

**What counts as evidence:** a linked device capture or profile, a recorded playtest naming its participants, a recorded decision, a delivered asset carrying `asset-record-001` provenance, or a runtime PR that cites the task ID and links its verification. Until one of these exists and is linked, the task stays open.

| Task | Status | Blocker | Required owner / input | Evidence required |
|---|---|---|---|---|
| T101 | NOT_RUN | Legacy test suite and build environment at the frozen SHA `3b20d88` are NOT_COMPUTABLE; deterministic-kernel tests are unrecovered | Developer with legacy-repo access performs the recovery; owner specialist approves | A recovered, runnable deterministic-kernel test suite with recorded results at the frozen SHA |
| T105 | STANDING_GATE | Legacy migration is not complete; the gate is active until every copied source is approved | Every copied source carries an approved record before migration closes (owner specialist Danny) | An approved record per copied source (asset-record / admission decision) plus a migration-close note |
| T305 | PARTIAL | Scripted probes only ([`docs/review/T305`](../../docs/review/T305/README.md), SS-runtime `06561a9`): 240 headless bot runs, seeds 1–20. Completed runs last 3:02–6:40 (median 3:43 for the 7 legal `competent` successes) against the then-current 8–12-minute target (superseded by D-079). No person has played a probe, so first-run learning time and competent human pace are unmeasured; the `T303-T404` range citation is not accepted | Designer / player runs the probes on a device (owner specialist Danny) | Recorded human pacing probes compared against the current `E-011` 5–8-minute target (D-079, later pacing refinements D-090/D-093/D-101) |
| T306 | NOT_DECIDED | The blockout freeze is a human judgment, pending pacing (T305) and density ceilings (T406) | Designer accepts the freeze (owner specialist Danny) | A recorded freeze decision referencing the pacing and density evidence |
| T406 | NOT_RUN | Peak-density profiling on an iPhone 12 (performance floor, D-011) is not run; D-021 ceilings are DECISION_PENDING | iPhone 12 device plus a human owner who settles D-021 | A device profile (resident memory, atlas memory, frame time) and a D-021 decision record |
| T503 | NOT_PRODUCED | The silhouette sheets are not produced | Artist delivers the sheets; intake records `asset-record-001` provenance | Delivered Player, standard-enemy, Improper Search Daemon, Algorithmic Moderate, Camera, objective, and upgrade silhouette sheets with provenance |
| T504 | NOT_PRODUCED | The review plates are not produced | Artist produces the plates | Delivered grayscale, color-vision, dense-combat, and reduced-presentation review plates with provenance |
| T505 | NOT_MEASURED | Bounded atlases and preload measurements are not recorded | Runtime builds the atlases and measures preload on a device | Bounded atlases plus a recorded preload measurement |
| T506 | NOT_DECIDED | Approving the minimum asset inventory is a human judgment | Designer / owner approves the inventory (owner specialist Danny) | A recorded approval decision for the minimum asset inventory |
| T508 | NOT_PRODUCED | The architectural module sheets and recombination tests are not produced | Artist produces the sheets; runtime adds the recombination tests | Delivered module sheets plus passing recombination tests |
| T606 | NOT_MEASURED | Animation, VFX, draw, and transient-node budgets are not measured on an iPhone 12 | iPhone 12 device | Recorded budget measurements on an iPhone 12 |
| T802 | NOT_PERFORMED | The P1 identity pass is not performed and must not weaken affordances | Artist performs the pass; human confirms affordances hold | A completed P1 pass plus a human judgment record |
| T804 | NOT_PASSED | Asset provenance and device acceptance have not passed | Device plus a human acceptance decision | Recorded device-acceptance results plus a provenance check |
| T806 | BLOCKED | P2 polish is allowed only after P0/P1 device acceptance (T804) | P0/P1 device acceptance lands first, then artist adds P2 | P0/P1 device-acceptance evidence before any P2 polish |
| T901 | PARTIAL | RM-001, the golden vectors, and a 9227-tick piloted replay pass on macOS arm64 (debug and release), macOS x86_64 under Rosetta (RM-001 and piloted replays only), and iOS Simulator 26.5 arm64 with iPhone 17, SE (3rd gen), and iPhone 12 profiles ([`docs/review/T901`](../../docs/review/T901/README.md)). No physical device has run them; D-020 is pending | The supported physical device matrix (D-020) | Linked device replay results across the matrix (B-002) |
| T902 | NOT_PASSED | Functional, visual, arena, animation, accessibility, and edge-case gates have not passed; `GateRegistry` maps gates to evidence but the evidence is not linked | Human plus device, per gate | Linked evidence for each acceptance gate (A–G) |
| T903 | NOT_RUN | The onboarding comprehension playtest is not run | Named participants plus a designer who records comprehension | A recorded playtest with a comprehension outcome |
| T904 | NOT_RUN | The voluntary-replay playtest with at least five external participants is not run | At least five named external participants | A recorded playtest from at least five external participants |
| T905 | NOT_RUN | Three consecutive physical-device complete runs on the performance floor (iPhone 12) are not run | iPhone 12 device | Three recorded consecutive complete runs on the performance floor |
| T906 | STANDING_GATE | Severity-one and -two defects are not fixed; the defect list must be found through device / playtest evidence first | Developer fixes; evidence discovers the defects | A defect registry with no open severity-one or -two defects |
| T907 | NOT_RECORDED | Release-candidate evidence is not recorded; `ReleaseEvidenceStore` is a harness, not evidence | The release owner records the evidence | A recorded release-candidate evidence bundle |
| T908 | NOT_DECIDED | The expansion-gate decision is a human judgment, gated on D-020, D-021, and Gates A–G | The owner specialist (Danny) decides | A recorded expansion-gate decision referencing D-020/D-021 and the gate evidence |
| T1042 | PARTIAL | Shared composition/projection/geometry fixtures and south source evidence exist; controlled four-facing master and full HUD/encounter acceptance remain incomplete | Artist and runtime renderer | Four-facing source, native-scale 704×326 scene with HUD and encounter, grayscale/50% views, and authoritative anchor/footprint review plate |
| T1043 | PARTIAL | Complete municipal candidate clips and state playback tests exist; production admission, full visual matrix and Captain identity remain open | Artist and runtime renderer | Complete-device frames, metadata, provenance, state playback and single-device renderer verification |
| T1044 | NOT_RUN | Production frames are not accepted, so clip/catalog/manifest migration cannot be finalized | Spec and asset intake owner after accepted delivery | Validated frame IDs, metadata, hashes, parity and bundle exclusion receipt |
| T1045 | PARTIAL | Preferred narrow-stance south source, 16 poses and initial live capture exist; detail defects, full-cycle contact, facings and complete state coverage remain open | Artist and animation reviewer | Four-facing 16-frame locomotion proof where applicable plus all required action clips and timed playback review |
| T1046 | PARTIAL | Family-level inventory found defects; per-ID disposition and in-scene base/footprint proof remain | Environment artist and runtime reviewer | 46-item disposition, repaired sources, native-scale traversal and collision review plates |

## Traceability rule

Every runtime pull request MUST cite task IDs and affected requirement or gate IDs. A task closes only when its verification evidence is linked.

## D-102 correction verification

Implementation and automated evidence: [SS-runtime PR #116](https://github.com/Zero-State-LLC/SS-runtime/pull/116). The requirements below do not close physical-device or playtest gates.

- T301 / PC-009: verify normalized touch movement, one-shot Dodge, pause/resume, and restart through the app scene in Debug and Release.
- T410 / EX-017–EX-020: verify final Exposure transitions, quiet latching after named pulses, Signal Jammer, lethal precedence, and M-C exemption.
- T705: verify the corrected transition reaches audio/VFX projection.
- T900/T901: review ruleset-007 golden differences, reject ruleset-006, run core tests and byte parity. Physical-device matrix evidence remains open.

## D-103 — combat causality

See [combat-causality.md](combat-causality.md) for collision, damage evidence, weapon anchor, upgrade clarity and bounded history. CC-001–CC-007 cover phases 1–2; CC-008 remains phase 3.

- T1030: D-103 contract and identity/fixture review.
- T1031: wall/actor integration regressions and repair (CC-001).
- T1032: damage evidence and honest impact rendering (CC-002/003).
- T1033: related ricochet traces and bounded history (CC-004/005).
- T1034: copy, replay rejection and full core/app validation (CC-006/007).
- T1035: accepted phase-3 presentation/accessibility (CC-008): event-backed discharge and independent aim, conditional Jammer contour, actual Ghost Step boundary, protected SwiftUI cards with VoiceOver activation and Dynamic Type scrolling. Verify automated tests before art/device testing; physical acceptance remains open.

## D-104 — phase-4 visual contract and staged art work

- [x] T1040 Record accepted visual intent, user-selected street-corner reference, midpoint projection study and visual decision; link both concept images as references, not runtime admission.
- [x] T1041 Define shared projection, player identity, role/equipment language, one visible municipal standard-camera family, logical-family replay preservation and 16 distinct locomotion frames per applicable facing in spec/plan/acceptance.
- [ ] T1042 Validate a four-facing hooded-player model and one representative player/building/camera/prop/ground scene in the actual 704×326 game view with HUD and encounter sample, including collision/base overlay, native/50% scale and no-color views. Compare costume and projection candidates against the selected image using the [design-choice research](../../docs/review/phase4/design-choice-research.md). The generated concept is direction evidence only.
- [ ] T1043 Produce registered municipal complete-device clips with persistent Integrity states, reduced presentation, exact mount and provenance. Reconcile Captain emitter appearance and asset IDs. Camera renderer integration belongs to the next implementation phase.
- [ ] T1044 Revise affected clip metadata, frame IDs, presentation manifest and asset catalog when accepted production assets are ready; validate source/delivery hashes and bundle exclusions.
- [ ] T1045 Complete actor state/facing coverage with controlled 16-frame locomotion where applicable; run timing, identity, anchor and gameplay-scale review before device testing.
- [ ] T1046 Audit each of the 46 environment PNGs for retain/repair/replace/exclude and validate visible base against collision geometry in the shared scene.

Production detail: [BP-001–BP-006](benchmark-production.md). T1042 owns exact viewport/HUD/encounter captures and projection comparison. T1043 owns complete-device state settling, interruptions and Reduced Motion. T1044 begins with exact spec-pin adoption and records deferred art admission honestly, then migrates complete accepted families. T1045 owns the named locomotion matrix, rational cadence/hold representation and Informant pursuit decision. T1046 records all 46 per-ID dispositions and geometry evidence. Do not close any task on the strength of pin alignment alone.

T1046 next evidence: ground-plan source and matching elevated render with wall base, steps, planters and walkable apron separated. Current building registration fails; see [measured review](../../docs/review/building-registration/review.md). Hidden rear vertices and art admission remain open.

T1042 / T1046 remain open for BP-009: current isolated contacts expose false roof elevation. Complete ground-cue comparison and continuous rear/front/corner transitions before implementing/admitting a general occlusion treatment.

T1044 / T1045 timing prerequisite: implement against clip-metadata-002.schema.json; run scripts/validate_clip_timing_migration.py and the runtime exact-vector/malformed-record tests. Target schema publication does not close either task or switch active delivery.

T1044 / T1045 one-shot prerequisite: implement the event-facing/occurrence/elapsed-phase policy in animation-timing-migration.md. Cover unequal direction durations, repeat events, late visibility, cancellation, fallback, pause and reset. No active v2 migration until this integration and renderer tests pass.

T1045 source prerequisite: record the controlled-source pilot project, evaluated limb/contact measurements and explicit visual limitations; complete the benchmark costume and four-neutral-facing gate before expanding locomotion. See [pilot](controlled-character-source.md). Accepted production coverage remains NOT_PRODUCED; source progress is PARTIAL.

T1044 / T1042 high-resolution outline prerequisite: resolve runtime #124 under BP-007 before admitting the painted 384px Player. Capture equivalent 64/256/384 source silhouettes at identical logical size/anchor; verify Player and enemy stroke/dash consistency, noncentral anchors, alpha margins, normal and Reduced Motion frame changes, unsupported-source cleanup and bounded cache churn. Include native/zoom comparison and measured allocation/residency evidence. These requirements do not mark the candidate artwork, animation or shared scene accepted.

T1042 / BP-010 remains open: compare opaque, reduced-opacity and no-added-outline Player treatments in the real renderer; evaluate the specified native/grayscale, backdrop, motion, dense encounter, damage, occlusion and Reduced Motion matrix. Record the visual decision and non-colour faction proof before coordinating production contract/runtime changes. The user questioning the glow is evidence of a design concern, not approval of a particular replacement.

T1045 layered-source prerequisite: complete the setup-pose/part-ownership and joint-range checks in controlled-character-source.md; include the elevated-motion keys and authored foot-contact model; keep production acceptance open until the existing full animation and renderer evidence is satisfied.

T1045 / BP-008 evidence clarification: the moving comparison must record post-action displayed frames with simulation and rendered positions, retain playback without per-sample fixture resets, and demonstrate that textures actually change. Static review-art injection and continuous source contact alone do not close gait acceptance. Include stop/start, reversal and interruptions without treating any proposed phase policy as accepted.

T1045/T1046 remaining evidence includes the BP-001/BP-010 Camera field contrast comparison in benchmark-production.md: exact-path control/dark/paired contours; backdrop, overlap, occlusion, Captain, state and motion-mode matrix; lifecycle checks; native/50%/grayscale and legal/dense encounter review. Runtime ecac1ef exposes the pale-ground grayscale defect; it does not close field readability.

T1042/T1046 remain open for the BP-001 street-surface comparison: separate asphalt/pedestrian paving and continuous curb/embedded rails, record authored parameters, verify reset and unchanged authority, then integrate with the legal arena rail spine before admission.

2026-10-15 reconciliation: [status and ordered plan](../../docs/review/benchmark-status-2026-10-15.md), [repository kanban](../../docs/kanban.md). User prefers narrowed stance plus alternating arms; dimensions/amplitudes and hidden surfaces remain proposed. All T1042–T1046 checkboxes remain open.
