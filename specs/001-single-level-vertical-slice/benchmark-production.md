# Benchmark production and runtime reconciliation

Status: implementation contract; visual proof pending  
Feature: SS-001 / D-104 / T1042–T1046

The [selected street corner](../../docs/review/phase4/street-corner-approved-concept.png) sets the visual quality target. [Visual reference](visual-reference.md) defines the world and cast; [design research](../../docs/review/phase4/design-choice-research.md) records the basis and uncertainty of the choices. This contract makes the production sequence reviewable. It does not admit concept images as runtime sprites.

## BP-001 — one shared production sample

The first sample contains the hooded Player, one complete standard municipal Camera, a representative solid corner building, one upright prop, ground and curb/transit detail. All use one elevated viewpoint, apparent scale, lighting direction and material treatment. Test the original-reference and midpoint projection candidates in the existing 704×326 gameplay viewport before choosing the production projection. Record the choice and the comparison images; an unmeasured angle in degrees is not required.

The scene must use the real runtime renderer, HUD and field geometry. It must show both a quiet composition and an encounter with the Player, one existing enemy, a visible attack and Camera field. A dense legal encounter capture follows before asset admission. A flattened illustration behind moving markers cannot pass. Review native phone size, 50% gameplay scale and grayscale, with natural and authoritative-geometry-overlay views. Record the viewport in points, image pixels and display scale separately.

## BP-002 — source and frame delivery

Every sample has an editable source master and an export record containing source identity/hash, tool/version, delivery identity/hash, logical canvas, texture pixel dimensions, alpha bounds, ground anchor, intended world draw size and frame order. Source texture resolution and world size are separate; changing one must not silently change the other. Existing logical Player 64×64 at (32,56) and Camera 64×96 at (32,88) remain the comparison baseline. A larger canvas or different mapping requires side-by-side native-scale evidence and recorded contract changes before admission.

Player delivery starts with four neutral facings in one rotation preview. North/back, south/front, east and west must show distinct body orientation from above; asymmetric straps and device placement remain physically consistent. Then produce one south 16-frame movement cycle and compare it against actual world travel. After that passes, complete north/east/west using the same anatomy, contact phases and equipment. Distinct hashes alone do not prove distinct motion. A changed highlight or one-pixel translation of an otherwise duplicated pose does not count as a new locomotion frame.

Review normal-speed playback, quarter-speed playback, frame-step, onion-skin and the last-to-first seam. Identify each frame's contact/passing/extension phase in the source record. Check foot slide against world displacement, limb count/length, hood volume, device continuity and ground contact. Cloth and equipment motion follows the body; it must not conceal foot/hand errors. A contact anchor may stay fixed while a lifted foot moves; this is not an instruction to pin every boot pixel.

## BP-003 — exact locomotion scope and timing

The current clip metadata is a historical delivery baseline, not the completed D-104 delivery. The 16-frame requirement applies to each of these four-facing looping movement clips:

| Existing clip | Current frames per facing | Current cycle | Required production |
|---|---:|---:|---|
| `player_move` | 6 | 6/12 s | 16 per facing |
| `fogAnalyticsCloud_move` | 6 | 6/12 s | 16 per facing; module/fog motion, no invented legs |
| `cableCarCorrelator_move` | 6 | 6/12 s | 16 per facing; transit chassis motion |
| `sutroSignalWitch_move` | 6 | 6/12 s | 16 per facing |
| `victorianVendor_move` | 6 | 6/12 s | 16 per facing; cart and body stay connected |
| `improperSearchDaemon_pursuit` | 6 | 6/14 s | 16 per facing |

Preserve those cycle durations for the first comparison. Sixteen equal holds over 1/2 s would be 32 fps; sixteen over 3/7 s would be 112/3 fps. These are arithmetic consequences of preserving cadence, not evidence of preferred artistic timing. The current integer `framesPerSecond` field cannot express the latter exactly, nor variable holds. Before admitting a cadence that cannot be represented, version the presentation metadata and update decoding, timing, export and tests together; never round silently or change movement speed. Record actual hold durations after the visual sample. Do not duplicate frames to simulate a hold while claiming 16 distinct poses.

The Informant's `autonomousInformant_anticipate` presents continuous `PURSUE` but is currently a three-frame, non-looping attack-family record (D-071). It needs an explicit pursuit playback decision after a movement sample; do not declare it a completed walk or add a new gameplay state. Its contact commit remains tied to its own damage event. The Captain has attack/state clips, not an invented walk. Elite dash and all attack/reaction clips retain their state/event windows. No 16-frame requirement is imposed on non-locomotion clips merely to inflate frame counts.

The [exact timing migration design](animation-timing-migration.md) defines the proposed versioned representation, affected runtime consumers and validation vectors. It does not itself migrate the delivered metadata.

## BP-004 — complete Camera sheet and persistent states

The Camera sheet is a complete device, including permanent pole/base and head, with one fixed mount anchor. The runtime must eventually render one complete-device node per standard Camera. The five logical family values remain placement/receipt data and map to that one visible family. Do not draw the legacy head or housing over it.

The production delivery must cover the existing six clip IDs and their exact frame order (4 operational, 2 hit, 3 critical-entry, 4 destroy, 1 field-off and 2 destroyed-idle). These counts are the current metadata obligations, not six isolated state pictures. Every terminal persistent state must remain truthful after transient actions end:

| Integrity / event | Required settled appearance | Timing and interruption |
|---|---|---|
| 3 | intact complete device | operational loop; no positional or heading motion |
| 3→2 | visible damage and single-notch marker | compact hit response; its final frame remains visibly Damaged |
| 2→1 | exposed damage and double-notch marker | critical-entry response; its final frame remains visibly Critical |
| 1→0 | dark broken head, unchanged mount/base | field disabled on the authoritative event; destruction animation cannot delay it |
| 0 on later frames | stable, non-emissive destroyed device | never returns to an intact or lit pose |

