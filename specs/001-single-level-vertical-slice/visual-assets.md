# Visual Asset Specification

Status: BASELINE  
Feature: SS-001  
Visual version: `visual-civic-seam-001`

## 1. Visual thesis

Surveillance Survivor uses readable 2.5D top-down pixel art with a dark urban base and high-salience systemic signals. The image must communicate:

1. player location;
2. immediate collision and escape space;
3. surveillance geometry;
4. incoming damage;
5. enemy role;
6. objective direction;
7. atmosphere and satire.

Decoration must never compete with these signals.

The tone is **paranoid slapstick**: privatized authority appears officious, over-equipped, and slightly absurd. The presentation is tense but not horror-realistic. San Francisco identity comes from geometry, grade, fog, transit, hills, civic materials, and selected landmarks—not labels pasted onto scenery.

## 2. Readability hierarchy

When the frame becomes dense, salience MUST resolve in this order:

| Priority | Surface | Required distinction |
|---:|---|---|
| 1 | Player | Unique silhouette, persistent grounding ring, unobscured core |
| 2 | Lethal telegraph and projectile | Shape, motion, outline, and high local contrast |
| 3 | Extraction and critical objective | Stable icon plus directional cue |
| 4 | Camera field and current detection | Procedural geometry plus boundary pattern |
| 5 | Algorithmic Moderate | Scale, silhouette, persistent boss marker |
| 6 | Standard enemies | Role-readable silhouettes |
| 7 | Drops and upgrade affordances | Compact pulse and icon |
| 8 | Environment interactables | Contextual rim or icon |
| 9 | Decoration | Lowest contrast and motion budget |

No lower-priority surface may obscure a higher-priority surface for more than two presentation frames.

## 3. Palette contract

The palette is role-based, not merely aesthetic.

| Role | Baseline family | Non-color carrier |
|---|---|---|
| Player | warm ivory / amber core | circular grounding ring and four-notch marker |
| Safe or recoverable space | cool cyan | dashed boundary |
| Camera observation | cyan-white at low state | scan-line pattern and wedge boundary |
| Tracked state | amber | double boundary and TRACKED glyph |
| Hunted / lethal warning | magenta-red | triangular chevrons and pulse cadence |
| Enemy body | desaturated civic/navy/gray | silhouette and role marker |
| Player attack | warm white | round projectile and short trail |
| Enemy attack | magenta/red | diamond projectile and segmented trail |
| Extraction | green-cyan | portal brackets and EXTRACT icon |
| Neutral environment | blue-gray, asphalt, concrete | material texture |
| Collectible | gold | diamond/star icon |

Color MUST NOT be the only state carrier. Critical adjacent UI contrast MUST target at least 3:1; normal text MUST target at least 4.5:1.

### Vendor mine (D-121, D-122)

The Victorian Vendor's `receiptMine` is a procedural circle at the radius in `enemies-and-encounters.md`. It is not a catalog sprite and it adds no asset id. D-122 replaces D-121's light neutral stroke with the rules below. The radius, the 30-tick arm, the 240-tick life, the 12 damage, the cap of two, and which mine retires are unchanged.

**Colour family.** The ring's hostile stroke is the same colour the runtime draws for telegraph outlines (`Palette.telegraphStroke`, 0.95, 0.55, 0.35, about `#F28C59`). That value is orange-red: hue 20° in HSV (about 52° in CIELAB). It is the runtime's orange-red telegraph colour, not the magenta/red Enemy attack row of the table above, and this section does not claim that row. A dark neutral keyline runs round the outside of that stroke. The ring MUST NOT use neutral white or near-white. White belongs to the Player kit (the warm ivory grounding ring and the Player placeholder fill) and to the unaware `?` marker, and a mine must not read as either.

**Geometry, in world units.** All widths are world units, not points or pixels, so they scale with the scene. Every stroke is aligned inside the authoritative radius, so nothing the mine draws reaches past it. For the 42 radius:

| Band | Arming | Armed |
|---|---|---|
| Keyline (dark neutral) | 41–42, width 1 | 41–42, width 1 |
| Hostile stroke | 39–41, width 2, a sweeping arc | 37–41, width 4, a closed circle |
| Fill | clear | hostile family at low alpha (target 0.12, at most 0.15), inside 37 |

The fill keeps the ground's material readable. It is not the lethal-warning card, and it does not replace the stroke.

