---
title: Release candidates need subtle phase-dependent motion rather than one repeated settle rhythm
author: Daniel
date: 2026-11-16
branch: intent/receipt-contract-reconciliation-20261115
id: l-4ac9bcad
scope: repo
status: active
src: agent
touches:
  - FACTS.md
  - docs/handoff/NEXT.md
  - docs/kanban.md
---

## Decided
Owner requested slight phase variation for more dynamic motion on November 16, 2026 at 02:36:26 UTC after the all-release source review. Treat this as a refinement request, not acceptance. Use deterministic source-backed phase-specific easing and lift proposals so review is repeatable. Keep the accepted timing/contact/endpoint and original5/13 constraints.
## Watch out
Do not silently replace the published baseline or cite its native captures as proof of a new variant. Preserve a synchronized baseline-versus-candidate comparison and distinguish source verification from native/live/visual acceptance.
## In the code:
Runtime baseline: docs/review/player-all-release-source-20261116/build_source.py, generate(source, neutral), and docs/review/player-all-release-native-20261116/. New candidate: docs/review/player-release-variation-20261116/. Specs owner direction: FACTS.md and docs/handoff/NEXT.md.
