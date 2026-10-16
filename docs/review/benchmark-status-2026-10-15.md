# Benchmark production: status and next steps

Updated 2026-10-15. Planning/evidence reconciliation, not a new product contract or art admission. Governing requirements remain D-104 / BP-001–BP-010. Historical committed evidence through 241a1ef is supplemented by the local 2026-10-15 reports below; runtime production spec pin remains d602775. Local reports are not assumed published. The [kanban](../kanban.md) mirrors this sequence and the [canonical tasks](../../specs/001-single-level-vertical-slice/tasks.md).

## Direction retained

**OBSERVED — user preference:** the narrower-stance, alternating-arm version is much better. Preserve the hooded player and urban street-theater identity. Improve the retained source; do not replace the preferred motion direction during detail repairs. This preference does not approve the numerical 8-unit stance, 4/10px elbow/hand displacement, hidden surfaces, production size, other facings or device performance.

**OBSERVED — inspection:** normal (0.5s) and quarter-speed (2s) modes were inspected separately using browser playback samples, all 16 exported poses, detailed keys and seam onion skin. Knee pads become cup-like; calf folds look stretched; boot shafts are flat beside bright toe caps; coat overlap lacks depth; hands alternate but elbow/glove articulation remains limited. Inspected front/rear boot keys assign laces to the tongue, not the heel. No exceptional 16→1 reset was found, but neither pixel differences nor sampled playback establish final smoothness or planted-foot contact. Runtime review: `241a1ef` (local commit; not yet published).

## Latest local evidence — supersedes earlier capture limitations

OBSERVED: runtime docs/review/reduced-motion-validation records two app runs, each 113 executions / 111 named tests passed. Three independent Reduced Motion captures in each run observed all 16 frames, with and without recording. The review harness now reuses its rendered snapshot for telemetry. Median/p95 callbacks were 16.67 ms; isolated recorded maxima reached 40.66 ms. This is simulator callback evidence, not physical scanout or sustained device acceptance. Older recorded failures remain retained.

OBSERVED: initial scene preparation, texture preload and prepared outlines are tested in the candidate fixture. Loading cost remains separately reported. The latest full core run passed 773 tests / 109 suites; the subsequent harness-only change reran five ClipTimingTests plus the app suites. No shipping startup admission is claimed.

OBSERVED: the owner said the clean silhouette looks better and requested less twiggy legs. A separate fuller-leg source study has 16 unique frames, preserved pose samples, stance, arm/coat assembly and knee-pad detail. All 32 projected knee centers have opaque finite surfaces. Changes start in the lower-body region; source parameters remain proposed. That volume-only study was staged in test assets, then superseded for review after owner feedback about excessive knee rise. The lower-recovery experiment retains its volume and reduces airborne clearance with fixed-length IK. Its 16 PNGs and matching poses are now reconciled into the test-only renderer fixture; fresh validation is in progress. Prior all-frame evidence applies to the previous candidate only.

Outstanding: lower-recovery motion/volume review and fresh renderer evidence; annotated contact and full interaction matrix; shared scene; distinct facings and full cast/action scope; admission and device QA. Do not mark T1042–T1046 complete.

## Historical evidence (retain provenance)

- Editable south source and 16 distinct frames, narrowed stance and opposing arm motion: runtime 718b392. Source remains proposed, not production accepted.
- Canvas/projection preflight ae5fecc: source 384×416, root (192,336); test fixture preserves aspect at 64×69⅓ and anchor (0.5, 1−336/416). These remain comparison parameters.
- Live source integration 88e79e8 uses WorldRenderer, SpriteLibrary exact half-second timing and GameSession. Final capture has 32 post-action records through tick 90, but only frames 0 and 15 before boundary stop. Full gait/contact is unproven.
- Core: 773 tests / 109 suites passed; simulator: 107 executions / 105 named tests, zero failures. These validate the recorded candidate, not visual completion, Release parity or physical performance.
- Municipal camera candidate clips, integrity settling and complete-device test integration exist. They are no longer merely concept keys. Captain appearance, complete visual matrix and production admission remain open.
- Registered building/ground, occlusion, outline and field-contrast comparisons exist as isolated fixtures. Full consistent shared scene and legal/dense encounter acceptance remain open.
- Runtime #130 harness defects are corrected and tested locally; publication/merge and issue closure are separate. Other open issue numbers are not closed by this document.

## Ordered next steps

### 1. Polish the preferred south source — T1045

Refine knee-pad form through flexion; reconcile calf folds, trouser cuff, boot shaft and toe lighting/detail; improve elbow/glove articulation and coat/thigh overlap. Keep the preferred stance and restrained counter-swing as the baseline. Use existing source/reference influence where coherent. Author missing surfaces explicitly. Any new design choice needs appropriate primary-source research and a recorded proposal; do not present guessed anatomy or thresholds as facts.

Exit: versioned editable source, all 16 poses, isolated part/ownership views, preserved asymmetric equipment, and separate normal/quarter/frame/onion/seam review. No unexplained cut gaps, material jumps or rear-facing laces in inspected poses. Record unresolved views rather than declaring them fixed.