**Arming cue.** State is not carried by line weight alone. While the mine is arming, the hostile stroke is an arc that starts at the top of the circle and sweeps clockwise to close over the 30 arming ticks. Its sweep is 360° × (30 − `armRemaining`) / 30, from the arming count the presentation snapshot already carries. The keyline is a full circle from the first tick, so the extent is visible before the arc closes. The arc closes on the tick the mine arms, and the armed ring, its wider stroke and its fill appear on that tick. Under Reduced Motion the arming stroke is static: a full closed circle at width 2 with no sweep. Arming and armed then still differ by width and by fill.

**Damage reads after the body crosses.** Damage is tested against the Player's centre (circle centre within the mine radius), not the Player's body. The Player's collision radius is 18 (`player-controller.md`), so the body reaches the ring's outer edge when the centre is 60 from the mine and covers the whole ring band before damage applies at 42. The ring shows the edge the Player's centre must not cross. It is not a body-contact edge.

**Not by hue alone.** The mine ring is distinguished from the HUD Hunted / lethal warning state by shape, keyline, and location, not hue. Hunted (0.93, 0.58, 0.30) is close to the ring's colour: CIEDE2000 6.4 with typical colour vision, 2.0 under simulated deuteranopia and 3.5 under simulated protanopia (Machado 2009, severity 1.0), with a CIELAB lightness gap under 1, so to a deuteranope the two are effectively one colour. The ring is a circle on the ground at the mine's authored radius, where the mine lies, with a full dark keyline from its first tick and, while arming, a sweeping arc. Hunted is a HUD state carried by triangular chevrons and pulse cadence (table above) and never draws as a ring in the world. Against the HUD Tracked amber (0.90, 0.78, 0.35) the ring also separates by colour (CIEDE2000 27.45 typical, 8.2 deuteranopia, 13.9 protanopia), so the concern that it would read as Tracked is not supported by the arithmetic. Neither separation may rest on hue.

The patrol cone owns the dash, so this ring is not dashed. No caption is added. An armed mine is not the lethal-warning card.

**Contrast requirement.** The ring MUST reach at least 3:1 non-text contrast (WCAG 2.2 Success Criterion 1.4.11) in both states, on the asphalt family (`#343D43`) and on the stucco family (`#A79C8B`, with civic limestone `#BDB39F` as its light end):

- the hostile stroke against the keyline;
- the ring's outer edge against the ground beside it, measured on whichever of the keyline or the hostile stroke gives the higher ratio on that ground.

This is a requirement, not a recorded result. It is verified only by the review plates in task T1060: each ground, arming and armed, native scale and half scale, colour and grayscale, Reduced Motion off and on, plus one plate of the Player body crossing the ring before damage, plus a colour-blind plate: the ring, arming and armed, beside the HUD Hunted and Tracked states under deuteranopia and protanopia simulation, showing that each is identified by shape, keyline, and location. Until those plates are recorded, the ring's contrast and its colour-blind read are NOT_COMPUTABLE.

**Unity note (informative).** The world unit is the simulation unit. If a Unity build draws this ring, map one world unit to one Unity unit and set widths in those units, not in screen pixels. Unity's `LineRenderer` centres its width on the path, so draw each band on a path inset by half its width (the keyline at radius 41.5, the armed stroke at 39, the arming stroke at 40), or use a mesh or shader ring with explicit inner and outer radii. Do not use an outline or glow effect that grows outward past the radius.

## 3a. Environment asset reachability

`presentation-assets-003` carries `environmentAssetIds` alongside
`requiredAssetIds`, `audioEventIds`, and `musicAssetIds`. Environment art is
runtime-reachable on the same footing as interface art, and the runtime bundle
filter admits it by the same rule.

Without that array environment art is unreachable **by construction**: the filter
only bundles assets an ID names, so admitted environment work would be excluded
however correctly it was produced. This is the same gap `musicAssetIds` closed
for music, found the same way — art existed and nothing could load it.

The array names 41 IDs:

| Group | Count | Derivation |
|---|---:|---|
| Ground tiles | 6 | one per authored surface |
| Solids | 14 | **one per `permanentSolids` entry in `civic-seam-arena-004`**, named for it |
| Camera housings | 5 | one per family in the `camera-placement-001` enum |
| Street props | 12 | the P0 infrastructure kit in `civic-seam-001` §5 |
| Motif sheets | 4 | phoenix, repair, counter-signal, broadcast glyph |

