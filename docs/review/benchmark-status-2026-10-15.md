# Benchmark production: status and next steps

Updated 2026-10-15. Planning/evidence reconciliation, not a new product contract or art admission. Governing requirements remain D-104 / BP-001–BP-010. Runtime evidence inspected through 241a1ef; runtime production spec pin remains d602775. The [kanban](../kanban.md) mirrors this sequence and the [canonical tasks](../../specs/001-single-level-vertical-slice/tasks.md).

## Direction retained

**OBSERVED — user preference:** the narrower-stance, alternating-arm version is much better. Preserve the hooded player and urban street-theater identity. Improve the retained source; do not replace the preferred motion direction during detail repairs. This preference does not approve the numerical 8-unit stance, 4/10px elbow/hand displacement, hidden surfaces, production size, other facings or device performance.

**OBSERVED — inspection:** normal (0.5s) and quarter-speed (2s) modes were inspected separately using browser playback samples, all 16 exported poses, detailed keys and seam onion skin. Knee pads become cup-like; calf folds look stretched; boot shafts are flat beside bright toe caps; coat overlap lacks depth; hands alternate but elbow/glove articulation remains limited. Inspected front/rear boot keys assign laces to the tongue, not the heel. No exceptional 16→1 reset was found, but neither pixel differences nor sampled playback establish final smoothness or planted-foot contact. Runtime review: `241a1ef` (local commit; not yet published).

## Evidence now available

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
