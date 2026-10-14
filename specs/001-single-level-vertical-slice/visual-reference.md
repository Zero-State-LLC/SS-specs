# Shared top-down visual reference — release one

Status: phase-4 reference candidate; native-size art proof pending
Feature: SS-001
Authority: user-selected street-corner direction and intermediate-angle refinement, 2026-10-13

This document specifies what the first-release art must communicate. The linked images are concept references. They are not production sprites, source masters, registered animation, collision data or evidence that the game already renders this way.

[Benchmark production](benchmark-production.md) defines BP-001–BP-006: shared sample, source delivery, exact locomotion scope, Camera settling states, environment mapping and evidence/adoption sequence.

## Reference scene and projection

- [User-selected street corner](../../docs/review/phase4/street-corner-approved-concept.png) sets mood, palette, character scale and architectural detail.
- [Midpoint projection study](../../docs/review/phase4/street-corner-midpoint-concept.png) is the working angle between the selected scene and the later overhead trial. The final production reference must be judged in the actual game scene, not by a numerical camera-angle claim.
- A single elevated three-quarter viewpoint governs actor, camera, building, prop and ground together. The top of the hood and shoulders, building roof, municipal dome and newsbox must all be visible. Vertical façades retain enough height to establish city character without turning east/west actors into eye-level side profiles.
- Ground is one navigable plane. Player boots, building base, pole base and upright-prop base contact that plane. Roofs and upright surfaces may overhang their authoritative footprints; they must not suggest a false open route or an invisible wall.
- The street grid, diagonal transit edge, sidewalk, civic materials and single municipal sensor communicate the Civic Seam. Keep texture secondary to player, field and attack readability. No arbitrary extra lens, duplicated hardware, fantasy staff, tourist collage or loose fragments.

## Reference composition at gameplay scale

The phase-4 proof uses one hooded player, one complete municipal dome Camera, one representative civic/Victorian corner building, one upright newsbox or hydrant and ground/curb/rail textures in the same scene. Provide two views: natural scene and overlay with authoritative footprints, mount/base points, player contact circle and field origin. The overlay is drawn from actual geometry when implemented; the concept image must not be traced to invent gameplay rectangles.

Check the scene at native phone size and at 50% gameplay scale, in grayscale, with the player passing in front of and behind the building/prop. The player and device must remain legible. Capture false openings and occlusion errors as defects, not as artistic interpretation. Use one light direction and one apparent object scale across all families.

## Player design and four facings

The player is one hooded urban participant. Weathered street jacket, practical boots and gloves, satchel/utility strap and a compact Civic Pulse device are the current costume proposal, pending a four-facing native-size review. The hood remains a functional silhouette, not a fantasy cowl. Small warm equipment light may reinforce the Pulse; it cannot replace the weapon's non-color form or shot cue.

N, E, S and W are four distinct authored body orientations from the same elevated view. South shows hood crown and shadowed opening; north shows back of hood and rear equipment; east/west show hood top, shoulder top and foreshortened torso, not full-height side profiles. Equipment position must rotate consistently with the body. Mirroring is allowed only if strap, device, asymmetrical clothing and lighting stay physically credible. The player retains the agreed 64×64 logical canvas and (32,56) ground anchor until a separately reviewed mapping change.

An identity sheet requires four neutral poses at matched scale before animation. It is not a movement loop. The locomotion proof then requires 16 distinct chronological frames for each actual movement-facing clip: ground contact, compression, passing, lift and extension with alternating limbs and a clean loop seam. Do not duplicate poses to fill the count. Movement rate, Dodge and attack timing remain authoritative and independent of frame count. Validate at normal speed, slowed playback and frame step before detail cleanup.

## Role identity in the same world

All characters share the same street-theater civic setting and projection, while each role communicates its attack before impact. The following physical readings are **candidates to test**, not researched costume facts or admitted sprites. The [design-choice research](../../docs/review/phase4/design-choice-research.md) defines the silhouette, rotation and phone-scale comparison that selects or revises them.

