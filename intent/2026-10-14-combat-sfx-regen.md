# Intent

**Author:** Errnerner Shernerner (prepared by Grok Bot)  
**Date:** 2026-10-14  
**Status:** draft  
**Next stage:** `spec.md`

## Problem

Two admitted audio cues are bright and harsh against the brief for this slice. `sfx_camera_scan_sweep.m4a` (shared by `camera_hit_02` and `boss_telegraph_temporaryOrder`) carries about 72% of its energy above 4 kHz and under 2% in its 400 to 1000 Hz target band. `sfx_suspicion_tier_up.m4a` (`exposure_state_up`) carries about 94% above 4 kHz and under 1% in 400 to 900 Hz. Both are AAC derivations of legacy CAFs frozen at `scrimshawlife-ctrl/Surveillance-Survivor@3b20d88`. Replacing them needs a decision, because the legacy-admission rules only cover frozen legacy binaries and sibling-product cues (D-077), not newly generated originals.

## Proposed outcome

- A decision records whether newly generated ElevenLabs Sound Effects masters may replace admitted legacy cues, and under what provenance and status.
- If accepted, `asset-catalog-001` entries `camera_hit_02`, `boss_telegraph_temporaryOrder` and `exposure_state_up` point at the new source with its SHA-256, and the runtime delivers matching AAC files.
- The other targeted cues (`weapon_civic_pulse`, `camera_hit_01`, `impact_enemy`, `camera_destroy`, `player_damage`) stay unchanged; no candidate passed.

## Affected users/systems

- Player: camera hit, Temporary Order boss telegraph and Exposure up cues sound darker and more midrange.
- Specification: `contracts/asset-catalog-001.json`, `decisions.md`, possibly `legacy-admission.md`.
- Runtime: `Sources/SurveillanceCore/Resources/RuntimeAssets/` two `.m4a` files and the bundled catalog copy, then the pin.

## Constraints/non-goals

- One level only. No new cue IDs, priorities, coalescence or captions.
- Do not copy more legacy files. The new masters are not legacy.
- No per-cue gain exists in this runtime; mix is `master * effects`. The planned legacy `audio_events.json` gain changes do not apply.
- `sfx_camera_scan_sweep` is shared with `boss_telegraph_temporaryOrder` (D-075). Changing it changes that telegraph too.

## Open questions

- Provenance and status for new generated originals: `originalAccepted` / `projectOriginal`, as in D-077, or a new value?
- Should the boss telegraph keep the old sound and get a separate asset ID instead?
- Where do new PCM masters live (runtime `ArtSources/`, or outside both repos)?
- AAC encode: runtime pipeline uses macOS `afconvert -d aac -b 128000`; candidates were checked with ffmpeg AAC 128k only.
- Plan-date licence evidence is still pending for ElevenLabs cues generally.

## Verified claims

- OBSERVED: catalog SHA-256 for the two cues equals the frozen legacy CAF digests (`b156b0016193...`, `2d46ca1776dd...`); current m4a files correlate 0.985 and 0.990 with those CAFs.
- OBSERVED: candidate masters (48 kHz, 16-bit, stereo WAV, true peak -1.1 dBTP):
  - camera scan: sha256 `64d2619c7f6b9dd172851582ef211e7cf9277eb254049de51be22649778467cb`, 0.88 s, -21.6 LUFS integrated, 82.9% in 400 to 1000 Hz, 0.1% above 4 kHz.
  - tier up: sha256 `290e64991be80c6280dcf12759f33077aa5cf15063e887279efbb1990b830bd2`, 0.680 s, -17.7 LUFS, 12% in 400 to 900 Hz, 9.9% above 4 kHz.
  - Encoded to AAC 128k with ffmpeg, both still beat the current m4a on both measures.
- OBSERVED: source was ElevenLabs Sound Effects v2, returned as MP3 44.1 kHz; processing chain was DC and 35 Hz high-pass, 4 kHz low-pass, -6 dB shelf at 3.5 kHz, +4 dB bell at band centre, trim, fades, peak normalize.

## Assumed claims

- Assumed: the darker cues stay readable in combat. Needs a listening check.
- Assumed: the -4 to -6 LU loudness drop versus the current cues is acceptable without a mix change.
