# Intent — combat correctness and causality

Date: 2026-10-13
Status: accepted
Next stage: specs/001-single-level-vertical-slice/combat-causality.md

Accepted user instruction: “go ahead with phases 1 and 2. deepen the specs and fix the combat issues, then run the tests before we move on”.

## Problem and outcome
OBSERVED: wall hit times are always zero, mine feedback points to its owner, unrelated projectile hits create ricochet traces, and presentation history retains expired IDs. Fix these and clarify weapon/upgrade/damage presentation before further art production.

## Constraints
One player, one weapon, three upgrades, one level. Hooded player is acceptable; no new art is approved. Phase 3 is accepted by the subsequent user instruction below; art and device testing remain deferred. Collision and event changes require a new ruleset and canonical fixture review, not weakened assertions. No release merge is authorized.

## Open questions
Physical weapon design and character turnarounds require later art review. Physical performance and comprehension remain unproven.

## Phase-3 authorization
Accepted: “go ahead with phase 3, improve the weapon and upgrade feedback and run the tests before we move on to art and device testing”. Implement the already specified aim/fire, conditional Jammer contour, actual Ghost Step concealment boundary and accessible protected selection overlay (T1035 / CC-008). Automated evidence precedes art and physical-device acceptance.