The solid IDs are derived from the arena manifest rather than authored
separately, so a solid cannot exist without art or art without a solid. If the
arena gains or loses a solid, this list moves with it.

Environment art is **not** required for a run to start. An unbacked solid keeps
its authored blockout, on the same all-or-nothing principle as clip coverage:
partial art is a legibility hazard, not a partial improvement.

## 4. Perspective and world scale

- Projection: top-down 2.5D, approximately 3/4 presentation, with collision defined separately.
- The first-release projection reference is [visual-reference.md](visual-reference.md): the user-selected street-corner scene, refined to an intermediate elevated angle. Player, roof, municipal dome, upright prop and ground must agree in one actual-scale scene.
- Authoring grid: 64 logical world units.
- One traversal cell: 64 × 64 units.
- Canonical actor footprint: 28–36 units in diameter.
- Canonical visual sprite box: 64 × 64 pixels for Player and standard enemies.
- Improper Search Daemon visual box: 80 × 80 pixels. Algorithmic Moderate visual box: 96 × 96 pixels.
- Camera pole box: 64 × 96 pixels.
- Large environment modules: multiples of 64 pixels.
- Texture filtering: nearest-neighbor for pixel assets.
- Camera and collision MUST never infer geometry from opaque sprite bounds.

Sprites may exceed their collision footprint for hats, coats, weapons, or antennas. The ground-contact point MUST remain stable across every animation frame.

## 5. Required asset inventory

### Player

| Asset group | Minimum |
|---|---:|
| Idle | 4 frames × 4 directions |
| Move | 16 distinct frames × 4 directions (D-104 production target) |
| Dodge/Ghost Step | 4 frames × 4 directions |
| Hurt | 3 frames × 4 directions |
| Defeat | 6 frames |
| Extraction | 6 frames |
| Grounding ring | procedural or 1 reusable texture |
| Aim/attack | procedural weapon orientation or 2–4 frame overlay |

### Enemies

Each standard enemy requires idle, move, attack/commit, hurt, and defeat presentation. All five canonical archetypes MUST have different silhouettes at thumbnail scale.

| Asset group (each standard enemy) | Minimum |
|---|---:|
| Idle | 4 frames × 4 directions |
| Move (not the Autonomous Informant, whose pursuit clip is its locomotion) | 16 distinct frames × 4 directions (D-104 production target) |
| Attack anticipate / commit | delivered (`clip-metadata-001`) |
| Hurt | 3 frames × 4 directions |
| Defeat | 6 frames × 4 directions |
| Recover (Cable-Car Correlator only) | 3 frames × 4 directions, 45 ticks |

Frames are 64 × 64 in the `playerAndStandardEnemy` box, anchored at (32, 56). The exact frame IDs are the `plannedOriginal` records in `asset-catalog-001` (D-071).

The D-071 six-frame planned records and current `clip-metadata-001` describe the previous delivery baseline. Before a 16-frame clip is admitted or bundled, amend the catalog, clip metadata, manifest and frame IDs together and validate parity against the runtime pin. Six existing frames do not become sixteen by interpolation or repeated IDs. Do not add locomotion clips to stationary/attack-only roles just to match the player count.

| Role | Visual identity |
|---|---|
| Fog Analytics Cloud | suspended clustered mass, soft perimeter, obvious pulse aperture |
| Cable-Car Correlator | long forward chassis, rail/route motif, committed charge axis |
| Sutro Signal Witch | tall narrow mast silhouette, cast antenna, ranged posture |
| Autonomous Informant | forward lean, narrow body, high-frequency leg silhouette |
| Victorian Vendor | broad loaded torso, receipt/projector appendage, deliberate stride |
| Improper Search Daemon | 1.25× mass, query apertures, dash-axis silhouette |
| Algorithmic Moderate | at least 1.5× mass, official geometric insignia, unique head/shoulder profile |

### Surveillance and objectives

- Camera pole base, mast, head, damaged state, destroyed state
- Procedural Camera field with state variants
- Camera acquisition reticle
- Exposure state glyphs
- Extraction locked, armed, active, interrupted, and complete states
- Boss health frame and phase markers
- Directional objective arrow
- Upgrade icons: Signal Jammer, Ricochet Pulse, Ghost Step

