# Intent — device feedback loop alongside art review

**Author:** Claude (audit follow-up)
**Date:** 2026-10-29
**Status:** accepted
**Next stage:** `specs/001-single-level-vertical-slice/acceptance.md`

Accepted by the user on 2026-10-29 in chat, in response to an audit that recommended this change: "ok so whats next ? start on next items and pr when done , and keep going". Merging the pull request that carries this intent is the owner's binding acceptance.

## Problem

**OBSERVED:** The 2026-10-13 physical-device QA (runtime `docs/review/device-qa/`) failed twice. Reported failures include frame stutter, whole-view jumps, invisible blocking space, and damage with no visible source, alongside unreadable art. No physical-device run has happened since.

**OBSERVED:** `acceptance.md` § D-104 says "Produce the complete character and Camera playback review before the next physical device installation." That makes every device check wait for the full art review, including checks unrelated to art: frame time (C-003), suspend/resume (B-004, PC-008), input (PC-009) and damage attribution (combat-causality.md).

**OBSERVED:** Since 2026-10-14 nearly all runtime work has been test-only Player source art. The shipping build has not been re-measured on a phone, so the device-visible failures that are not art problems are still unverified.

## Proposed outcome

- Physical-device checks of the current build's feel, performance, lifecycle, input and damage attribution can run at any time. They do not wait for the D-104 art review.
- The D-104 visual gates are unchanged. Art is still not admitted to production until the complete character and Camera playback review, and their device evidence, pass.
- A device session records which build and which art it ran, so its results are not mistaken for art acceptance.

## Affected users/systems

Operator and owner (device sessions), runtime QA, `acceptance.md`. No change to rules, content, arena, replay identity or visual direction.

## Constraints/non-goals

- Does not weaken any D-104 gate, BP-001–BP-010 evidence requirement, or the Civic Seam visual direction.
- Does not declare any art admitted or any device gate passed.
- One level, existing roster and scope.

## Open questions

- Which device classes are available (D-020 is still `DECISION_PENDING`). The iPhone 17 Pro used on 2026-10-13 covers the current-Pro class only.

## Verified claims

- The acceptance sentence quoted above is at `acceptance.md` § D-104.
- Device QA failed on 2026-10-13 (runtime `docs/review/device-qa/README.md`, `candidate-findings.md`).

## Assumed claims

- Some of the reported stutter comes from main-thread work that art review cannot fix: lazy texture decode, per-cue audio player allocation, and evidence profiling at run end. Assumed until a device trace confirms it.
