# Intent: isolated original-reference renderer trial

Author: Jcode
Date: 2026-11-16
Status: accepted
Next stage: review-only trial specification below, then runtime test tooling

Owner authorization received November 16, 2026 at 00:38 UTC following the recommendation to authorize an isolated reference-matching trial, not approve midpoint. The approved visual benchmark stays unchanged. This authorization is not projection selection, source-family detail approval, production migration, art admission or merge permission.

## Problem and outcome

BP-001 calls for original-reference versus midpoint renderer candidates. The published shipping-control/midpoint pair is not that comparison. Implement a bounded reference-ground-fit candidate using measured visible ground directions from the unchanged approved concept and compare it with midpoint through the real renderer. Record uncertainty and every source-view mismatch rather than calling a ground fit complete visual fidelity.

## Trial specification, BP-001/BP-007

1. Preserve approved concept and source-art hashes, gameplay/collision/contracts, production renderer defaults and existing evidence fixtures. Add independent test-only capture code rather than modifying prior capture sources.
2. Record manually sampled ground-only line segments in original image pixel coordinates, their feature labels, uncertainty and exclusion reasons. Fit one rotation plus vertical scale model, report residuals, and explicitly label uniform scale/translation and world-axis association as trial conventions, not recovered camera calibration. No inference of hidden wall vertices or exact camera elevation.
3. Compare midpoint and fitted-reference candidates at the same 704×326-point viewport, snapshot, source textures, anchors, lighting, field treatment, HUD, and 1×/1.25×/1.4× magnifications. Keep source art upright and attach roots to projected ground. Do not modify existing artwork to improve the trial.
4. Capture quiet and existing legal-input encounter, natural and authoritative geometry overlays, native/half/grayscale derivatives. Report points, pixel scale, source hashes, actual node bounds and gameplay digest. Any cropping or missing ground registration is a result, not a reason to change collision.
5. Validate forward/inverse mapping against actual SpriteKit coordinate conversions across eight headings and several analog magnitudes. Preserve stick magnitude and existing authoritative speed. Identical world commands retain simulation identity. No production touch mapping is installed.
6. Show approved reference and measured fit assumptions alongside actual-renderer comparisons. Run existing BP-011 palette measurements against the original approved reference. Use its existing review-flag semantics, no new acceptance bands.
7. State limitations explicitly: unchanged upright art may not match the fitted ground view. Static/mathematical checks do not prove live facing, occlusion, dense encounter, physical performance or family admission. Existing BP-005/BP-008/BP-009/BP-012 gates remain mandatory before promotion.

## Affected systems

Runtime test-only capture tooling, local calibration/verification scripts, review evidence/gallery and handoffs. SS-specs records this bounded authorization and requirements without changing a versioned gameplay contract or the runtime contract pin.

## Constraints and decisions still reserved

No new source-family detail, no modified concepts, no arena/collision changes, no source mirroring/warping to impersonate a facing, no production transform or input change. Preserve 0.375s Player settle timing. Owner projection choice remains UNRECORDED. If existing upright art prevents faithful whole-scene matching, report that result without fabricating a successful reconstruction.

## Verified and assumed claims

Verified: BP-001/BP-007 require this comparison, existing control is not a reference reconstruction, owner authorized this isolated trial. Assumed: visible ground segments admit a useful rotation/scale fit. The fit must measure and disclose residual disagreement before it can be treated as evidence.