### San Francisco environment

Required modular families:

- asphalt and lane-marking tiles;
- concrete sidewalk and curb transitions;
- civic plaza paving;
- service alley walls, doors, dumpsters, and utility fixtures;
- transit platform edge and shelter components;
- hill/stair/ramp visual language;
- fog overlays;
- bollards, planters, barriers, kiosks, and street furniture;
- cable/transit motifs used sparingly;
- one distant landmark silhouette layer;
- surveillance retrofit variants for civic objects.

Text embedded in world textures is prohibited except for approved fictional diegetic signage that remains legible and non-essential.

## 6. Materials and collision legibility

Every blocking object MUST have:

- a stable ground contact;
- a boundary readable against every adjacent floor family;
- no transparent visual invitation into blocked space;
- a collision footprint that is smaller than or equal to the perceived solid base.

Every traversable transition MUST avoid false walls caused by high-contrast seams. Decorative shadows MUST NOT resemble Camera fields, projectiles, hazards, or navigable openings.

## 7. Procedural visual systems

The following MUST be procedural or data-driven:

- Camera fields and occlusion clipping;
- detection boundary patterns;
- target reticles;
- health and state rings;
- projectile trails;
- objective arrows;
- Extraction countdown;
- Exposure meter;
- fog density response;
- damage flash and hit-stop presentation;
- debug collision and line-of-sight overlays.

Baking Camera wedges, collision guides, captions, or state labels into environment art is prohibited.

## 8. VFX budget and language

| Event | Default presentation | Reduced presentation |
|---|---|---|
| Camera acquire | contracting reticle + short scan | static reticle + opacity step |
| Exposure threshold | HUD pulse + edge brackets | icon swap + short highlight |
| Player hit | 1–2 frame impact, directional arc | directional arc without screen flash |
| Enemy hit | compact spark, ≤ 120 ms | outline change |
| Enemy defeat | 4–8 particles, ≤ 350 ms | dissolve or 2-particle cue |
| Ghost Step | afterimage trail, ≤ 300 ms | single outline echo |
| Ricochet | segmented path trace | impact markers only |
| Lockdown | one controlled scene pulse + barriers | static perimeter change |
| Captain telegraph | ground shape + body anticipation | ground shape + phase icon |
| Extraction | inward particles + stable brackets | brackets + progress fill |

No gameplay VFX may use uncontrolled full-screen white flashes. Particle emitters MUST be pooled or bounded, use finite lifetimes, and stop emission when offscreen or irrelevant.

## 9. HUD and safe-area contract

- Support landscape left and landscape right.
- All critical controls and text MUST remain inside the current safe area.
- Virtual stick placement MUST support left- and right-handed modes.
- Critical gameplay HUD MUST occupy no more than 18% of the unobstructed play area during normal play.
- The center 60% of the viewport SHOULD remain free of persistent opaque UI.
- Player health, Exposure, current state, upgrade identity, and objective MUST be readable without opening a menu.
- Upgrade selection and result screens MUST support VoiceOver and Dynamic Type up to 200% through reflow or scrolling.
- Touch targets MUST be at least 44 × 44 points.

## 10. Texture and atlas contract

Atlas groups follow simultaneous use rather than directory convenience:

- `player.atlas`
- `enemies_standard.atlas`
- `captain.atlas`
- `sf_environment_core.atlas`
- `sf_environment_props.atlas`
- `surveillance_ui.atlas`
- `combat_vfx.atlas`
- `hud.atlas`

Rules:

- Preload the next encounter's required atlases before the encounter admits entities.
- Do not place all art in one atlas.
- Do not split every frame into separate runtime loads.
- Record decoded memory estimates per atlas.
- Reject duplicate content hashes under different names unless documented.
- Use opaque/replace blending where visual output permits.
- Assets not reachable in SS-001 MUST NOT ship in the application bundle.

Apple recommends texture atlases for textures rendered together and warns that overly large atlases increase memory use. The atlas layout therefore requires measurement rather than a fixed universal maximum.

## 11. File contract

Naming:

`{domain}_{role}_{state}_{direction}_{frame}@{scale}.png`

Example:

`actor_autonomous_informant_move_ne_03@1x.png`

Each source asset record MUST include:

