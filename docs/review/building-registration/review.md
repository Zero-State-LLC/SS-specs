# Building registration investigation — BP-005 / BP-007

OBSERVED at runtime 9501261: the benchmark uses solid-03-transit-kiosk, center (576,704), half-size (64,64). The candidate building is 673×768 pixels, drawn 190×217 with bottom-center at (576,640). The texture contains two houses, stairs, planters and an outer sidewalk apron. It is not a bare wall footprint.

Approximate visible outer-paving samples, recorded in registration.json, map to world (482.69,693.12), (584.61,643.67), (668.74,701.03). The unchanged collision spans x=512…640, y=640…768. The outer left/right samples extend about 29.31 and 28.74 units beyond its x bounds. These are paving observations, not collision vertices. The hidden rear ground boundary is NOT_COMPUTABLE from this image. The roof must not substitute for it.

## Researched repair path

Tiled distinguishes tile-image alignment from independently authored collision objects: https://doc.mapeditor.org/en/stable/manual/objects/ . Apple describes node placement in parent coordinate systems: https://developer.apple.com/documentation/spritekit/about-spritekit-coordinate-systems . Accessed 2026-10-14. These support explicit registration and separate geometry; they do not select SS's aesthetic projection.

PROPOSED: author a ground-plan master for the representative building with separately identified wall base, steps, planting beds and walkable apron. Keep the current immutable obstacle as the comparison authority. Compare a source redrawn for the existing projection against a coherent projected-world candidate. A projected-world candidate must transform every ground-space primitive and invert input consistently; upright sprites retain their authored vertical form and attach at projected roots. Transforming the entire finished scene would also flatten upright art and is not equivalent to ground projection.

No hidden vertex or new collider is inferred. No whole-texture warp can be accepted as the repair: wall planes, upright details and ground apron need distinct treatment. Retain the original material palette and facade details where possible. A production choice requires front/rear/corner traversal, projectile contacts, camera field alignment, depth/occlusion and legal encounter captures at native scale. The current isolated still cannot pass those gates.

Next source deliverable: top-view ground plan plus matching elevated building render, labeled contact landmarks, explicit walkable versus solid regions, and separate ground/vertical layers. This is a repair of existing content, not a new gameplay obstacle or level.
