# Benchmark evidence — 2026-11-02

Index of what is on runtime main `49759ab3da23eaa11159085c5b2d4c249acb2cd2`. Specs main is `2e5186a313f2ce1265075bb2697fb79d200793f5`. The runtime pin is `393b06f7c195e6040be74d4d170e4f930d2a8845`. No parent production task is Done. BP-001 remains for the owner to record in `decisions.md`, with the comparison images. The production order in [benchmark-production.md](../../specs/001-single-level-vertical-slice/benchmark-production.md) is unchanged.

`ingestBenchmarkEvents()` on this main is inside `#if DEBUG`. The Release compile of the game still follows `31345cd81ffa9a0b0a665ab4cee6b3556861c5b3`.

## On runtime main

| Evidence | Commit | Where |
|---|---|---|
| Same-art projection pair | `#170` `1a4fd888a86d8f6da0876fdcc41abf79d25c5a72` | `BP001-quiet-street-current`, `BP001-quiet-street-midpoint`, and their records |
| Geometry overlay on that pair | `#171` `31345cd81ffa9a0b0a665ab4cee6b3556861c5b3` | `BP001-quiet-street-current-geometry`, `BP001-quiet-street-midpoint-geometry` |
| Two blocking-solid footprints | `#169` `813cf1c56017` | `docs/review/device-qa/solid-footprint-2026-11-01.md` |
| The other twelve blocking solids | `#172` `a3a709b940789c61d74eeb30eebeb0632734a46b` | `docs/review/device-qa/solid-footprint-twelve-2026-11-02.md` |
| Camera frame bounds | `#173` `d7ba4aa2356d0b0bfb152d24ac9ebb76ac00d8b9` | `docs/review/device-qa/camera-frame-bounds-2026-11-02.md` |
| Enemy sprite bounds | `#174` `d4a8eb9e4e6e2c19f906025c995e4c2932ee67bb` | `docs/review/device-qa/enemy-sprite-bounds-2026-11-02.md` |
| Device-sitting bot column | `#175` `70fb1dd9941a4b76fe71fb071a119f65a84c74b2` | `docs/review/device-qa/retest-checklist.md` |
| Device-sitting probe | `#168` `b1411546cb66` | `Tests/SurveillanceCoreTests/PacingProbe/DeviceSittingQA.swift` |
| Registered square assert; issue `#128` closed | `#176` `a3e571117166de5a873ed2d7b58563b909d5ab84` | `AppTests/BenchmarkCaptureTests.swift` |
| Shipping walk and damage plates | `#177` `7f228ea246b8085ffc2d58d1ad86d60562fab757` | `BP117-walk-solid-01-residential-west`, `BP117-walk-solid-13-phoenix-west`, `BP117-damage-contact`, `BP117-damage-witch-shot`, `BP117-damage-vendor-mine` |
| Placed decoration canvases | `#178` `c700b8242d35bd81d7635f6c938410832af61899` | `docs/review/device-qa/decoration-placement-2026-11-02.md` |
| Tiled ground and fog planes | `#178` `c700b8242d35bd81d7635f6c938410832af61899` | `docs/review/device-qa/tiled-planes-2026-11-02.md` |
| Actor bounds and the shapes already drawn | `#179` `c5730525c041dfbd1f0477c8c03ab76dc5ba67f5` | `docs/review/device-qa/` notes dated 2026-11-03 |
| One-logical-pixel outline bar | `#180` `a4e25e62490a6234b427e0755db67a50722e51ab` | `AppTests/OutlineResolutionTests.swift` |
| Other shapes and player south action frames | `#181` `bf173ec319752588dba144160643859073337100` | `docs/review/device-qa/world-shapes-2026-11-03.md`, `docs/review/device-qa/player-action-frames-2026-11-03.md` |
| Facing frame 01 and the other south state frames | `#182` `1d9754c4faf46573ffbfd5382a0e9046d614c163` | `docs/review/device-qa/player-facing-frame-01-2026-11-03.md`, `docs/review/device-qa/south-state-frame-01-2026-11-03.md` |
| Directions that reuse the south bytes | `#183` `8c37807deb574e5a12cf2385dbec37cf35cc0b6e` | `docs/review/device-qa/player-direction-copies-2026-11-03.md` |
| Directions that do not share a hash, and frame 01 bounds | `#184` `836620922f95c88440ec666bcb8f1b3f2ab2a9b7` | `docs/review/device-qa/direction-distinct-2026-11-03.md`, `docs/review/device-qa/player-action-facing-frame-01-2026-11-03.md`, `docs/review/device-qa/enemy-idle-frame-01-2026-11-03.md`, `docs/review/device-qa/boss-facing-frame-01-2026-11-03.md`, `docs/review/device-qa/elite-facing-frame-01-2026-11-03.md` |
| Copy-lock of the three copied clips | `#185` `aa20931a163ea26e7c37488c162d68e238d4944c` | `AppTests/CopiedDirectionBytesTests.swift` |
| Enemy action frame 01 and the remaining player action frames | `#186` `c603aebec524de631b4b96030cfeef2fb167ca63` | `docs/review/device-qa/enemy-action-facing-frame-01-2026-11-03.md`, `docs/review/device-qa/player-action-rest-frames-2026-11-03.md` |
| Clip lengths and the remaining idle and move frames | `#187` `ff1ba272f931658ab75688484b9d311294844272` | `docs/review/device-qa/clip-lengths-2026-11-03.md`, `docs/review/device-qa/player-idle-rest-frames-2026-11-03.md`, `docs/review/device-qa/player-move-rest-frames-2026-11-03.md`, `docs/review/device-qa/enemy-idle-rest-frames-2026-11-03.md`, `docs/review/device-qa/enemy-south-move-rest-2026-11-03.md`, `docs/review/device-qa/enemy-move-rest-frames-2026-11-03.md` |
| Boss, elite, and hurt-defeat frames after 01 | `#188` `78101b2464c47d4269e0311c1b606b4d691e6b55` | `docs/review/device-qa/boss-south-rest-frames-2026-11-03.md`, `docs/review/device-qa/boss-six-rest-frames-2026-11-03.md`, `docs/review/device-qa/boss-long-rest-frames-2026-11-03.md`, `docs/review/device-qa/elite-south-rest-frames-2026-11-03.md`, `docs/review/device-qa/elite-six-rest-frames-2026-11-03.md`, `docs/review/device-qa/elite-short-rest-frames-2026-11-03.md`, `docs/review/device-qa/enemy-south-hurt-defeat-rest-2026-11-03.md`, `docs/review/device-qa/enemy-hurt-defeat-rest-frames-2026-11-03.md` |
| Index rows for the eight later-frame notes | `#189` `df637da86c782f9a83b8105374b3516fd06aba5c` | `docs/review/device-qa/README.md` |
| Anticipate and commit frames after 01 | `#190` `9d4656c5b72851c10e449f4e6cbd27c1c6d4b2a6` | `docs/review/device-qa/` notes dated 2026-11-03 for the rest frames |
| Captain housing frames | `#191` `279dc63ebd0cf92e1eea8dda22987ac6285135df` | `docs/review/device-qa/captain-housing-bounds-2026-11-03.md` |
| Copied player filename rows and the six shell images | `#192` `92c500fea6be258e6e2668d1e4b028d073df9c98` | `docs/review/device-qa/player-copied-direction-rows-2026-11-03.md`, `docs/review/device-qa/shell-image-bounds-2026-11-03.md` |
| Shipped audio file bytes | `#193` `241c167982b571e942bf17234c90d1a163f8b749` | `docs/review/device-qa/audio-file-bytes-2026-11-03.md` |
| Catalog digests against shipped PNG bytes | `#194` `dc1fdc48c0128acabb8e984eb4f78911e26c2622` | `docs/review/device-qa/catalog-png-digests-2026-11-03.md` |
| Draw order and the cue projection | `#195` `914a5c0146c15bcb18d0b550660a452e7c93c33c` | `docs/review/device-qa/world-layer-order-2026-11-03.md` and the cue notes dated 2026-11-03 |
| README row for the catalog digest note | `#196` `3e32d76475c5979d0b8d23e2f5da0a70e54a5c2c` | `docs/review/device-qa/README.md` |
| Camera follow, exposure bands, medals, and upgrades | `#197` `49759ab3da23eaa11159085c5b2d4c249acb2cd2` | `docs/review/device-qa/camera-follow-2026-11-03.md`, `docs/review/device-qa/exposure-bands-2026-11-03.md`, `docs/review/device-qa/medal-predicates-2026-11-03.md`, `docs/review/device-qa/upgrade-effects-2026-11-03.md` |
| Lethal warning, T1058 | `#165` `15b1c94cb117` | presentation only; gameplay digest unchanged |
| Shell copy, T1059 | `#166` `aed7bff793f1` | `START`, `SETTINGS`, `RESTART` |

