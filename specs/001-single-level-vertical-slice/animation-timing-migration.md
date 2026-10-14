# Exact frame timing migration for BP-003

Status: implementation design; no v2 delivery or production art admitted.

## Research and decision

SpriteKit's [texture animation action](https://developer.apple.com/documentation/spritekit/skaction/animate(with:timeperframe:)) accepts a duration in seconds per texture and defines total duration as count times interval. [Sequences](https://developer.apple.com/documentation/spritekit/skaction/sequence(_:)) add child durations. Aseprite exposes [per-frame durations](https://www.aseprite.org/docs/frame-duration/) and its [frame API](https://www.aseprite.org/api/frame) expresses these in seconds. Sources checked 2026-10-14. These support authored holds; they do not prescribe an SS cadence or guarantee that every authored pose is displayed at every device refresh rate.

SS design choice: the next clip-metadata schema uses positive integer duration units and a positive integer timebase, rather than a floating fps or rounded milliseconds. Keep the current v1 delivery unchanged until v2 decoder, playback, duration consumers, exporters and parity tests are ready. Version the contract before admitting v2 records; no v2 key may be silently ignored by a v1 decoder.

## Proposed v2 representation

Replace each clip's `framesPerSecond` with `timing: { unitsPerSecond: Int, frameUnits: [Int] }`. `frameUnits` is parallel to the COMPLETE `frameIds` array, including all facings, not an implicit per-direction template. Direction filtering must select frame ID and its duration together, preserving order. Non-directional camera clips use the same representation. Both representations in one record are invalid. Missing timing, unknown keys, booleans, fractions, zero/negative integers, count mismatches and integer arithmetic overflow fail closed; do not coerce NSNumber fractions into integers.

Durations are rational seconds: frameUnits[i] / unitsPerSecond. Preserve integers through validation, summation and lifetime conversion. Convert to Double only at SpriteKit's seconds boundary. Reaction lifetime at 60 simulation ticks/second is ceil(sum(selected frameUnits) * 60 / unitsPerSecond), with checked arithmetic. Presentation scheduling cannot authorize damage, delay field removal or change gameplay speed.

Equal holds may use one texture-animation action. Unequal holds use an ordered sequence of single-texture actions, each retaining its texture for its declared duration. A one-shot retains its final texture; a loop repeats the whole duration sequence. Stable canvas/anchor, pause, restart, interruption and Reduced Motion terminal selection continue to apply. Action caching must not reuse a sequence from another timing definition. Pause/resume and authoritative event precedence require renderer tests, not just arithmetic tests.

## Exact migration vectors

| Case | Timing | Expected cycle | Lifetime at 60 Hz |
|---|---|---|---|
| Existing 6-frame 12-fps direction | unitsPerSecond=12; six 1s | 1/2 second | 30 ticks |
| New 16-frame ordinary locomotion direction | unitsPerSecond=32; sixteen 1s | 1/2 second | 30 ticks |
| Existing elite pursuit, 6 frames at 14 fps | unitsPerSecond=14; six 1s | 3/7 second | 26 ticks |
| New elite pursuit, 16 poses | unitsPerSecond=112; sixteen 3s | 3/7 second | 26 ticks |
| Variable-hold technical fixture, four frames | unitsPerSecond=24; [1,2,1,2] | 1/4 second | 15 ticks |

The variable-hold row is a technical test vector, not an approved artistic rhythm. Repeat the appropriate entries in frameIds order for every facing. Actual authored holds require BP-002 motion review. More frames do not change the cycle or prove good animation.

## Runtime impact and admission checks

Inspection of runtime d772842 found independent fps consumers in ClipCatalogLoader/ClipRecord (strict contract decoding), ClipFrameLibrary (delivery parsing and frame selection), SpriteLibrary.animation (SKAction construction), and ReactionClipTracker (presentation lifetime). All must adopt a common validated duration representation. DaemonClipTests and StandardEnemyClipProjectionTests also compute fps-derived expectations; update these to independent exact timing vectors rather than merely echoing the implementation.

Before migration, prove every existing clip's duration, frame order, directional membership, anchor, looping flag, event marker and cancellation rules are unchanged by a mechanical v1-to-v2 conversion. Update schema filename/version registry, catalog owner references, resource bundling, specification pin, exports and reachability together. Preserve ruleset/content/arena identities and replay digests; report any unexpected changes rather than replacing golden values. Do not duplicate current poses to manufacture 16-frame deliveries.

Required evidence: strict malformed-record rejection; exact vectors above; different durations by facing; equal and unequal SKAction timing; final texture retention; pause/resume; 3→2→1→0 camera interruption; reaction lifetime tick boundaries; exported frame-order/timing round-trip; full contract parity; core replay suite; iOS playback tests. Then visually review actual new source cycles at normal and quarter speed with contact phases and world travel. No production schema switch occurs solely because this design document exists.