| Role | Physical reading and motion | Avoid |
|---|---|---|
| Fog Analytics Cloud | cluster of sensor/fog modules around a stable pulse aperture; circulation and swell, not a human walk | disconnected smoke bits hiding the pulse |
| Cable-Car Correlator | fictional narrow transit chassis with visible wheels/route apparatus and fixed charge axis | arbitrary tourist cable car or human gait on wheels |
| Sutro Signal Witch | street performer or counter-signal operator with a practical antenna mast and ranged gesture | fantasy wizard hat, staff, robe or spell silhouette |
| Autonomous Informant | compact civic courier/runner with forward pursuit posture and readable contact body | identical guard silhouette or duplicated legs |
| Victorian Vendor | improvised street seller with a grounded cart/receipt device; deliberate constrained stride | floating cart parts or detached projectile origin |
| Improper Search Daemon | heavy inspector/search apparatus, broad query frame and clear dash axis | amorphous armor or unexplained extra weapons |
| Algorithmic Moderate | outsized officious civic authority with unique head/shoulder mass and boss-owned signal hardware | generic glowing-eyed knight or ordinary enemy silhouette |

Each actor receives a four-facing identity review where its state requires orientation, a clip-coverage matrix from the authoritative state machine, and attack anticipation/commit evidence. A stationary or attack-only state is not assigned a fictitious walk. Actual game-scale and no-color recognition decide admission, not illustration detail or sheet hashes alone.

## Civic Pulse, upgrades and damage in the scene

The Pulse is a compact carried or worn civic counter-signal device attached consistently to the player. Its emitted aim/fire cue follows the selected shot direction independently of walking facing. The visual muzzle can be offset for legibility only if the beam/trail makes the actual authoritative origin and wall collision understandable. Show aim, fire, travel and hit/miss together at phone scale.

Signal Jammer's contour appears only on actual reduction; Ricochet shows a true same-projectile continuation; Ghost Step shows concealment only in its inclusive window. Ordinary Dodge must read differently. Weapon and upgrade effects retain distinct non-color shapes and cannot bury the player or Camera field. Death review compares the visible contact or communicated offscreen hazard against recorded source evidence.

## Camera presentation

For this level, all eight selected standard Cameras present the same **municipal dome** complete-device family. Logical `housingFamily` selection, four-family legal-layout check, receipt and RNG consumption remain unchanged for ruleset-008. Their values record placement identity, not a promise of four visible housings in release one. Do not silently change socket eligibility, selection, replay identity or fairness fixtures.

One camera entity presents one full 64×96 device frame at fixed mount anchor (32,88), including pole and dome. Operational, Damaged, Critical and Destroyed remain distinguishable without color or rapid blinking; 3→2→1→0 Integrity and field timing do not change. No legacy camera head or second housing may overlay this device. The six-state municipal study is a design influence, not the complete clip set or admitted asset.

Captain emitters remain indestructible boss-owned attack sources. Their appearance should share municipal construction language but carry a persistent non-color boss/locked marker and distinct active telegraph. They must not display standard Camera Integrity or invite three-hit targeting. This resolves the first-release one-family look against D-078's earlier unique Art Deco housing direction without changing boss mechanics. Its production asset IDs and decision history require explicit catalog reconciliation before integration.

## Environment mapping and production admission

Solids need a visible base that covers the blocked footprint. The source canvas, alpha bounds, visible base, world scale, render anchor and authoritative AABB are separate recorded values. Never derive collision from alpha; never auto-crop a padded solid and silently stretch it back. Upright props use explicit ground anchors and depth review. Ground tiles keep seams and linear infrastructure coherent; fog stays below important threats.

The 46-image environment inventory is reviewed by ID: retain, repair, replace or exclude. The current scene is a reference for projection and material consistency, not a blanket approval of every existing environment image. Production follows approved turnaround → controlled poses/layers → deterministic export → frame registration → review plates → provenance and manifest intake. Generated grids whose frames must align are concept studies only.

## Phase-4 acceptance before the camera renderer fix

The specifications, decision, plan, tasks and acceptance below must agree on the midpoint reference, 16-frame movement goal and one visible municipal standard-camera family while preserving logical placement identity. Deliver the reference scene and visual comparisons to the user. This visual review can settle projection direction; it does not certify animation, runtime art, collision or device performance. Camera production and renderer changes follow as the next phase.

The [phase-4 research ledger](../../docs/review/phase4/researched-open-questions.md) names the technical questions that the concept cannot answer. The [design-choice research](../../docs/review/phase4/design-choice-research.md) records why the viewpoint, world language, character and Camera choices are proposed and what must be observed before they become production decisions. In particular, clip timing, 64×64 fidelity, depth behavior and D-020/D-021 device/budget decisions remain open.
