---
title: Keep directional leg silhouettes consistent with the preferred baggy trousers
author: Daniel
date: 2026-11-16
branch: intent/receipt-contract-reconciliation-20261115
id: l-a09af972
scope: repo
status: active
src: agent
touches:
  - FACTS.md
---

## Decided
Owner corrected the north/south comparison on November16 at03:41:04UTC: the legs are inconsistent and the baggy look is preferred. Match new south and other facing proposals to the baggier trouser silhouette instead of slimming north to the historical south. This retains the requested grounded character without treating an older source shape as permanently binding.
## Tried and ruled out
A per-part uniform scaling pass aimed at old south dimensions made the north legs slimmer. That is the wrong visual target after this owner correction. Preserve it only as an explicitly superseded attempt.
## Watch out
The preference is for leg silhouette, not blanket approval of the generated bag, coat, material treatment or camera. Original south and approved5/13 remain immutable comparison inputs; native/contact evidence stays tied to its exact source revision.
## In the code
FACTS.md records the correction. Runtime docs/review/player-north-source-20261116/attempts/01-uniform-0.4/ contains the preferred baggy first sample; attempts/02-per-part-uniform/ is historical. New south source work belongs in runtime docs/review/player-baggy-south-source-20261116/ rather than overwriting the original source/variation packets.
