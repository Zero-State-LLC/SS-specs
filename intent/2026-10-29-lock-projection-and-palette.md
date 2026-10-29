# Intent — lock the release projection and palette before more per-asset detail

**Author:** Claude (audit follow-up)
**Date:** 2026-10-29
**Status:** accepted
**Next stage:** `visual-reference.md`, `benchmark-production.md` (BP-001), `civic-seam-visual-direction.md` § 10

Accepted by the user on 2026-10-29 in chat: "accept, and merge". The next stage is specify; open questions stay open until the specification answers them.

This intent does not change the art direction. It asks for the two decisions the direction already requires to be recorded, so that production follows them.

## Problem

**OBSERVED: the projection has not been chosen.** BP-001 says: "Test the original-reference and midpoint projection candidates in the existing 704×326 gameplay viewport before choosing the production projection. Record the choice and the comparison images." No choice is recorded.

The runtime projection guide (`docs/review/projection-guide/review.md`) still treats the +45°/half-height transform as "a measurable experiment, not an angle recovered from the approved concept". It shows that this transform halves each solid's projected area and doubles the world area visible at 704×326. The benchmark status says the facing/travel mapping is unresolved ("current +45°/half-height comparison sends world south down-right").

Meanwhile, from 2026-10-14 to 2026-10-25, the Player's south/front source received detailed work on boots, knees, laces and settle timing. All of that depends on a projection and facing mapping that is not settled. If the projection changes, that work is redone.

**OBSERVED: the palette has drifted from the approved concept.** Measured over whole frames, downsampled to 300 px wide, with each pixel assigned to the nearest § 10 palette colour:

| Image | Mean luminance | Mean chroma | Dominant § 10 colours |
|---|---:|---:|---|
| Approved concept (`docs/review/phase4/street-corner-approved-concept.png`) | 85 | 11 | asphalt 38%, brick shadow 27%, stucco 15% |
| Midpoint concept | 86 | 13 | asphalt 37%, brick shadow 27%, stucco 13% |
| Latest shared-scene capture (runtime `docs/review/street-surface/BP004-street-shared-scene-paired-integrity-3.png`, HUD rows excluded) | 135 | 30 | **stucco 73%**, teal 10% |

The capture is about 59% brighter and 2.6× more saturated than the concept. It is mostly light paving where the concept is mostly asphalt blue-grey (`#343D43`).
- Its building is a free-standing teal/brick box. The concept has a limestone civic corner inside a street wall, with kerb, crosswalk and rails, as § 1 and § 4 require.
- § 10 reserves bright colour for "active information and threat". On pale ground the Camera field loses contrast, which `acceptance.md` § D-104 already records as a pale-ground grayscale failure.

**OBSERVED: breadth is far behind depth.** The cast in `visual-reference.md` needs, before release:
- six enemy roles plus the boss, each with four-facing identity reviews;
- the municipal Camera's complete state set;
- the 20–25-module architecture kit (§ 4).

Enemy production is deferred until the Player is complete (`plan.md`, kanban). The Player has one partially accepted facing after roughly two weeks.

## Proposed outcome

1. **A recorded projection choice.** One of the BP-001 candidates is chosen and recorded with its comparison images, from a real-renderer scene with a legal encounter and HUD, as BP-001 already requires. The facing/travel mapping and input inverse follow from it. All further source art is authored against it.
2. **A palette conformance check for review plates.** Every BP review plate reports mean luminance, mean chroma and the nearest-§ 10-colour distribution next to the approved concept's values. A plate outside an owner-set band is flagged for review, not auto-rejected. The approved concept stays the reference.
3. **A fidelity bar per family.** The bar is the existing review: native size, 50% scale and grayscale at 704×326. Detail that is invisible at that bar does not block admission. Families advance in breadth: four Player facings, then the municipal Camera, then enemy roles, then the environment kit.

## Affected users/systems

Art production (Aaron, artist, owner), `benchmark-production.md`, `visual-reference.md`, `civic-seam-visual-direction.md` § 10 (reference values only), and runtime review tooling (a small script). No gameplay, collision, ruleset or replay change.

## Constraints/non-goals

- The Civic Seam direction, the approved and midpoint concepts, the D-104 gates and BP-001–BP-010 are unchanged. This intent makes their required decisions explicit; it does not lower them.
- The arena stays axis-aligned (§ 5b). The projection is presentation.
- No concept image is admitted as a sprite.

## Open questions

- Which projection? This needs the owner's eye on the BP-001 comparison in the real renderer.
- The width of the palette band, and whether it applies per zone. The Civic Plaza is legitimately lighter stone than the Transit Cut.
- Is the shared-scene building a stand-in for layout, or a candidate for production? If it is a candidate, it should be redone as a limestone/stucco civic corner set into a street wall.

## Verified claims

- The quoted BP-001 text, the projection-guide finding and the benchmark-status note are in the files named above.
- The palette numbers are reproducible from the named images with the method stated above the table.

## Assumed claims

- Locking the projection before more Player detail reduces rework. This is inferred from the guide's finding that the transform changes footprint, framing and facing.
