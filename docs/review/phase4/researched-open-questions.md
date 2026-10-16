# D-104 research — unresolved production questions

2026-10-14. Scope: visual and technical questions exposed by the phase-4 reference. **OBSERVED** records local contracts or images. **DOCUMENTED** records an external primary source. **OPEN** requires a prototype, measurement, source asset or owner decision. No numeric answer is assigned without that evidence.

The companion [design-choice research](design-choice-research.md) separates the user-selected benchmark from researched production methods and the remaining costume, projection and Camera proposals.

## 1. Sixteen frames and cycle timing

**OBSERVED:** `clip-metadata-001` currently lists `player_move` as 24 frames across four facings at 12 fps: six per facing, a 0.5-second cycle. D-104 asks for 16 distinct frames per applicable facing. `animation.md` now says to preserve movement-cycle cadence but does not specify the new playback rate or frame holds.

**DOCUMENTED:** SpriteKit's [`SKAction.animate(with:timePerFrame:)`](https://developer.apple.com/documentation/spritekit/skaction/animate%28with%3Atimeperframe%3A%29) has a total duration equal to frame count times frame interval. [Aseprite frame duration](https://www.aseprite.org/docs/frame-duration/) and [CLI metadata export](https://www.aseprite.org/docs/cli/) allow frame durations, tags and JSON export.

**OPEN solution:** Produce one controlled 16-frame south walk, then four facings. Compare normal/slow playback, foot contact, travel distance and loop seam against the current 0.5-second baseline; select actual frame duration only after review. Revise metadata and renderer together. Do not multiply the frame count while leaving 12 fps unchanged: that would change the cycle duration. Do not assume equal holds are optimal or claim 16 frames are visibly better without a game-scale playback proof.

## 2. The concept's detail versus 64×64 delivery

**OBSERVED:** The selected scene is a 1672×941 concept with much more character detail than a 64×64 logical player sprite. Current contracts specify 64×64 for player/standard roles and 64×96 for Cameras. No native-size production frame of the selected look exists.