### 2. Measure an unobstructed live cycle — T1045 / BP-008

Preflight a legal route using actual simulation travel. Keep expensive image extraction outside the measured interval. Capture actual post-action frame identity, authoritative and rendered position, dimensions, anchor, camera/projection and frame intervals. Require observed coverage across the 16-frame cycle and repeated support phases; report skipped frames and missing candidate states. Measure annotated foot displacement only over supported observations. A single support sample is insufficient, never zero drift.

Then cover quarter/half/full input, stop/start, collision stop, wall slide, reversal, dodge and pause/resume; extend cardinal/diagonal evidence once the necessary view sources exist. Keep controller speed and gameplay authority unchanged. No new slip tolerance or phase policy is adopted by this plan.

### 3. Restore the shared benchmark scene — T1042 / T1043 / T1046

Bring the reviewed player, one municipal camera, registered building, props and continuous street surfaces together with the same ground mapping and upright-art treatment. Review native/50%/grayscale with HUD, geometry, occlusion and legal/dense encounters. Complete the outline-control/reduced/absent comparison and field-contrast matrix; preserve non-colour faction identity. Show the result before device testing. Current white-outline control is not accepted finish.

### 4. Complete facing, role and action coverage — T1045 / T1043

Reconcile four distinct neutral facings with the editable master before expanding locomotion. Complete the named six movement families at their specified durations and counts, then required action/reaction states. Preserve individual urban identities and asymmetric equipment. Deepen unresolved Civic Pulse carried-device/attachment and Informant/Captain design decisions with research; do not silently invent mechanics or reuse a wrong-facing image.

### 5. Admit complete reviewed families — T1044

After visual/source/playback evidence exists, coordinate metadata, exact durations, frame IDs, catalog, manifests, hashes, resources, spec pin and removal of superseded bundled assets. Validate parity, fail-closed timing, event-facing behavior and both Debug/Release application paths. Candidate source commits and green harness checks alone cannot authorize production admission.

### 6. Finish full QA and physical acceptance — T1046 / T9xx

Close all 46 environment dispositions and actual base/collision/projectile traversal evidence. Recheck weapons, upgrades, damage diagnostics, accessibility and complete-run pacing in the integrated scene. Measure memory/node growth and sustained performance on the specified device floor; record D-020/D-021 and Gates A–G. Preserve the user's before-device visual checkpoint. Do not close the benchmark or expansion gate on simulator evidence.

## Completion rule

Bounded source/fixture work may be done while its parent production task remains partial. Keep production admission, publication/merge, device evidence and human acceptance distinct. The whole benchmark remains open.

## GitHub tracking

