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

### Resolution-independent actor outlines

OBSERVED: runtime `b33f637` captures the 384×384 painted Player in the real renderer. Normal post-action outline refresh removes the outline because the current generator rejects images above 256×256. Its one-source-pixel dilation also makes thickness depend on source density. Runtime [#124](https://github.com/Zero-State-LLC/SS-runtime/issues/124) tracks this admission blocker; green capture tests do not establish outline compliance.

The existing one-point faction outline in animation.md §8b must remain visually consistent at the same framing when an actor's delivered texture resolution changes. Keep logical sprite canvas, registered anchor and ground position unchanged. Source density must not alter outline width, enemy dash spacing, faction colour or opacity. This clarification preserves the existing reference framing; it does not prescribe a new zoom or silently change the outline to a permanent one-device-pixel stroke. Any zoom-dependent stroke policy needs separate comparison.

At every displayed frame, the outline must derive from that frame's silhouette. After replacement, an old outline must never remain around a different pose. Transparent margins and noncentral anchors must align the outline without clipping or shifting the actor. Reduced Motion uses the selected settled frame's outline. Unsupported or invalid sources must clear a previous outline explicitly and produce diagnosable admission evidence; silently losing contrast is not an accepted higher-resolution delivery.

DOCUMENTED research, accessed 2026-10-14: Apple's [SKTexture.size](https://developer.apple.com/documentation/spritekit/sktexture/size()) returns dimensions in points; [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture) exposes cgImage and filtering separately, shares immutable texture resources, and retains GPU texture data while referenced. These mechanisms support explicit separation of pixel storage from drawing dimensions. They do not prescribe SS's outline algorithm, cache budget or visual quality.

PROPOSED implementation comparison: generate the alpha outline in a bounded logical-mask coordinate system, independent of the source image's storage dimensions, then map padded-mask dimensions and anchor explicitly back to the actor. Preserve the original colour texture. Compare this with a density-aware source-resolution mask if logical resampling visibly damages thin silhouettes; select from native/zoom captures and measured cost. Do not simply lift the 256px cap while retaining a one-source-pixel stroke. Record source-read limits, mask/output dimensions, peak temporary allocation, retained outline bytes and cache lifecycle. No final memory/performance claim follows from a theoretical byte estimate or simulator alone.

## BP-008 — gait and displacement comparison

Player-controller.md fixes full-input travel at 240 world units/second (4 units/tick). BP-003's initial half-second Player cycle therefore covers 120 world units without obstruction. A quarter-input and half-input reference would nominally cover 30 and 60 units per cycle before command quantization/collision. Record actual positions from the simulation for the review; do not substitute nominal velocity when collision prevents motion.

The registered south candidate in the 2026-10-14 study has 208 occupied alpha rows on a 256-pixel texture mapped to 64 logical units: 52 logical units tall. Thus maximum travel per initial cycle is about 2.31 visible sprite heights. This is a screen/world-scale diagnostic, not a measurement of human height or proof of a particular real-world gait. A relaxed walk generated in place cannot be accepted merely because it looks plausible without ground travel.

Compare a brisk run at maximum input against the walk study with identical world speed, scale and cycle duration. This is a proposed presentation treatment of the existing move state, not a sprint mechanic or change to maximum speed. Select the gait only after normal-speed world-travel review. For partial analog input, specify the playback-speed or separate-pose policy after comparing quarter/half/full movement; do not assume that slowing a run produces a convincing walk. Include stationary input, collision-stopped input, wall sliding, direction reversal, dodge interruption and pause/resume. Do not change the authoritative controller to rescue art.

Before in-betweening, identify anatomical hips, both knees, both ankles, heel/toe contacts and the ground root in contact/support/passing/flight-or-lift keys for both steps. Preserve asymmetric costume sides. Rigging or pose-guided source work must hold limb lengths and contact constraints; a larger count of independently generated poses is insufficient. Interpret lengths in their recorded source/anatomical space, separately from projected screen length; follow the elevated-motion and contact prerequisites in [controlled-character-source.md](controlled-character-source.md). A walk need not have a flight phase; a run proposal must show its support/flight pattern explicitly. Review last-to-first continuity without exporting a redundant closing frame as a new distinct pose.

During each declared planted interval, project the foot landmark plus actor position into world/view coordinates and compare against its contact point on the ground. Report drift in world units and output pixels alongside video; do not claim zero slip from a stationary preview. Evaluate both cardinal and diagonal movement at the chosen projection. Foot landmarks are review annotations, never collision or damage authority. Numerical slip acceptance remains unchosen pending a native-size comparison; do not invent a passing threshold.

Research (2026-10-14): Animation Mentor's [basic human walk tutorial](https://www.animationmentor.com/blog/tutorial-animating-human-walk-cycle/) describes key-pose blocking and subsequent root translation; its [sneak-walk tutorial](https://www.animationmentor.com/blog/tutorial-animating-sneak-walk-cycle-with-personality/) distinguishes support/passing and weight shifts. Blender's [IK documentation](https://docs.blender.org/manual/en/5.2/animation/armatures/posing/bone_constraints/inverse_kinematics/introduction.html) explains endpoint-constrained bone chains. Unity's [animation/navigation coupling](https://docs.unity3d.com/ru/530/Manual/nav-CouplingAnimationAndNavigation.html) illustrates matching motion presentation to velocity and addressing foot slide. These support the workflow; SS gait selection and acceptance remain empirical design decisions.

BP-008 precision rule: select cosmetic idle/move from exact fixed-point position change across an advancing tick when that history is available. A whole-unit distance counter is insufficient: sub-unit analog travel must not display idle. Keep existing simulation counters, digest and event streams unchanged. No advancing tick means no new motion sample; restart/scenario replacement clears presentation history. This correction must preserve dodge, extraction, hurt and terminal precedence. Compare an identical command stream through the session and bare simulation.

BP-005/BP-007 source-separation clarification: a building export may include walkable sidewalk, stairs and planting beds. Its alpha outline is not a solid footprint. Require a ground-plan source with wall contact, apron and other depicted barriers labeled separately, plus a matching elevated render. Unknown hidden ground vertices remain unknown until authored; never infer them from roof bounds. Record the mapping for each layer. The [building registration investigation](../../docs/review/building-registration/review.md) records the current failed candidate. For a projected-world comparison, transform ground positions and geometry consistently while attaching upright art at projected roots; do not squash an already elevated building by transforming the finished scene. This clarification does not authorize changing arena collision.

## BP-009 — player occlusion and ground truth

The BP-005 contact study at runtime c5b5037 demonstrates that nonpenetrating solver positions can still render the Player on an upper wall or roof when actors always draw over architecture. Opaque depth ordering instead hides the Player completely. Both outcomes fail this benchmark.

When architecture obscures the Player, preserve a readable indication of the Player's actual ground position and the obstacle's solid ground boundary. A visibility treatment must communicate occlusion rather than elevation, passage through a wall, invulnerability or damage. It must not change collision, targeting, fields or events. Ground-space cues use the same projection as authoritative geometry; screen-space circles cannot substitute for projected circles. Ordinary foreground contacts must return to the normal art treatment. Restart, scene replacement and removal must clear any visibility state. Reduced Motion retains a static readable cue without requiring a pulse or fade animation.

Compare opaque depth, faded architecture, and faded architecture with a ground-boundary/contact cue before selecting production treatment. Opacity, cue width and transition duration remain comparison parameters until native-scale evidence supports a choice. Do not claim an experimental0.35opacity is externally prescribed. Avoid fading all scenery globally or promoting all actors above roofs. Occlusion eligibility must account for ground/depth relationship and actual projected overlap; the labels of three test positions are not a production classifier.

Required evidence: front/rear/corner movement including entry and exit, direction reversal, stationary contact, overlapping occluders and scene edges; natural and geometry-overlay captures; normal and Reduced Motion; enemies, projectiles and Camera fields in a legal encounter. Compare representative building and upright prop. State explicitly which of these remain untested. A static contact probe does not close traversal, combat or animation acceptance.

Research basis: Apple's [node drawing order](https://developer.apple.com/documentation/spritekit/about-node-drawing-order) and [node alpha](https://developer.apple.com/documentation/spritekit/sknode/alpha) describe ordering and opacity mechanisms (accessed2026-10-14). SS-specific cue and opacity selection comes from the comparison, not those API references.

BP-002 source-control implementation: follow the [controlled character source pilot](controlled-character-source.md). A rig scaffold is technical evidence only; it cannot substitute for the hooded costume master, four-facing review or world-travel animation acceptance.


## BP-010 — painted character separation without an implied status effect

OBSERVED: runtime b693cad provides paired 1×/3× mask captures of the painted Player. Finer masks improve silhouette sampling, but the user questioned the apparent glow. The inherited D-094 opaque cool-white border is therefore a comparison baseline, not accepted finish for the D-104 benchmark. The source colour texture is not responsible for that added border. Runtime outline-resolution/finer review records the images and cost limits.

The Player must remain locatable and distinguishable from enemies and terrain at native gameplay scale, including fog, attacks and dense encounters. A constant separation treatment must not suggest damage, invulnerability, detection, an upgrade or an active ability. Ground contact must remain understandable. Preserve non-colour faction differentiation and truthful attack/field geometry. Greater outline smoothness alone does not satisfy these requirements.

Run the following controlled real-renderer comparisons before selecting a replacement for animation.md §8b:

1. Existing opaque continuous Player outline and ground shadow as control, using the finer mask candidate to avoid conflating contour quality with contrast strength.
2. The same contour at reduced opacity, with identical artwork, shadow, dimensions and registration. Try 25% and 50% as explicitly PROPOSED comparison parameters, not evidence-based acceptance thresholds.
3. Authored costume value separation plus the existing ground shadow, with the added Player outline absent. Initially use the unchanged painted source to isolate what removal does; any subsequent repaint must be separately identified and compared. A shadow alone does not establish faction identity or visibility against dark terrain.

Do not remove enemy dash differentiation as an incidental side effect. If a candidate cannot preserve non-colour identity in the existing cast, it fails pending an explicitly specified replacement cue. Do not add a new user setting, automatic background detector, status glow, or shader system merely to run this comparison. Context-dependent highlighting and optional accessibility modes would require their own behavior and settings specification.

For each candidate, hold seed/snapshot, pose, framing, backdrop, fog and HUD fixed. First capture the existing shared scene as a diagnostic, then test pale sidewalk, dark asphalt, building shadow and visually busy props within the intended level. Quiet-scene aesthetics alone cannot select production treatment. Required acceptance includes native/50%/grayscale views, movement and reversals, legal dense combat, damage versus steady-state separation, Camera fields, occlusion entry/exit and Reduced Motion. Record whether the Player can be located and faction distinguished without colour, whether boots remain grounded, and whether transient damage is still distinct. Record observer findings and failures; do not invent a numeric contrast pass mark or claim a text-contrast ratio proves sprite readability.

Production remains on the existing D-094 contract until the comparison has a recorded choice and coordinated animation/readability contract, runtime, tests and pin changes. DEBUG-only comparison controls may suppress or attenuate the Player border; they must not leak into normal play, alter enemy contrast, change geometry or change replay identity. BP-007's current-frame alignment/cache requirements still apply wherever outlines are used. A no-outline diagnostic is not a global waiver of missing-outline defects in the current delivery.

Research (accessed 2026-10-14): Riot's [VALORANT shader explanation](https://www.riotgames.com/en/news/valorant-shaders-and-gameplay-clarity) describes separate character/environment treatment and restraining silhouette lighting to avoid distraction, with emphasis toward upper-facing surfaces. This is a 3D shooter implementation, not evidence that SS should copy its Fresnel shader or numeric settings. [Game Accessibility Guidelines](https://gameaccessibilityguidelines.com/ensure-no-essential-information-is-conveyed-by-a-fixed-colour-alone/) supports redundant shape/pattern information rather than fixed colour alone. These establish relevant principles; the three SS candidate treatments and comparison opacity values are design proposals to be evaluated in SS.

### BP-008 — distinguish source sampling from displayed playback

OBSERVED (runtime e6db65d): the source geometry study holds its toe at a fixed nominal world point continuously, but uniformly holding its sixteen samples produces up to 7.44 world units of drift on the study's dense time grid. This is analytical source evidence, not a shipping-renderer measurement. The current composition fixture injects a static Player texture, removes its actions and renders with Reduced Motion; it cannot establish movement-cycle acceptance.

DOCUMENTED: Apple's [texture animation action](https://developer.apple.com/documentation/spritekit/skaction/animate%28with%3Atimeperframe%3A%29) displays each texture for its specified interval. [didEvaluateActions](https://developer.apple.com/documentation/SpriteKit/SKScene/didEvaluateActions%28%29) runs after action evaluation in a presented, unpaused scene. These distinguish the displayed texture from an expected index calculated before actions. They do not prescribe SS's acceptable foot drift or gait policy.

For BP-008 evidence, distinguish continuous source contact, exported-frame contact and actual displayed contact. A source curve's zero residual must not be reported as zero rendered slip. Record the displayed frame identity after action evaluation, the simulation tick and authoritative position, rendered actor/root position, facing and clip identity, and capture time in their respective coordinate/time spaces. Where interpolation changes rendered position, record it separately from the authoritative position. Transform authored foot landmarks using the actual displayed frame's canvas, anchor, scale and projection.

The moving benchmark must install its candidate once and retain playback across successive observations; a fixture that resets the renderer or reassigns a static texture each sample only proves composition. Use the same frame-duration/action construction as normal playback. Label deliberately diagnostic static/Reduced Motion captures as such. Do not infer an action's displayed frame from elapsed simulation ticks alone when it is driven by a different clock. Include a changing-texture sanity check so an accidentally static capture cannot pass as an animation review.

Retain BP-008's existing movement matrix. In direction reversal, stop/start, dodge and hurt interruption, record whether clip/phase restarts occur and compare their visible effect; this requirement does not select a new restart or phase-preservation policy. Compare normal and Reduced Motion separately. Do not shift the authoritative actor, alter controller speed, stretch limbs or invent a numerical slip threshold to force a passing result. Playback-policy changes still require a researched comparison and coordinated specification/runtime adoption.
