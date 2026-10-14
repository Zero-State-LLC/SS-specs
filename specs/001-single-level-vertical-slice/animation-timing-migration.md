# Exact frame timing migration for BP-003

Status: implementation design with a versioned target schema; no v2 delivery or production art admitted.

## Research and decision

SpriteKit's [texture animation action](https://developer.apple.com/documentation/spritekit/skaction/animate(with:timeperframe:)) accepts a duration in seconds per texture and defines total duration as count times interval. [Sequences](https://developer.apple.com/documentation/spritekit/skaction/sequence(_:)) add child durations. Aseprite exposes [per-frame durations](https://www.aseprite.org/docs/frame-duration/) and its [frame API](https://www.aseprite.org/api/frame) expresses these in seconds. Sources checked 2026-10-14. These support authored holds; they do not prescribe an SS cadence or guarantee that every authored pose is displayed at every device refresh rate.

SS design choice: the next clip-metadata schema uses positive integer duration units and a positive integer timebase, rather than a floating fps or rounded milliseconds. Keep the current v1 delivery unchanged until v2 decoder, playback, duration consumers, exporters and parity tests are ready. Version the contract before admitting v2 records; no v2 key may be silently ignored by a v1 decoder.

## V2 target representation

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

## Versioned target and staged adoption

[clip-metadata-002.schema.json](../../contracts/clip-metadata-002.schema.json) is the structural migration target. Active `versions.json.componentContracts.clipMetadata` remains `clip-metadata-001`; the target schema is not a new active delivery. A mechanical conversion preserves `animation-civic-seam-001`, since it changes representation without changing frame identity, timing, events or state semantics. A later artistic change still follows its own coordinated admission.

Target integer fields must fit signed 64-bit integers, matching supported runtime platforms. JSON Schema checks structure, scalar types, positive duration units, closed objects and version identity. It cannot prove equal array lengths, checked sums/products, role/facing membership, cancellation/event rules or asset reachability. Runtime semantic validation must enforce those separately; schema success alone never admits a clip.

`scripts/validate_clip_timing_migration.py` converts the current v1 delivery in memory and verifies the target schema, complete frame-order/field preservation, exact per-facing rational durations and 60 Hz lifetimes. It also checks malformed timing rejection. This is migration evidence, not an accepted replacement delivery. Run it alongside `scripts/validate_specs.py` while implementing the runtime decoder.

## Event-driven one-shot facing and phase

Implementation decision for the comparison build: event-driven hurt/stagger, held commit and defeat playback retain their selected event-facing for that one-shot. Select the Player's post-tick facing or the enemy's presentation-facing from the event-tick body (use the last available body for defeat). Compute lifetime from that same facing's selected duration units. Do not substitute the first catalog facing or change authoritative movement/aim to hold the picture still. Locomotion and authoritative state clips continue to use their live facing.

Track the event/transition start tick separately from clip ID and facing. A later qualifying event for the same clip and facing is a new one-shot and restarts its authored response under existing cancellation/precedence rules. Repeated rendering of the same occurrence, or a turn without a new event, must not restart or extend it. Defeat supersedes hurt as before. Multiple same-tick events may share the existing per-entity reaction aggregation; this does not create additional damage or new priority rules.

Lifetime ends at startTick + ceil(selectedDuration × 60), exclusively. A reaction first drawn after its event must enter at the elapsed phase, not receive a fresh full duration. If presentation is suppressed by an uncancellable state, it cannot extend its original deadline when it later becomes eligible. Pause freezes simulation and world action time; resume preserves phase. Restart, scenario replacement and removal clear the occurrence. Reduced Motion uses the selected facing's settled final pose and the same lifetime; neither playback nor expiry changes damage, fields or events.

Keep reaction facing/occurrence separate from live state facing. If reaction art is unbacked, fallback uses the live state clip and live facing; an unavailable reaction must not freeze the fallback's direction. Held commits use their selected facing only while the held clip is actually presented. Capture native-scale turning during hurt/commit before treating event-facing retention as visually accepted.

Required tests: four directions with independently expected durations; turn during a reaction; same-clip/same-facing repeat event; late first render; temporary suppression; exact final tick and expiry; missing-art fallback; pause/resume; reset/removal; defeat precedence; Reduced Motion. Show that the same command stream still produces the same simulation digest. These extend the admission checks, not the list of gameplay mechanics.

Research and tradeoff (2026-10-14): Apple's [action control](https://developer.apple.com/documentation/spritekit/controlling-actions-precisely-by-using-names) treats action replacement as explicit control; Godot's [transition API](https://docs.godotengine.org/en/stable/classes/class_animationnodetransition.html) separately specifies restart behavior. These support separating event occurrence from state/facing selection. Retaining event-facing is SS's chosen comparison policy, not a universal animation rule or externally proven aesthetic. It avoids restarting the same response on movement input and gives exact lifetime ownership. The tradeoff is a brief pose facing different from travel; preserve live movement and verify readability in the real renderer. Phase-preserving live-facing retargeting remains an alternative if that visual comparison fails, and requires an explicit mapping rather than a silent action restart.
