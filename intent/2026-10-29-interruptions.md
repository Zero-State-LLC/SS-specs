# Intent — interruptions pause the run

**Author:** Claude (audit follow-up)
**Date:** 2026-10-29
**Status:** accepted
**Next stage:** `specs/001-single-level-vertical-slice/run-shell.md`

Accepted by the user on 2026-10-29 in chat, in response to an audit that recommended this change: "ok so whats next ? start on next items and pr when done , and keep going". Merging the pull request that carries this intent is the owner's binding acceptance.

## Problem

**OBSERVED (runtime `5b36566`):** the app shell does not respond to the app leaving the foreground or to an audio-session interruption. `App/` has no `scenePhase`, resign-active, or `AVAudioSession.interruptionNotification` handling.

PC-008 already guarantees that suspension adds no ticks. But nothing specifies what the player sees on return. After a phone call, Control Center or an app switch, SpriteKit resumes the scene and the run continues in live combat with no Pause surface. On a phone that is the most common way to lose a run unfairly.

**OBSERVED:** Reduced Motion is a Settings toggle that starts `false` on first launch. It does not follow the iOS Reduce Motion accessibility setting, so a player who already asked iOS for less motion gets full shake and hit-stop until they find the toggle.

## Proposed outcome

- A run in progress that loses the foreground comes back paused, on the existing Pause surface. It resumes only when the player resumes it.
- An audio interruption silences the game's audio. Audio comes back without the player re-entering Settings.
- On first launch, Reduced Motion takes its value from the iOS Reduce Motion setting. Once the player changes it in Settings, their choice wins.

## Affected users/systems

Players on phones (calls, notifications, Control Center, app switching) and players who use iOS Reduce Motion. Affects `run-shell.md`, `decisions.md` and the runtime app shell. No simulation, content, arena or replay change.

## Constraints/non-goals

- Presentation only. No simulation tick, digest or receipt change. PC-008, PC-009 and B-004 continue to hold.
- No save/resume of a run across app termination. That is a separate decision.
- No new Pause controls. The existing surface is reused as is.
- One level and existing scope.

## Open questions

- Should the game also honour iOS "Dim Flashing Lights" for Reduced Flash? This intent does not decide it.

## Verified claims

- The `App/` sources at runtime `5b36566` contain no lifecycle or interruption handling (searched for `scenePhase`, `willResignActive`, `interruptionNotification`, `isReduceMotionEnabled`).
- Pause today is the Settings sheet raised from the HUD Pause control (`GameContainerView`), and it pauses the scene (PC-008).

## Assumed claims

- iOS delivers `scenePhase` `.inactive` before `.background` for calls, Control Center and app switches. Assumed until confirmed on a device.