**DOCUMENTED:** SpriteKit's [texture filtering modes](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode) distinguish nearest from linear when sprites are drawn away from native size. Apple's [texture animation guide](https://developer.apple.com/documentation/spritekit/animating-a-sprite-by-changing-its-texture) recommends consistent frame size and anchor placement.

**OPEN solution:** Make one 64×64 player blockout and one 64×96 complete-camera frame from controlled masters. Place them in the actual runtime scene at its real display scale and at 50% gameplay scale. Review hood, feet, Civic Pulse device, camera dome and field boundary in light/dark/grayscale/dense scenes. Keep or revise the logical canvas only on that evidence; do not infer that the illustration automatically translates or that a higher source resolution fixes tiny on-screen detail.

## 3. Frame registration and export

**OBSERVED:** Previous generated multi-frame studies drifted in pose, equipment and projection. The municipal six-key candidate is 1536×1024, six 512×512 transparent cells, and is not the required 64×96 complete clip family.

**DOCUMENTED:** [Aseprite animation](https://www.aseprite.org/docs/animation/) supports frame tags and preview; [onion skinning](https://www.aseprite.org/docs/onion-skinning/) displays adjacent frames; [sprite sheet export](https://www.aseprite.org/docs/sprite-sheet/) and [CLI metadata export](https://www.aseprite.org/docs/cli/) provide frame rectangles and durations. Apple's [texture animation guide](https://developer.apple.com/documentation/spritekit/animating-a-sprite-by-changing-its-texture) explains why consistent texture size and anchor reduce per-frame corrections.

**OPEN solution:** Use a controlled editable master for every role and the one complete municipal device. Export named frames and metadata deterministically; verify exact cell dimensions, alpha, anchor position and frame order, then visually inspect onion-skin and native-size playback. Select an authoring tool only after confirming available source masters and licenses. A generated grid is not registration evidence.

## 4. Visible base, collision footprint and depth

**OBSERVED:** Some bundled solids have large transparent margins while the renderer scales the whole image to an authoritative AABB. The concept scene has convincing building and prop bases, but its pixels do not define actual gameplay geometry. The current visual hierarchy requires the player core to remain readable, while an elevated building may occlude it.

**DOCUMENTED:** SpriteKit's [`zPosition`](https://developer.apple.com/documentation/spritekit/sknode/zposition) controls drawing order; equal-position sibling ordering depends on node ordering and `ignoresSiblingOrder`. [SpriteKit's drawing-order documentation](https://developer.apple.com/documentation/spritekit/about-node-drawing-order) describes the relevant scene ordering. It does not choose SS's collision or occlusion rule.

**OPEN solution:** In a representative runtime scene, use **authoritative** AABB/contact points to create the overlay. Traverse front, rear and corners of the building and newsbox with the player and projectiles. Record where foreground artwork may obscure the actor, and what player marker remains visible. Specify a deterministic render-depth rule only after observing the actual SpriteKit node hierarchy and screenshots. Never derive collision from alpha or assign a z-sort formula from the concept image.

## 5. Camera catalog migration and Captain distinction

**OBSERVED:** `presentation-assets-003` still lists five standard housing IDs and two Captain IDs; `clip-metadata-001` has six camera clips (4+2+3+4+1+2 = 16 listed frames). The six-key municipal concept covers state identity, not all 16 clip frames. D-104 maps five logical seeded families to one visible municipal family, while D-078 historically admitted a unique Captain housing. Existing runtime camera composition uses both a housing and a legacy camera actor.

**OPEN solution:** Before the renderer fix, specify each required output frame and its source/target anchor, persistent Integrity states, animation interrupt priority and field-off event. Then update presentation manifest, clip metadata, catalog and runtime bundle/reachability together. Preserve logical placement receipts, RNG and replay vectors. Review the proposed boss-owned non-color marker in a boss scene: it must be recognizable without suggesting standard three-hit destruction. Do not mark any of the six-key study frames admitted merely because a state is illustrated.

## 6. Atlas, draw and memory limits

**OBSERVED:** Moving from six to 16 frames per applicable facing increases the potential asset set; the actual atlas count, draw cost and memory are unmeasured. D-021 remains `DECISION_PENDING`; no iPhone-12 production ceilings exist.

**DOCUMENTED:** Apple states that textures in the same [SpriteKit atlas](https://developer.apple.com/documentation/spritekit/sktextureatlas) can be loaded and preloaded together, and that atlas grouping can reduce draw calls in [node drawing performance](https://developer.apple.com/documentation/spritekit/maximizing-node-drawing-performance). Apple's [Game Performance template](https://developer.apple.com/documentation/xcode/analyzing-the-performance-of-your-metal-app/) includes Time Profiler, thermal, Metal resource and GPU/display traces. Its [memory tools](https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use) measure allocations and warn that simulator memory behavior does not establish a safe physical-device ceiling.

**OPEN solution:** Measure decoded atlas bytes, loaded atlases per segment, bundle bytes, preload latency, draw/node counts, peak resident memory and frame-time distributions on the required physical performance floor. Compare before/after character and camera batches. D-021's exact limits come from the grayscale blockout and physical profile, not a guessed budget or a newer iPhone run. D-020's equivalent device list likewise needs an explicit recorded decision.

## 7. Provenance and rights

**OBSERVED:** The concept images were generated from two earlier project images and have prompt/tool/date/hash records in this folder. They are not admitted runtime assets. Existing catalog entries include separate third-party audio plan-date evidence still pending.

**DOCUMENTED:** [OpenAI's Terms of Use](https://openai.com/policies/terms-of-use/) state that, between user and OpenAI and where law permits, the user owns output. They also state users need rights to input and must evaluate output; ownership text does not itself establish each input's chain of rights or visual approval.

**OPEN solution:** Before shipping derivative production art, trace each input/master and edit path into an `asset-record-001` record, identify creator/tool/version and applicable rights, and verify no prohibited/copycat motifs. Resolve the separate pending audio evidence on its own source ledger; do not use these art terms to close it. Keep concepts out of the app bundle until production admission.

## 8. Device and human acceptance remain distinct

**OBSERVED:** Phase 3 passed automated core and Debug/Release app tests. The user has reported stutter, clipping, camera glitches and unexplained damage on a physical phone; the selected visual scene is not an executable build. Acceptance A–G remains open.

**DOCUMENTED:** Apple's [Game Performance guidance](https://developer.apple.com/documentation/xcode/analyzing-the-performance-of-your-metal-app/) supports measuring actual frame-time causes. Xcode's [memory guidance](https://developer.apple.com/documentation/xcode/gathering-information-about-memory-use) distinguishes simulator development evidence from real device memory pressure.

**OPEN solution:** First complete controlled art and renderer reviews, then gather comparable physical runs and recorded damage evidence on an exact build. Meet the iPhone 12 or approved no-better floor for Gate C, perform VoiceOver and 200% text checks, and run the five-person comprehension gate. A liked concept scene, CI pass, simulator run or a profile from a newer phone cannot close those gates.

## Questions that cannot be answered by research alone

- D-020: which available physical devices count as approved equivalents? Requires inventory and owner decision.
- D-021: what numerical entity/particle/atlas/resident ceilings pass? Requires the playable blockout profile on the performance floor and owner decision.
- Which 16-frame cadence and holds feel correct? Requires controlled source frames and actual playback review.
- Does 64×64 retain the selected character identity at phone size? Requires a production sample rendered in game.
- Where may a building occlude the player while preserving legibility? Requires authoritative geometry and runtime captures.
- Does the Captain's municipal-language boss marker avoid confusion? Requires actual no-color boss encounter review.
- Are all referenced sources and paid-plan audio records commercially documented? Requires source-specific provenance, not generic terms.

These stay open until their named evidence exists. No second-level work or camera-renderer fix is claimed in this research pass.