Shipping mapping remains `(x, -y)`. On the midpoint plate, world-south still reads down-right. The recommendation is to keep the shipping mapping. That recommendation is not a record in `decisions.md`.

Camera frames are 64×96. The renderer anchors both the head and the housing at catalog `(32, 88)`, which is SpriteKit `(0.5, 8/96)`. The housing is not centered. Separated pieces remain in operational frames 02 and 03 and in several destroy frames. Device issue `#117` was closed by the owner on 2026-11-02.

The five standard enemies are canvas 64×64 with clip anchor `(32, 56)`. Body radii from `combat-content-009` stay fog 18, cable car 20, witch 18, informant 16, vendor 22.

The bot column is the UTC 2026-11-02 device-sitting seed `9972847794717746389`, salt 0, Ricochet Pulse. Mine counts on the four pinned rows are 66, 12, 0, and 6. None is SURGICAL. The human checklist rows are unchanged, including the line that Vendor mines are about 9% of damage.

Issue `#128` keeps the 190×217 control at anchor `(0.5, 0)` and asserts the registered square of the 1254 source at anchor `(653, 1152)`. The simulation digest assert was already present. Collision is unchanged. Closing `#128` leaves projection acceptance open.

## Open

- The shipping walk and damage plates are on main as `#177` `7f228ea`. Device issue `#117` was closed by the owner on 2026-11-02. The phone retest and the comprehension note remain human.
- T1060 stays open. Main paints a filled Vendor mine disc. Runtime `#167` is unmerged. Specs `#92` stays held: the hostile colour remains the proposal, and the 1-unit keyline has to get thicker before it meets the half-scale stucco requirement.
- Specs `#93` records the T1058 and T1059 checkboxes and leaves T1060 open.
- The phone retest and one comprehension note are human. Install `49759ab`. T903, T904, and T905 stay unrun. Medal numbers stay.
- T1042–T1046 stay open. Enemy sheets wait on the recorded BP-001 choice and an explicit go-ahead.
- Specs `#63` and run-shell § 8.1 stay open.

The phone sitting names whatever runtime main is installed. `7f228ea` adds a debug-only ingest. The Release compile of the game still follows `31345cd`.
