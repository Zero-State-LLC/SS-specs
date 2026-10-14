# Intent — combat correctness and causality

Date: 2026-10-13
Status: accepted
Next stage: specs/001-single-level-vertical-slice/combat-causality.md

Accepted user instruction: “go ahead with phases 1 and 2. deepen the specs and fix the combat issues, then run the tests before we move on”.

## Problem and outcome
OBSERVED: wall hit times are always zero, mine feedback points to its owner, unrelated projectile hits create ricochet traces, and presentation history retains expired IDs. Fix these and clarify weapon/upgrade/damage presentation before further art production.

## Constraints
One player, one weapon, three upgrades, one level. Hooded player is acceptable; no new art is approved. No phase-3 implementation. Collision and event changes require a new ruleset and canonical fixture review, not weakened assertions. No release merge is authorized.

## Open questions
Physical weapon design and character turnarounds require later art review. Physical performance and comprehension remain unproven.