Current board: [SS-specs + SS-runtime — Benchmark](https://github.com/orgs/Zero-State-LLC/projects/27). Active repository issues:

- [1. Polish the preferred south source — T1045](https://github.com/Zero-State-LLC/SS-runtime/issues/131) — SS-runtime
- [2. Measure an unobstructed live cycle — T1045 / BP-008](https://github.com/Zero-State-LLC/SS-runtime/issues/132) — SS-runtime
- [3. Restore the shared benchmark scene — T1042 / T1043 / T1046](https://github.com/Zero-State-LLC/SS-runtime/issues/133) — SS-runtime
- [4. Complete facing, role and action coverage — T1045 / T1043](https://github.com/Zero-State-LLC/SS-specs/issues/65) — SS-specs
- [5. Admit complete reviewed families — T1044](https://github.com/Zero-State-LLC/SS-runtime/issues/134) — SS-runtime
- [6. Finish full QA and physical acceptance — T1046 / T9xx](https://github.com/Zero-State-LLC/SS-runtime/issues/135) — SS-runtime

## Lower-recovery continuation evidence

Fresh app suite: 111 named tests / 113 executions, zero failures or skips, on the lower-recovery test fixture. All three Reduced Motion captures and each input level observed all 16 frames. Core runner finished 773 tests / 109 suites successfully, but swift test exited 1 after a sandbox manifest-evaluation denial; this is not a clean command pass. Projected support-toe diagnostics show greater displacement at lower input: clean full-input segments 2.50–2.75 logical pixels, half 7.25, quarter 7.75–8.75; these are model-derived observations, not visual acceptance or an adopted tolerance. Review timing/stride reconciliation under BP-008 before admitting locomotion. See runtime docs/review/player-low-recovery.

Live cadence comparison: 112 named tests / 114 executions passed. All 12 control/candidate captures observed 16 frames. Normal-mode modeled support range at half/quarter input fell to 3.5 logical pixels versus 6.25 / 8.25–9.25 in matched original-cadence controls. Candidate p95 reaches 40.09 ms; no performance acceptance. Test-only path retains unchanged production behavior. Interruption matrix and separate visual captures remain pending. Runtime docs/review/cadence-live-comparison preserves hashes and records.

Candidate interruption correction: the test-only distance path now follows the renderer's selected clip rather than the snapshot's base movement state. Renderer fixture regression passed for reactions, dodge, idle, terminal and north-facing movement in both motion modes; full app run 115 executions passes. Full command-driven interruption matrix remains open. Timing analysis identifies nine-tick catch-up batches in the earlier recorded run but does not establish the initiating bottleneck. See runtime docs/review/cadence-interruptions.

Command-driven route: 114 named tests / 116 executions passed. Four captures retained all 16 south candidate frames; each pause produced 21 observations of the same tick/frame, while Dodge and north reversal explicitly relinquished the candidate. Independent real-solid blockage/sliding/Dodge preflight and final live position matched. This is test-scene command evidence, not full per-tick trajectory parity, shipping pause integration or visual/performance acceptance. See runtime docs/review/command-route-review.

Shared composition checkpoint: clean real-renderer static captures combine the lower-recovery player, municipal camera, building and props with HUD; app suite 114 named tests / 116 executions passed. Review-only outline suppression verified visually in four-pose plate. Ground repetition, scale, field presentation and projected-facing mapping remain open; this is neither animated shared traversal nor benchmark acceptance. See runtime docs/review/revised-shared-scene.

Projection reconciliation: current +45°/half-height comparison sends world south down-right. Specs now distinguish authoritative heading, projected travel and authored facing; a front-facing pilot corresponds to world south-west. Offline eight-direction inverse checks pass, but no SpriteKit mapping or production input adoption is claimed. See runtime docs/review/revised-shared-scene/projection-reconciliation.md.

Live shared pilot passed: 116 named tests / 118 executions. Normal and Reduced Motion each observed all 16 source textures/two wraps, exact 90-step position trace and final digest match independent preflight, zero player-outline readbacks. Test-only front-source alias uses world-facing key w for projected SW travel; no full-facing or legal-encounter claim. Passing shared video/contact review remains open. Runtime docs/review/shared-traversal preserves failed/retry context.

Recorded shared review: separate native/detail normal/quarter exports are ready with verified 4× timestamps. Shared test retained 16 frames/two wraps in both modes, but overall recorded suite failed one full-input standard-motion distance-phase comparison at 15/16 frames. Preserve that failure separately from earlier unrecorded 118-execution pass. See runtime docs/review/shared-traversal-recorded.

Recording-load diagnosis: all sampled phase selections match recorded distance; callbacks missed ticks 30/60/90/120 where frame 15 was eligible. Debug stage timing with per-tick state/event parity passes; fresh app suite 119 executions. Awareness snapshot/hint cost ~1.2 ms/tick (~28% of measured session work), making presentation snapshot construction the next measured optimization target. This does not close the recorded miss or device performance gate.

Awareness optimization: direct read-only state projection now preserves snapshot camera/rounding/alive/awareness/lifecycle semantics, with boundary parity coverage. 47 targeted core tests and 119 app executions pass. Same-scenario stage median fell from ~1.2 ms to ~0.005–0.006 ms. This measured CPU reduction does not close the earlier recorded frame miss or device gate. See runtime docs/review/awareness-optimization.

Feel projection optimization: preserved camera/cone membership, hint ordering, safety/upgrade holds and encounter timing without full rendering projection. 61 targeted core tests and fresh simulator suite 117 named / 119 executions pass. Same session HUD/captions/quiet/feel stage median fell ~96.7% (1.74–1.76 ms to ~0.057 ms); authoritative per-tick parity remains intact. Prior recording-load failure remains open. Art amplitudes and source admission are unchanged. See runtime docs/review/feel-optimization.

Recording-load retry after both presentation optimizations passes: 119 app executions; all 12 input/motion/cadence cases show 16/16 frames, zero distance-phase mismatches. Prior failure did not recur; sustained device performance is unproven. Return to visual/shared-scene work; no further full-suite rerun without relevant changes or new evidence. See runtime docs/review/recording-retry.

Street composition trial: researched sidewalk/curb/crossing organization; shared review helper adds asphalt corner, curb gap, crossing and rails. Real-renderer still captured; player scale/framing and lower-edge crossing remain open. Capture test passed; overall run deliberately stopped and changed live traversal remains pending. See runtime docs/review/street-corner-review.

Closer-framing captures complete: one focused renderer test passes at 1×/1.25×/1.4×, unchanged HUD/world sizes/digest. 1.25× recommended for next moving trial; 1.4× clips building base. No gameplay framing adoption. Temporary review scheme removed; per-test navigator Run verified. See runtime docs/review/framing-review.

Moving framing: focused traversal passes authority/clip/frame assertions across six variants. Fixed 1.25× clips player near route end and is rejected; tracking 1.25× keeps player canvas visible but emitter leaves view later. Legal encounter warnings/occlusion remain unproven; no shipping zoom adoption. See runtime docs/review/moving-framing.

Hostile-encounter diagnostic: strengthened fixture requires hostile projectile; seed 1 tick 4248 replay matches and focused capture passes. Closer view loses cameras 6/7 and enemy 151; enemy 144 partly clipped. Legacy environment projection remains visibly wrong. Hold gameplay zoom adoption; upright environment registration and projected camera-boundary handling precede moving warning proof. See runtime docs/review/hostile-framing.
