# Intent

**Author:** Grok Bot (follow-up to D-121)
**Date:** 2026-11-02
**Status:** accepted
**Next stage:** `visual-assets.md` § Vendor mine (D-122)

Directed by the owner on 2026-11-01 in chat ("Fix it"), as the follow-up to D-121 (SS-specs #91). Acceptance of the specified result is the owner's yes on the pull request that adds this file. The next stage is specify.

## Problem

D-121 made the Vendor mine a ring, but four parts of it work against the read.

- **OBSERVED:** D-121 specifies one light neutral stroke, white 0.92 at alpha 0.95. In SS-runtime `App/WorldRenderer.swift`, that is exactly `Palette.unawareMarker` (line 1574), and `Palette.playerFill` is white 0.92 (line 1557). `visual-assets.md` § 3 gives the Player a warm ivory grounding ring and puts Enemy attack in magenta/red. A white hazard ring reads as Player kit or as the unaware marker.
- **OBSERVED:** D-121 carries arming against armed by line weight alone (2 against 4).
- **OBSERVED:** D-121 gives no units and centres the stroke on the radius, so half of the armed stroke draws outside the 42 hazard edge.
- **OBSERVED:** damage applies when the Player's centre is within the mine radius (SS-runtime `Simulation.swift:893`), and the Player's collision radius is 18 (`player-controller.md`). D-121 does not say which edge the ring marks.
- **OBSERVED:** D-121 states the ring "reads" at native scale, half scale and in grayscale. No plate records that.

## Proposed outcome

1. The ring uses the runtime's orange-red telegraph-outline colour (`Palette.telegraphStroke`, line 1582), with a dark outer keyline. It never uses neutral white, and it is told apart from the HUD Hunted state by shape, keyline, and location, not hue.
2. Arming and armed differ by more than weight: a low-alpha hostile fill when armed, and a 30-tick arc that sweeps closed while arming. Under Reduced Motion the arming ring is static.
3. Widths are in world units and every stroke is inside the radius, so nothing draws past 42.
4. The specification says that damage triggers on the Player's centre, so the body visibly crosses the ring first.
5. Contrast is a requirement: at least 3:1 non-text contrast (WCAG 2.2 1.4.11) on asphalt and stucco, at native and half scale and in grayscale, verified by review plates in T1060.
6. A short Unity note on units and stroke alignment.

## Affected users/systems

The player (reading the hazard), `visual-assets.md`, `decisions.md` (D-122), `enemies-and-encounters.md`, `hud-tutorial.md`, `tasks.md` (T1060), and the SS-runtime mine renderer. SS-runtime #167 implements the superseded D-121 white ring; after this lands it must be rebased onto SS-runtime main and updated to D-122. No simulation, collision, ruleset, content, arena, or replay identity changes.

## Constraints/non-goals

- Arm 30, life 240, radius 42, damage 12, the cap of two, and which mine retires are unchanged.
- No caption, no asset id, no catalog row. Not the lethal-warning card.
- Player art, camera and framing, and the hooded street-theater style are unchanged. The Player keeps its warm ivory grounding ring.
- One level only. No new enemy, hazard, or system.

## Open questions

- **OBSERVED (arithmetic, recomputed 2026-11-02):** the runtime's telegraph-outline colour (0.95, 0.55, 0.35) is orange-red, HSV hue 20°, not the magenta/red Enemy attack row of § 3. The tracked concern that it sits too near the amber Tracked family is unfounded: CIEDE2000 27.45 with typical colour vision, 8.2 under simulated deuteranopia, 13.9 under protanopia (Machado 2009, severity 1.0). The real near-match is the HUD Hunted colour (0.93, 0.58, 0.30): 6.4 typical, 2.0 deuteranopia, 3.5 protanopia. `visual-assets.md` therefore requires the ring to be told apart from Hunted by shape, keyline, and location, not hue, and T1060 adds a colour-blind plate beside Hunted and Tracked. That read is NOT_COMPUTABLE until the plates exist. The owner may still prefer a value inside the magenta/red row.
- The dark keyline value. The runtime's darkest neutral now is `Palette.barrierRail` (white 0.10 at alpha 0.95). The specification asks for a dark neutral, and T1060 picks the value against the contrast requirement.

## Verified claims

- The runtime values and line numbers above are in SS-runtime `main` at `1c100b2`.
- `PresentationSnapshot.MineSprite` already carries `armRemaining`, so the arming arc needs no new simulation data.

## Assumed claims

- **INFERRED (arithmetic only, not a plate):** with the telegraph-outline colour at alpha 0.9 and a white 0.10 keyline at alpha 0.95, the WCAG relative-luminance formula gives about 4.0:1 for the stroke on asphalt `#343D43`, about 1.1:1 for the stroke on stucco `#A79C8B`, about 6.0:1 for the keyline on stucco, and about 5.65–6.0:1 for the stroke against the keyline across asphalt, stucco and limestone (recomputed 2026-11-02 with the stroke composited over the keyline, the conservative case; with each band composited on bare ground it is 6.2–6.7:1). On that arithmetic the stroke carries the edge on asphalt and the keyline carries it on stucco. Only the T1060 plates count as evidence.
- The keyline and the arming arc are enough to stop a first-time player missing the mine. That needs the device feedback loop, not this file.
