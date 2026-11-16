---
title: Keep the approved art benchmark separate from midpoint ground projection
author: Daniel
date: 2026-11-16
branch: intent/receipt-contract-reconciliation-20261115
id: l-42b4872a
scope: repo
status: active
src: agent
touches:
  - FACTS.md
  - docs/handoff/NEXT.md
  - intent/2026-11-16-grounded-motion-ten-slices.md
  - docs/review/phase4/street-corner-approved-concept.png
  - docs/review/phase4/street-corner-midpoint-concept.png
---

## Decided
- At2026-11-16 04:22:37UTC the owner rejected the latest Camera review: it does not match the benchmark. Withdraw the recommendation of the alternate-midpoint concept extraction. The fixed street-corner-approved-concept.png remains the source fidelity target.
- Choosing midpoint ground projection did not approve a new source-camera elevation, material or proportion benchmark. A source test passing and an exact extraction from a different reference do not establish benchmark fidelity.
## Tried and ruled out
- Camera attempt02 extracted street-corner-midpoint-concept.png. Its prior recommendation is withdrawn after the owner rejection. Preserve attempts01/02 as rejected history rather than silently replacing their evidence.
## In the code:
- FACTS.md
- intent/2026-11-16-grounded-motion-ten-slices.md
- docs/review/phase4/street-corner-approved-concept.png
- docs/review/phase4/street-corner-midpoint-concept.png
- docs/handoff/NEXT.md
