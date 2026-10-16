# Intent — shared projection and visual coherence

**Author:** SS-001 art and specification pass
**Date:** 2026-10-13
**Status:** accepted
**Next stage:** `specs/001-single-level-vertical-slice/visual-reference.md`

The user authorized phase 4 of the remaining-findings plan: deepen specifications and show a shared top-down reference scene before the camera renderer fix. They chose the first generated street-corner scene as the look, then asked for the final viewing angle somewhere between that scene and a higher overhead study, using our judgment. The hooded player and urban street theater direction remain in scope.

## Problem

**OBSERVED:** The current art set mixes viewing angles and contains disconnected fragments, large transparent margins and camera hardware drawn twice. Earlier character studies looked side-on, varied little between frames, and did not provide valid production loops. The visual contracts still require six movement frames and five visible housing families, despite the agreed 16-frame locomotion target and one municipal housing for the first release.

## Proposed outcome

One coherent elevated three-quarter street scene becomes the visual reference for player, camera, architecture, upright prop and ground. Four player facings and future motion share its projection and scale. A standard Camera appears as one complete municipal device. The existing deterministic family identity remains recorded; first-release presentation maps it to one housing. Every repaired asset must preserve readable gameplay geometry and provenance.

## Affected users/systems

Players see coherent orientation, contact, scale and surveillance hardware. Artists and runtime implementers receive testable reference and clip requirements. Specification, catalog, asset intake and QA tasks are affected. No authoritative combat or placement behavior changes in this phase.

## Constraints/non-goals

One level, one player, existing roster, one weapon and three upgrades. Do not add a second camera behavior, new attack, invented diagonal facing, new game mechanic or replay identity. The approved concept scene is a visual direction, not a sprite atlas or proof of collision, runtime performance or animation. The camera renderer repair and physical device pass are later work.

## Open questions

The four-facing player turnaround and 16-frame locomotion proof must still demonstrate consistent projection and actual motion. Production camera clips, precise building footprint mapping, object depth and the D-021 memory budget remain to be measured before asset admission.

## Verified claims

**OBSERVED:** The user explicitly liked the first street-corner concept and requested an intermediate viewpoint. The two reference images are saved under `docs/review/phase4/`. The candidate six-state municipal sheet is not a complete camera clip set. Existing camera placement records a seeded housing family and includes a four-family legal-result constraint. Existing clip contracts and catalogs still enumerate six-frame movement.

## Assumed claims

**PROPOSED:** The midpoint image is the working projection candidate. Its merits must be tested at actual game scale with four facings, collision/base overlays and motion. Presentation can use one municipal housing while retaining legacy seeded family metadata and RNG consumption; runtime/spec parity must verify this before integration.
