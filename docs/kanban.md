# SS benchmark kanban

## Current handoff — 2026-10-25

Aaron continues from the [continuation brief](review/aaron-continuation-2026-10-25.md). Stop recorder/OBS troubleshooting; retain the0.375-second Player candidate and bounded visual approval. Prioritize remaining Player releases/facings/actions, then shared-scene integration and direct iPhone validation. Live cadence/performance remain unverified and required before production admission; they do not block further source work. Historical recorder-dependent next-step notes below are superseded for sequencing only. No parent production task is Done.


Updated 2026-10-19. Repository planning mirror of [SS-specs + SS-runtime — Benchmark](https://github.com/orgs/Zero-State-LLC/projects/27). Canonical parent tasks: [tasks.md](../specs/001-single-level-vertical-slice/tasks.md). Evidence, dependencies and exit gates: [next-step plan](review/benchmark-status-2026-10-15.md). No parent production task is Done.

## Current priority — player first (2026-10-19)

Owner steering: defer enemy production until the Player is done correctly; retain the enemy pipeline requirement rather than beginning it now.

- [ ] **T1045 / Player finish:** review the bounded-proportion cycle and proposed 0.25s settle in the exported native normal/quarter clips (`runtime/docs/review/player-settle-timing`); verify contacts, coat/boot/knee ownership, arm motion and the 16→1 seam. Preserve the preferred narrower stance and arm swing. Then finish distinct facings and required Player actions with the same detail standard. Candidate dimensions, amplitudes and hidden surfaces remain proposed.
- [x] **T1042/T1046 / bounded camera-post and exterior repair:** focused simulator test and 779 core tests pass; evidence is in runtime `docs/review/camera-depth-edge-repair/README.md`. Neutral-pose, paused-action captures prove neither animated gait nor complete scene acceptance.
- [ ] **T1045 / deferred enemy production pipeline:** after Player completion, derive a repeatable editable-source → directional/action sheets → registered exports → real-renderer validation workflow from the accepted Player package. Enemies must retain comparable design detail and their individual urban street-theater identities. Existing tools and studies are ingredients, not a proven complete cast pipeline. Research unresolved role/design choices before production; preserve archetype-specific movement and action timing. Track under existing [SS-specs #65](https://github.com/Zero-State-LLC/SS-specs/issues/65), without creating new cast scope.

Current verification: 13-trigger lifecycle regression and two-phase × two-motion-mode source-backed settle test pass. Native recordings are exported with matched frame counts and fourfold relative timestamps. After review-harness search and clock-boundary fixes, the full playback class passes: 20 tests, 0 failures/skips (351.434s). Prior failures are retained as historical evidence. Timing and contact approval remain open.

This priority supersedes earlier “next” entries below. The repository ledger is updated; no remote Projects synchronization is claimed.

## Done — bounded evidence only

- [x] T1045: narrowed-stance / alternating-arm south source preserved (718b392); user prefers this direction.
- [x] T1045: separate normal/quarter-speed detail and seam inspection (241a1ef); remaining art defects recorded.
- [x] T1042/T1045: canvas/anchor mismatch diagnosed (ae5fecc); isolated live renderer integration corrected and tested (88e79e8).
- [x] Capture harness #130 corrected locally; 773 core tests and 107 simulator executions pass. Remote closure remains separate.

## Current continuation — 2026-10-15

- [x] Bounded south-cycle harness: preload/registration/outline preparation and rendered-snapshot telemetry reuse; two app suites at 113 passing executions, six Reduced Motion captures at 16/16. Full interaction/contact/device gates remain open.
- [x] Fuller calf/cuff source candidate exported, with preserved pose samples and separate two-speed review; not admitted or visually accepted.
- [ ] Reconcile fuller-leg asset hashes and fresh renderer coverage/contact evidence, then shared scene. Prior candidate results cannot be reused as new-asset proof.

## Next — ready

- [ ] **T1045 / source polish:** knee pads; calf/cuff/boot material; elbow/glove articulation; coat overlap. Preserve preferred motion direction. Exit: all 16 poses and separate two-speed/seam inspection.
- [ ] **T1045 / live-cycle evidence:** legal longer route, no synchronous image extraction during measurement, actual frame/projection/travel records, sufficient contact samples. Exit: full-cycle coverage plus honest contact report; no arbitrary pass threshold.

## Upcoming — after source and motion evidence

- [ ] **T1042 / shared scene:** player + municipal camera + building + props + street; common projection, HUD, native/50%/grayscale and encounter evidence.
- [ ] **T1042 / visibility:** complete Player outline and camera-field contrast matrix; decide from evidence and update affected specs before production changes.
- [ ] **T1045 / facing and cast:** four-neutral-facing master reconciliation, six movement families, required actions/reactions; resolve remaining physical weapon/role design through research.
- [ ] **T1043 / camera completion:** full state/interruption/reduced-motion visuals, Captain identity, provenance and complete-device admission gates.
- [ ] **T1046 / environment:** finish 46-item disposition and base/solid/traversal/projectile/occlusion matrix.

## Waiting on prerequisite evidence

- [ ] **T1044 / production migration:** waits for complete accepted families; then timing/metadata/catalog/resource/hash/pin parity and old-asset exclusion.
- [ ] **Release/device QA:** waits for integrated visual review and test candidate; then Debug/Release, accessibility, weapons/upgrades/damage, complete runs and physical budgets.
- [ ] **D-020/D-021 and Gates A–G:** waits for specified measurement and human evidence; no expansion approval inferred.

## Tracking notes

The old NOT_PRODUCED labels describe accepted production coverage, not absence of source studies. Current parent statuses remain partial/unaccepted. GitHub Projects CLI access lacks read:project; board maintenance uses the authenticated browser. The legacy Surveillance-Survivor project is excluded. Six mistakenly added legacy drafts were archived; its original CI card was retained. Local commits cited here are not assumed published.

- [ ] BP-008: lower excessive knee recovery; fresh source review at both speeds, then exact-revision renderer validation. Fuller-leg fixture is held pending the motion correction.

- [x] Lower-recovery test-only fixture: matching PNGs/poses and source hashes; fresh app suite 113 executions passes, including three 16/16 Reduced Motion captures.
- [ ] BP-008 contact: investigate measured support-point displacement and compare authored cadence with actual-travel phase; reconcile timing contract before any runtime policy change. Core runner: 773 passed; command exited 1 due to manifest sandbox denial.

- [x] BP-008 partial-input research and recorded-route counterfactual: retain authored cadence control; distance-indexed source frames reduce modeled support displacement but do not establish visual acceptance.
- [ ] Implement the specified test-only live cadence comparison with explicit interruption/reset semantics; preserve production timing and simulation authority.

- [x] Test-only live cadence comparison at all three inputs and both motion modes: compiled, all 16 frames observed in all 12 captures; app suite passed.
- [ ] BP-008 comparison interruption matrix and separate normal/quarter-speed visual review; timing spikes remain unaccepted. No production policy adoption.

- [x] Recorded exact revised fixture; separate native/detail normal- and quarter-speed review exports for full/half/quarter input. App suite 114 executions passes; paired video timestamps verified.
- [ ] Review captured motion/contact and interruptions; investigate recorded p95 spikes (up to 66.48 ms in the distance candidate), preserve performance gate as open.

- [x] Candidate selection guard: preserve renderer-selected hurt, dodge, idle, terminal and other-facing clips; regression passed in both motion modes. Fresh app suite 115 executions passes.
- [ ] Live command-driven interruption scenarios and isolated performance profiling; renderer fixture checks do not close these.

- [x] Command-driven candidate/control route in both motion modes: independent real-solid blockage/slide/Dodge preflight, matched final position, 16 frames, frozen pause tick/frame and unsupported-facing records; app suite 116 executions passes.
- [ ] Complete per-tick live/preflight trace parity, visual interruption capture and performance profiling before adoption/shared-scene acceptance.

- [x] Review-only shared composition: four lower-recovery poses with camera/building/props/HUD, native/half/grayscale exports; clean app suite 116 executions passes.
- [ ] Shared scene: reconcile projected-facing mapping, improve ground/scale/field presentation and capture animated traversal/occlusion; retain performance and device gates.

- [x] Research and document shared projection/facing mismatch; offline eight-direction inverse and foreshortening diagnostic passes.
- [ ] Compare projection algebra with actual node conversions; capture a correctly oriented projected pilot, then complete facing/input/occlusion integration.

- [x] Actual shared-scene SpriteKit forward/inverse checks: eight directions × four magnitudes; fresh app suite 116 executions passes.
- [ ] Correctly oriented live shared traversal, facing selection and input integration; numerical mapping alone is insufficient.

- [x] Shared environment review art can preserve selected player clips/actions; movement/idle/dodge/hurt/unsupported-direction comparisons pass in both motion modes. Fresh app suite: 117 executions.
- [ ] Wire selected-clip mode into correctly oriented shared traversal and record actual displayed contacts.

- [x] Live projected shared pilot: actual 75-tick SW travel then idle; both modes show all 16 frames/two wraps, every position and final digest match preflight; app suite 118 executions passes.
- [ ] Capture passing shared pilot at normal/quarter speed; review contact/seam and scene composition; full-facing/encounter/performance gates remain open.

- [x] Separate normal/quarter-speed shared-scene simulator exports, native/detail, with verified identical captured-frame counts and 4× PTS spacing. Shared traversal retained 16/16 in both modes during recording.
- [ ] Recording-load regression: full-input standard-motion distance-phase candidate displayed 15/16 frames; investigate without weakening coverage. Moving shared contact/seam review remains open.

- [x] Recording frame miss isolated: observed phase arithmetic matches; all frame-15 opportunities fell between display callbacks. Opt-in session-stage timing preserves every tick/event; app suite 119 executions passes.
- [ ] Investigate redundant full-snapshot work in awareness/feel presentation (~28% awareness stage in diagnostic); prove semantic parity, then remeasure recording load.

- [x] Awareness direct-state projection replaces unnecessary full snapshot; 567 visibility parity combinations plus lifecycle, 47 targeted core tests and 119 app executions pass. Measured stage median ~1.2 ms → ~0.005–0.006 ms.
- [ ] Independently reconcile/measure FeelPassPresenter snapshot work; repeat recording-load coverage and Release/device performance before closing the frame miss.

- [x] Feel copy projection no longer constructs full render snapshots: parity/priority/lifecycle tests, 61 targeted core tests and 119 app executions pass. Same session stage median ~1.74–1.76 ms → ~0.057 ms, with authority parity intact.
- [ ] Repeat recording-load coverage after both presentation optimizations; retain normal/quarter visual review and Release/device gates. Earlier recorded 15/16 failure is not closed by the unrecorded pass.

Recording-load retry after both presentation optimizations passes: 119 app executions; all 12 input/motion/cadence cases show 16/16 frames, zero distance-phase mismatches. Prior failure did not recur; sustained device performance is unproven. Return to visual/shared-scene work; no further full-suite rerun without relevant changes or new evidence. See runtime docs/review/recording-retry.

Street composition trial: researched sidewalk/curb/crossing organization; shared review helper adds asphalt corner, curb gap, crossing and rails. Real-renderer still captured; player scale/framing and lower-edge crossing remain open. Capture test passed; overall run deliberately stopped and changed live traversal remains pending. See runtime docs/review/street-corner-review.

Closer-framing captures complete: one focused renderer test passes at 1×/1.25×/1.4×, unchanged HUD/world sizes/digest. 1.25× recommended for next moving trial; 1.4× clips building base. No gameplay framing adoption. Temporary review scheme removed; per-test navigator Run verified. See runtime docs/review/framing-review.

Moving framing: focused traversal passes authority/clip/frame assertions across six variants. Fixed 1.25× clips player near route end and is rejected; tracking 1.25× keeps player canvas visible but emitter leaves view later. Legal encounter warnings/occlusion remain unproven; no shipping zoom adoption. See runtime docs/review/moving-framing.

Hostile-encounter diagnostic: strengthened fixture requires hostile projectile; seed 1 tick 4248 replay matches and focused capture passes. Closer view loses cameras 6/7 and enemy 151; enemy 144 partly clipped. Legacy environment projection remains visibly wrong. Hold gameplay zoom adoption; upright environment registration and projected camera-boundary handling precede moving warning proof. See runtime docs/review/hostile-framing.

Player-first contact audit (2026-10-16): current 16 textures plus pose metadata match the recorded lower-recovery candidate. Historical shared continuous records retain modeled support-toe ranges of 2.399–5.013 logical units; this is not pixel-tracked acceptance. Preserve contact as open, separate it from frame coverage and paused Camera captures. Evidence: runtime `docs/review/player-contact-audit/README.md`. No new art or playback policy adopted.

T1045 material-only source comparison (2026-10-16): restored retained calf/boot contrast without changing source poses, geometry, UVs or assembly. All 16 alpha masks identical and changed pixels restricted to original calf/boot masks. Separate normal/quarter source previews in runtime `docs/review/player-material-detail`; not admitted and not evidence that contact is fixed.

T1045 recorded renderer follow-up (2026-10-19; capture 2026-10-16): focused shared traversal passes (1 test, six variants). Separate normal/quarter native captures are saved in runtime `docs/review/player-material-renderer-review`. These are 57-frame steady-movement excerpts, not full contact/seam acceptance. OBSERVED: entry has a white fallback; the isolated library supplies no player_idle. Do not substitute movement art to conceal missing clip coverage. Next: registered idle/transition coverage for the projected facing, followed by entry/movement/exit and repeated seam review in both motion modes. Enemy production remains deferred until Player completion.

BP-008 diagnostic reconciliation verified (2026-10-19): focused renderer test passes across six variants; records now cover ticks 0–90 and explicitly retain 15–17 missing-sprite idle callbacks per variant while retaining all 16 movement frames. Core Clip: 66 tests pass. Evidence: runtime docs/review/player-transition-diagnostic. Diagnostic omission repaired; authored idle/facing correspondence and visual transitions remain open. GitHub defect publication pending connectivity.

T1045 next source correction (2026-10-19): direct reuse of painted idle rejected after registered comparison: upper-body identity matches but lower-body proportions/materials diverge. Reconcile one editable lower-body source across neutral and motion before adding idle to runtime. Preserve narrowed stance, opposing arms and low knee recovery. Evidence: runtime docs/review/player-idle-correspondence. No production art change or visual acceptance.

T1045 neutral control rendered (2026-10-19): separately authored planted pose from the existing movement model preserves inherited segment lengths/materials and narrower stance; no movement frame relabeled idle. Comparison confirms that stride explains some elongation but neutral knee placement and boot detail still diverge from painted reference. Source-only geometry checks pass; visual admission rejected. Evidence: runtime docs/review/player-idle-correspondence/model-neutral. Next correction must reconcile lower-body geometry/material with the painted reference, without whole-character scaling or root shifts.

T1045 source trials (2026-10-19): shorter neutral-leg fit cannot reach existing stride targets and is rejected as a standalone correction. Retained-paint knee trial removes procedural replacement but yields a shallow visible cap; also not accepted. Inspect cap orientation/UVs/calf depth overlap before further material tuning. Evidence: runtime docs/review/player-idle-correspondence/painted-knee-trial. No runtime art changed.

T1045 knee comparison rendered through all 16 unchanged poses (2026-10-19). Neutral-view paint mapping and 2.8-radius cap are proposed; dark lower rims in recovery remain a visual concern. Separate normal/quarter source videos retained in runtime docs/review/player-knee-surface-cycle. Not installed; contact, idle and visual acceptance remain open.

T1045 knee material boundary corrected in a separate source candidate; all 16 alpha masks and pose samples unchanged from prior surface trial. Four inspected poses show closed painted caps without the broad black rim. Next: isolated renderer comparison and full-cycle review; idle/proportion/boot work remains open. Evidence: runtime docs/review/player-knee-material-boundary. No production assets changed.

T1045 test-only knee candidate reconciled (2026-10-19): 15 playback tests pass; 27 coverage metrics retain 16/16 frames; six shared traces span ticks 0–90 and preserve missing idle evidence. Built textures verified. Production art, idle/proportions, contact/seam visual acceptance and device gate remain open. Evidence: runtime docs/review/player-knee-material-boundary.

T1045 proportion study: neutral-only fit rejected by full-cycle knee-height checks. A smaller segment redistribution with bounded unsupported-foot recovery passes sampled reach/clearance/support-preservation checks; rendering remains next. Runtime knee-material fixture stays unchanged. Evidence: runtime docs/review/player-proportion-fit.

T1045 bounded-proportion source rendered (2026-10-19): all 16 keys, separate eight-loop normal/quarter previews; sampled segment/reach/support/clearance checks pass. Max knee height unchanged; right seam step slightly larger, left smaller. Visual cadence/contact acceptance remains open. Next same-source neutral/transition comparison, then isolated renderer reconciliation. Evidence: runtime docs/review/player-bounded-proportions. Runtime fixture remains prior knee-material candidate.

T1045 matching neutral rendered with bounded-proportion source; all 16 direct-stop phases exported separately at normal/quarter speed (2026-10-19). Identity/scale correspondence now has a source plate; transition smoothness, contact and runtime delivery remain open. Diagnostic has no interpolated settling frames and no world travel. Evidence: runtime docs/review/player-bounded-transitions.

T1045 bounded movement/held-neutral integrated in isolated renderer fixture (2026-10-19). Initial six readback failures exposed omitted neutral outline preparation; repaired without weakening assertions. Retry passes six variants, 16/16 movement frames and correct supported idle through tick 90; unsupported initial world-e remains missing. Core Clip 66 pass. Evidence: runtime docs/review/player-bounded-idle-renderer. Visual transitions, other facings and production admission remain open.

T1045 native bounded-player recording exported (2026-10-19): focused traversal passes; separate normal/quarter clips preserve 89 frames with verified 4× timestamps. Held neutral is visible at the end. Contact/ground separation, cadence/seam acceptance, unsupported facing and production admission remain open. No new full-suite claim. Evidence: runtime docs/review/player-bounded-idle-recording. Enemy production remains deferred until player acceptance.

T1045 contact investigation: corrected stale neutral provenance to measured 12.5/14.5 segments; installed PNG hash matches current source. Preserve root (192,336); heel/toe ground projection differs by depth. Next isolate sole/ground/shadow positions in renderer before any anchor adjustment.

T1045 held-neutral pixel registration measured: root matches terminal telemetry within 0.36 captured pixels; sole-center raster reaches modeled toe row within 0.5 source pixel. Preserve anchor. Next isolate shadow placement in real renderer, then moving contacts. Evidence: runtime docs/review/player-ground-contact.

T1045 review-only grounded-shadow comparison implemented; control + candidate pass two native tests across twelve variants (36.748s), retaining 16 frames and simulation/idle/readback checks. Geometric delta records saved under runtime docs/review/player-ground-contact/shadow-comparison. Visual capture remains next; production default unchanged. Specs validator passes.

T1045 shadow comparison recorded: both native tests pass (38.104s), separate control/candidate normal and quarter clips exported with equal frame counts and exact 4× PTS. Sequential decoding used after seek-index discrepancy. Visual admission remains open; no production-default change. Evidence: runtime docs/review/player-ground-contact/shadow-recording.

T1045 current bounded-player full playback suite passes: 16 tests, zero failures, 217.420s (2026-10-19). Current gate-status table added to benchmark-production.md. Neutral exporter now truthfully reports one held frame and zero arm/coat swing; regeneration preserves exact installed PNG hash. Visual contact/transition, facings/actions and production admission remain open. Evidence: runtime docs/review/player-bounded-full-playback.

T1045 all-phase renderer release coverage passes: 32 unique displayed-phase/motion-mode cases, observed texture markers, first/terminal idle delivery and independent simulation replay. Both traversal controls rerun; 3 tests, zero failures, 134.620s. Evidence: runtime docs/review/player-phase-release. Visual smoothness, restart/reversal and complete source-family admission remain open.

T1045 stop-source investigation identifies phases 5/13 as extreme direct-neutral changes. Researched next prototype: contact-aware source settling with unchanged authoritative stop, anatomical lengths and root; compare offset-foot idle rather than sliding planted feet to a parallel stance. Timing remains proposed. Evidence: runtime docs/review/player-stop-transition-design.

T1045 extreme-phase settling source prototype rendered for phases 5/13: 17 samples, proposed 0.5s and 3-unit lift, fixed supporting toes, exact movement-entry/neutral-end pixels, geometry checks pass. Direct vs settle normal/quarter source videos at outputs/SS-player-settle-prototype. No runtime adoption; cadence/contact, interruptions and Reduced Motion remain to review. Evidence: runtime docs/review/player-settle-prototype.

T1045 settling integration prerequisite deepened against current runtime selection: reaction cancellation windows and terminal/Dodge/Extraction precedence preserved; immediate resume/reversal cancellation, pause/reset behavior, missing-source fallback, and Reduced Motion settled-idle behavior specified. Two-phase source timing remains proposed; no runtime integration yet. Evidence: runtime docs/review/player-settle-prototype/lifecycle-mapping.md.

### 2026-10-19 — settle timing feedback

Half-second source settle was judged better but too slow. Compare proposed 0.25s against 0.50s using the same 17 poses and foot-contact sequence; keep walking at 32fps and provide separate normal/quarter views. No timing accepted yet. Review-only renderer lifecycle prototype is opt-in with no installed default sequences; cancellation test results must be recorded before integration. Enemy production remains deferred until the player gate.

Native opt-in settling lifecycle regression passed: 1 test, 0 failures (14.631s). This isolates state/cancellation behavior using backed textures; it is not a visual acceptance of settling art. Shorter source comparison exported at normal and quarter speed; timing remains proposed.

Settling discontinuity follow-up: fixed stale intermediate texture on tick rewind; added rewind and idle-facing checks. Expanded native regression passed (13 triggers in 1 test, 0 failures, 20.531s). Specs validation passed. Timing and real-renderer candidate-art review remain open.

Source-backed settling renderer comparison passed: both extreme phases × Standard/Reduced Motion, 1 test / 4 variants / 0 failures. Simulation trace/digest parity, prepared outlines with zero playback readbacks and neutral completion verified. Normal/quarter native video review still outstanding; 0.25s remains proposed.

Latest owner timing feedback (2026-10-19): “Too abrupt” supersedes the preceding “Timing feels right” response for 0.25s. Half-second was too slow. Neither is accepted; next comparison is authored 0.375s with unchanged pose/contact order. The full playback regression of the existing 0.25s implementation continues independently.

Coverage investigation: instrumented focused traversal passed 6 variants, 16/16 frames, but does not clear prior full-class failure. Standard/tracking median update12.959ms; review projection5.100ms versus renderer0.491ms. Next isolate harness projection/tree traversal overhead while preserving equivalent visuals, authority and coverage assertions. Runtime evidence: docs/review/player-settle-timing/stage-diagnosis.md.

Review harness search optimization measured: tracking projection median5.100→1.039ms, total update12.959→7.711ms. Sprite/outline identity parity passed. Focused run still has one coverage failure: first Standard/1× variant delivered9/16; simulation-step block max114.671ms. Five other variants16/16. Failure remains open; next distinguish catch-up count from per-step stalls. No production FPS or clean-suite claim.

Preparation-clock fix verified: last warm-up interval no longer becomes active simulation debt. Delayed-preparation assertions plus six live variants pass (21.317s); all16/16 frames, authority and node parity retained. Full playback-class rerun remains pending. Midpoint settle timing still proposed; no device gate closed.

Full corrected playback verification: 20 tests passed, 0 failures/skips, including previously failing traversal and the added preparation-clock regression. Source/art hashes unchanged through run. Next: review proposed0.375s midpoint, then remaining source contact/facing/action gates. No full-game or device acceptance inferred.

Proposed0.375s native integration: existing ClipTiming encodes3/128s holds; quarter-second control retained. Eight native variants and13-trigger cancellation regression pass. Neutral midpoint observed at23/24ticks, all samples match exact formula; display quantization recorded. Native midpoint videos and visual approval still pending. The full20-test result predates this small timing change.

Native midpoint review exported: both extreme stopping poses, normal and quarter speed separately; 133/139 matching frames and exact4× relative timestamps verified. Recorded eight-variant run passed. Timing remains proposed pending visual review; production/device gates remain open. Evidence: runtime docs/review/player-settle-timing/midpoint-native-review.md.

Midpoint contact coverage remains open: recorded renderer callbacks observed13/17 and16/17 authored poses. Export integrity is verified, but slow replay cannot restore missing poses. T1045 next requires separately labeled native all-pose/frame-step contact evidence; normal-speed timing remains proposed.

Core regression complete:779 tests/110 suites pass,372.949s. Native all-pose diagnostic added for the two midpoint stopping phases, asserting texture identity and unchanged root/size/anchor for every pose; full DisplayedPlaybackTests run is now active in Xcode. Results and pose images remain unverified until run completion.

T1045 static native inspection now captured:34 clean images cover all17 poses for both stop phases. Final focused test passes (6.728s); all20 existing playback tests pass in the full run, whose sole failure was the new fixture setup, retained in evidence. Core779 tests pass. Viewer: outputs/SS-player-settle-clean-pose-review/index.html. Cadence/contacts remain proposed; static captures do not close moving-contact or family admission.

T1045 modeled contact refresh complete for current source:18 traces, source identities verified. Standard fixed-time half/quarter drift6.25/8.75 units versus3.5/3.5 for existing distance phase. Next shared native comparison and actual sole tracking; no adopted tolerance or playback policy. Historical source audit remains historical.

T1045 shared distance-phase harness implemented as opt-in review:12 variants pass,16/16 movement coverage each, actual299.968-unit matched travel, independent simulation parity and restored neutral. Recording with explicit captions is in progress. No production cadence/source adoption; shared contact/interruptions and visual review remain open. Evidence: runtime docs/review/shared-distance-phase.

T1045 labeled shared comparison passes: 12 variants, all16 renderer poses each; original traversal/preparation-clock regression passes6 variants. Video capture has gaps and wall-time/caption alignment discrepancies; normal/quarter exports withheld pending continuity verification or isolated recapture. Automated pass does not close visual contact approval. Latest0.25s feedback remains too abrupt;0.375s remains proposed.

T1045 capture diagnosis resolved: decoder-estimated timestamps diverged up to6.88s; presentation-timestamp decode restores visible variant alignment. Six Standard Motion comparison pairs exported separately at normal/quarter speed, source frame counts and relative PTS verified. Recorded gaps remain explicitly disclosed; quarter-input candidate lacks complete held-idle footage. Specs evidence-integrity rule added and validator passes. Visual cadence/contact and production admission remain open.

T1045 full current playback regression passed:22 tests, zero failures/skips,433.235s bundle elapsed; source/fixture inventory unchanged. Includes new shared distance-phase and corrected all-pose fixture in one complete run. Evidence: runtime docs/review/shared-distance-phase/full-suite-result.json and full-suite-tests.json. Mac locked during later cases; tests completed, but visual review awaits unlock. Next: reliable isolated cadence/contact capture, proposed0.375s timing review, then remaining facing/action gates. No device or family admission implied.

T1045 source-pixel contact diagnostic complete: all16 original/annotated foot crops; eight support landmarks within0.5–1 source pixel of sampled visible boot edge. Source-alpha proxy over18 archived traces retains the partial-input fixed/distance drift difference. No source/anchor change, timing acceptance or native-contact pass inferred. Xcode became accessible again after the prior lock; next native review can proceed. Evidence: runtime docs/review/player-sole-correspondence.

T1045 owner timing acceptance:0.375-second native normal-speed settle “Timing feels right” (2026-10-19). This supersedes proposed status for that reviewed duration only.0.25s remains rejected as abrupt and0.5s too slow. Contact, source-backed interruption matrix, remaining phases/facings and family admission stay open. Owner confirmed Mac unlocked; native access verified.

T1045 source-backed state-selection matrix passed:442 unique cells, phases5/13 ×17 poses ×13 triggers, with configuration retained throughout. No stale occurrence; valid new movement can create a new stop. Actual settling source used, other-state sentinel scope documented. No production change needed. Existing22-test code and other inventoried inputs unchanged; new focused test passes. Fresh core regression passed:779 tests/110 suites,481.180s, exit0. Visual contact/cadence and remaining release/facing/action coverage remain open.

T1045 native static support inspection (2026-10-19): all34 native stills inspected in enlarged unfiltered foot crops. Integer-pixel boot-patch search across the two declared support intervals yields zero best displacement in34 observations. This supports static registration only; includes background and cannot establish subpixel stability, full-sole support, live cadence or weight transfer. Heel remains raised during initial toe support. No anchor/source change justified. Next isolated live capture with complete idle tail and separate normal/quarter review; other release phases remain open. Evidence: runtime docs/review/player-settle-timing/native-support-review.md.

T1045 capture/load comparison (2026-10-19): unchanged native test passes8 variants with Simulator recording and8 without. Standard midpoint pose coverage recorded15/17 and17/17; unrecorded17/17 for both. Unrecorded max update11.69ms versus recorded22.73ms; movie still has73–102ms packet gaps. Single paired run supports capture-load contribution, not causal proof or production FPS. Preserve accepted timing; next resolve capture overhead before cadence approval, then remaining phase/facing coverage. Evidence: runtime docs/review/player-settle-timing/recording-control-review.md.

T1045 host-rendering isolation comparison implemented (2026-10-19): opt-in test helper pauses pre-existing host SKViews and restores original values; default control unchanged. Focused native test passes4 variants,16.859s. Four attachments each confirm1 host view, originally unpaused and restored unpaused. Concurrent core run means these timings are not performance evidence; core result pending. Next measure recorded comparison after core completes, then default-path regression and native review. Evidence: runtime docs/review/player-settle-timing/host-isolation-review.md.

T1045 host-isolation core regression completed:779 tests/110 suites pass,455.035s, exit0. Native4-variant restoration check and specs validator also pass. Core process is terminal; next recorded host-isolation comparison can proceed without concurrent core-test load. Full native/default-path follow-up and visual acceptance remain open.

T1045 host-isolation recorded experiment rejected as a fix:4 native variants pass but video gaps remain~100ms and observed Standard settling coverage15/17,16/17. Experimental helper/test removed; source hash exactly restored to prior tested baseline. Next independent macOS region capture, preserving source timing; cadence/contact acceptance remains open. Evidence: runtime docs/review/player-settle-timing/host-isolation-review.md.

BP-008 capture split evidence (2026-10-19): deterministic native export passes4 variants with167 samples each, full walking seam/idle tail and17/17 Standard settle poses, preserving0.375s. Separate normal/quarter-speed pages exist. Core779/110 pass; matching live test passes functional assertions but one Standard release misses a settling pose under concurrent host load. Simulator Hitches target is unsupported; Mac-host trace processing/presentation attribution remains unverified. Keep live cadence, visual acceptance, shared-scene advancement and device gates open. Evidence: runtime docs/review/player-settle-timing/deterministic-renderer-review.md.

BP-008 owner visual acceptance (2026-10-19): owner reviewed the separate deterministic normal/quarter-speed walking-to-idle comparison and answered “Looks right visually” to foot-contact and weight-transfer review. Record bounded visual acceptance for the shown midpoint releases5/13; keep live cadence open. No unseen release/facing/action, proposed dimension/amplitude/hidden surface, production art migration or device gate is accepted by this response.

BP-008 live follow-up (2026-10-19): Display-only capture targeting host Simulator collected without concurrent core/export tests. Unchanged native test passes22.774s; Standard release5 observes17/17 poses, release13 misses index11. Callback maxima82.104ms/50.592ms remain diagnostic concerns, not physical presentation measurements. First host trace lacks SSRuntime attribution; narrower Run2 is processing. Keep live cadence and shared-scene gate open. Evidence: runtime display-only-summary.json and deterministic-renderer-review.md.

BP-008 live clock diagnosis (2026-10-19): OBSERVED Standard release13 skips settle index11 when callbacks advance tick100→102 across19.715ms; selection uses whole simulation-tick offsets. This separates a quantized sampling problem from the82.104ms walking callback gap. PROPOSED next diagnostic records SpriteKit update time/residual/step count and compares a read-only fractional presentation clock against the captured schedule; define pause/rewind/entry/cancellation behavior first. Preserve0.375s, authored holds, deterministic60Hz authority and all-frame assertions. No timing policy is adopted and no shared-scene gate is cleared. Research and exact evidence: runtime `docs/review/player-settle-timing/live-clock-diagnosis.md`.

BP-008 clock replay completed: four Standard traces from two runs reproduce native tick selection exactly; both wall-time sensitivity models include all17 poses. Actual SpriteKit clock measurement is next; no runtime clock policy adopted. Live cadence/shared scene still open.

BP-008 exact clock measurement completed: rebuilt native four-variant test passes23.050s; accumulator/tick balance checks pass for641 samples. Whole-tick Standard release5 misses index1; actual SpriteKit-time and tick-plus-residual replays cover17/17 for both Standard releases at unchanged0.375s. This supports the next bounded presentation-clock candidate, not its adoption or physical-display acceptance. No gameplay/art changes; live and shared-scene gates remain open. Evidence: runtime `docs/review/player-settle-timing/live-clock-diagnosis.md` and `exact-clock-*`.

BP-008 bounded clock candidate: opt-in benchmark implementation and seven lifecycle cases pass with four native live variants in27.525s. Both Standard releases observe17/17 poses at unchanged0.375s. Default whole-tick path remains control; no production art/timing adoption. Callback gaps still reach43.908ms Standard/45.597ms Reduced; physical display acceptance remains open. Core regression started after native completion. Next full source-backed candidate interruption coverage and separate normal/quarter native exports, then resolve live presentation before shared scene. Evidence: runtime `live-clock-diagnosis.md`, `fractional-clock-*`.

BP-008 candidate coverage complete:442 source-backed interruption cells and four deterministic exports pass131.468s; core779/110 pass725.932s. Separate normal/quarter exports retain167 frames each and Standard17/17 poses. Owner reported post-menu scene confined to top-left; review host now uses full window-scene bounds with uniform aspect-fit, preserving logical geometry/art. Rebuilt four-variant host test passes28.049s. Visual confirmation and physical-display cadence remain open; shared scene not advanced. Evidence: runtime `live-clock-diagnosis.md`, `full-window-result.json`, workspace `SS-player-fractional-clock-review`.

BP-008 live recording audit: native Simulator recording succeeded and shows full-window composition, but decoded timestamp validation fails at two reversals/duplicate PTS. Dimensions remain constant; root cause is unverified. No live cadence acceptance or derived quarter-speed proof from this master. Preserve the recording and isolate stable landscape capture next; deterministic visual exports remain separately reviewable. Evidence: runtime `live-clock-diagnosis.md`, output `live-timestamp-validation.json`.


#### 2026-10-19 gated capture result
- Native gated playback passed (91.942 s including operator gates); Standard release5/13 observed17/17 settle poses, Reduced Motion none. Full-window scene layout confirmed in captured static frames. Keep0.375-second settle.
- Specs validator passes. Core remains779 tests/110 suites passed; no core changes in this capture harness revision.
- Live video acceptance remains open: complete Simulator capture has one backwards timestamp (14.583333→12.546667 s at decoded index148). Do not count static images, callback records, or deterministic exports as live cadence approval. No shared-scene/device advancement yet.
- Evidence: runtime `docs/review/player-settle-timing/gated-live-summary.json` and `live-clock-diagnosis.md`; workspace `work/gated-full-window-clock.xcresult`, `outputs/SS-player-fractional-clock-review/gated-timestamp-validation.json`.


2026-10-19 correction: gated movie has no backwards encoded PTS; the earlier reversal is in FFmpeg best-effort estimates after duplicate PTS. Seven duplicates and burst spacing remain unvalidated, so live acceptance is still open. See runtime live-clock-diagnosis.md and gated-pts-diagnosis.json. Independent OBS Simulator-window source setup requested after its Add Source UI failed to open through automation; no recording/streaming active.