If an impact arrives during a response, the newest authoritative Integrity wins; destruction supersedes all living visuals. A 2→1 hit must never settle into the Integrity-2 picture. Reduced Motion shows the settled state immediately while retaining non-color impact confirmation. The field-off clip must not create another visible housing. Any new persistent clip IDs needed by the source art require coordinated metadata/catalog/manifest migration, not an undeclared file lookup.

Captain emitters share construction materials but must be recognizable as indestructible, boss-owned sources using a persistent non-color distinction. Compare the marker in the actual boss scene before admission. Standard three-hit notches must not appear on Captain emitters.

## BP-005 — environment and geometry truth

For every one of the 46 environment images, record retain/repair/replace/exclude, the observed defect or reason, and source/delivery identity. The representative building and prop must record their visible ground base, render anchor and world placement separately from their authoritative AABB. Review front/rear/corner traversal and projectile contact with overlays taken from runtime geometry. Do not trace the concept into new collision or stretch a cropped texture into an old AABB without recording its mapping.

Evaluate actor visibility behind foreground art in the shared scene before selecting the depth/occlusion implementation. The Player's gameplay position must remain understandable. A successful still screenshot does not establish correct traversal, layering or hit visibility.

## BP-006 — evidence and staged adoption

Each review records exact spec/runtime commits, asset hashes, launch recipe, device or simulator identity, viewport, seed/scenario and presentation settings. Label each item `NOT_PRODUCED`, `CAPTURED`, `FAILED` or `REVIEWED`; a capture is not automatically a pass. Include normal-speed video, frame-step plate, native/50%/grayscale views, authoritative geometry overlay, quiet and dense encounter, camera 3→2→1→0 sequence and reduced-motion sequence. Record failures with the affected frame/asset ID and visible symptom.

Reconcile the runtime pin to the adopted D-104 spec before implementation, recording unchanged ruleset/content/arena identity and exact contract/fixture parity. Retain historical art metadata until accepted replacements exist. Migration then updates frames, clip metadata, asset catalog/provenance, presentation manifest, runtime resources and reachability in one reviewed family. Old assets leave the shipping bundle when no reachable record uses them. Tests must prove event timing, stable anchors, one device per entity, field-off, and unchanged replay results; visual review must prove actual art fidelity.

Device profiling measures the accepted sample and later dense scene on the required performance floor. D-020 device equivalence and D-021 numerical budgets remain pending until their named evidence and decision exist. The benchmark is achieved only when art, animation, geometry/readability and performance evidence agree. CI, an image hash or a generated concept cannot stand in for that result.

## BP-007 — resolution, framing and ground registration

The revised runtime composition at runtime commit `3d46ddd` is CAPTURED, not accepted. Its 704×326 logical viewport produced 2112×978 pixels. Player texture 256×256 maps to 64×64 logical units (192×192 output pixels at this capture scale); Camera 256×384 maps to 64×96 (192×288 output pixels); building 673×768 maps to 190×217 (570×651 output pixels). These assets already exceed their displayed sampling dimensions in this fixture. This does not prove sufficient authored detail, nor that the shipping renderer has the same effective sampling at every device/zoom.

Before increasing delivery dimensions, record source pixels, occupied alpha bounds, logical draw size, camera scale, output pixels and any intermediate render targets. Compare the approved reference and runtime at the same output dimensions. Measure occupied Player height and representative building/camera height as fractions of viewport height. Show current framing and a closer candidate at native size, retaining HUD and the same encounter. Treat closer framing as a design proposal requiring field/attack visibility and traversal checks; do not silently change simulation sizes or call it a resolution fix.

Compare original high-detail masters with current exports at identical framing. Increase delivery resolution where the export loses visible source detail or becomes magnified; do not count interpolated pixels as newly authored detail. Record filtering mode. Animation deliveries use the selected sampling budget consistently across frames. Profile texture residency and frame time before admitting larger atlases; no unmeasured global size multiplier is prescribed.

The building sample also fails ground registration: its visible oblique base and unchanged axis-aligned collision box disagree. Record visible ground-base vertices in texture coordinates, texture anchor, render placement, authoritative world vertices and their projected screen positions separately. Choose a consistent art/world projection through the required comparison. If a new world-to-screen transform is proposed, apply and validate it for actors, solids, props, camera fields, projectiles, telegraphs, overlays and input conversion together. Do not rotate only a collision overlay or alter the simulation obstacle to make one still look correct. Ground shadows attach to the registered contact point; roof extent is not a ground footprint. A still cannot establish depth ordering: retain front/rear/corner traversal and projectile proof from BP-005.

Research basis (accessed 2026-10-14): Apple's [contentScaleFactor](https://developer.apple.com/documentation/uikit/uiview/contentscalefactor) separates points from backing pixels; [sprite size initialization](https://developer.apple.com/documentation/spritekit/skspritenode/init(texture:size:)) allows an explicit draw size independent of texture; [texture filtering](https://developer.apple.com/documentation/spritekit/sktexturefilteringmode) governs non-native sampling. Apple's [sprite guide](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/SpriteKit_PG/Sprites/Sprites.html) describes anchor placement and consistent animation frame sizes/anchors. Tiled's [object documentation](https://doc.mapeditor.org/en/stable/manual/objects/) distinguishes object alignment and collision objects. These sources establish mechanisms; the closer framing and required comparisons above are SS design proposals, not externally proven aesthetic settings.