- stable asset ID;
- role;
- source file;
- delivery file;
- pixel dimensions;
- color space;
- alpha requirement;
- anchor;
- visual bounds;
- intended atlas;
- animation clip IDs;
- content hash;
- license/provenance;
- authoring tool and export version;
- approval state.

Delivery PNGs MUST use sRGB, clean alpha, deterministic names, and exact approved dimensions. Masters remain outside the runtime bundle.

## 12. Visual validation

Every asset family MUST pass:

- dimension and color-space validation;
- non-empty opaque-content validation;
- alpha-edge inspection;
- nearest-neighbor scale inspection;
- contact-point stability;
- silhouette test at 50% gameplay scale;
- grayscale and color-vision simulation;
- light/dark background contrast plates;
- dense-combat occlusion plate;
- reduced-motion presentation plate;
- license and provenance check;
- runtime atlas lookup test.

A beautiful asset that weakens gameplay readability fails.


## 13. Civic Seam environment authority

The canonical location-specific direction is `civic-seam-visual-direction.md`. When a general visual rule conflicts with that artifact, gameplay readability remains supreme and the conflict requires a recorded decision.

The environment MUST use:

- a southwest–northeast diagonal transit spine;
- Victorian/Edwardian Residential Wedge;
- rail, trolley-wire, island, and ventilation infrastructure in Transit Cut;
- formal Classical massing in Civic Plaza and Phoenix Steps;
- brick, steel-sash, fire-escape, loading, and rooftop-service language in Service Seam;
- temporary sensor infrastructure at Grid Junction;
- restrained Art Deco authority language at Captain Court.

The approved environment palette extends the role palette with the exact material colors in the Civic Seam direction. Surveillance cyan and Detection red remain active-system colors, not general decoration.

## 14. Location-specific production inventory

P0:

- diagonal road/rail modules;
- Victorian, Edwardian, and Classical façade families;
- Civic Plaza landmark kit;
- six Camera housing families;
- trolley-wire system;
- two-layer fog;
- core street furniture;
- Detection State materials;
- original phoenix relief;
- basic rooftop kit.

P1:

- fire escapes;
- Art Deco corner/court kit;
- transit shelter and island;
- parklet;
- original protest-poster decals;
- seismic retrofit kit;
- signs/signals;
- pigeon and parrot animation;
- fictional autonomous vehicle;
- distant three-pronged tower glyph.

P2:

- window-interior cards;
- rare environmental events;
- rooftop narrative props;
- fictional historic plaques;
- repair variations;
- rain-darkened material state;
- storefront dressing;
- architectural Camera disguises.

P1 and P2 assets may not delay P0 gameplay acceptance.

## 15. Location-specific prohibitions

No Golden Gate Bridge, arbitrary cable car, exact civic seal, real logo, copied street art, full-neon cyberpunk skin, geographically incoherent neighborhood mixture, or dense fog that weakens gameplay truth may ship.


## 16. Camera destruction assets

The normative behavior is `camera-destruction.md`.

Every standard housing family requires:

- Operational Integrity 3 state;
- Damaged Integrity 2 state with one non-color damage marker;
- Critical Integrity 1 state with two-notch/non-color damage marker;
- Destroyed Integrity 0 state with broken-lens silhouette and no emissive field;
- compact hit VFX;
- bounded destruction VFX;
- field-off transition;
- three-notch targeting/Integrity HUD.

Housing damage art MUST NOT imply reduced detection before destruction. Destroyed debris has no collision and may not resemble loot.


All eight standard Cameras use stationary housings. No Camera animation may imply panning, tracking rotation, patrol, relocation, or changing field geometry. Housing families distinguish institutional provenance, not mechanics.

For release one, the five logical seeded housing-family values share a single visible municipal-dome presentation family (D-104). The earlier five-family asset inventory and D-073 admission are historical production facts, not a requirement to layer or ship all five visible housings now. Asset manifest/catalog reachability must be reconciled when the complete municipal sheet is admitted. Each standard Camera draws one complete device frame; the legacy head and old family housing must not be stacked. Captain emitters retain distinct boss-owned cues and no standard Integrity treatment; see [visual-reference.md](visual-reference.md).


## Runtime presentation identity

The required HUD, control, telegraph, objective, and audio IDs are enumerated by `contracts/presentation-assets-003.json`. Shipped asset records must resolve every required ID exactly once. Missing, duplicate, unreachable, or undeclared runtime-facing IDs fail asset validation before release.
