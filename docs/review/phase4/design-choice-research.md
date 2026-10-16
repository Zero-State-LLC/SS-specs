# D-104 design research and benchmark translation

2026-10-14. This record separates **user direction**, **documented craft or place reference**, **current runtime fact**, and **unproven design proposal**. Research can justify a method and constrain a choice; it cannot prove that a particular costume, angle or animation feels right in SS. Those require a game-scale review.

## Benchmark and actual display

**User direction:** The [selected corner image](street-corner-approved-concept.png) is the visual benchmark. The desired playable viewpoint is somewhere between it and the more overhead trial. Keep the hooded player and an urban street-theater cast. The game is not a side scroller. The release has one level and one visible municipal Camera family.

**Runtime facts:** `GameScene.didMove` sets an aspect-fit scene to `PresentationCamera.visibleWidth/visibleHeight`; `ArenaReachability.viewportMatchesContract` requires 704×326 world units. `WorldRenderer.renderActors` draws the player in a 64×64 box; `renderCameras` currently composes a 64×96 housing and a second 64×96 head. The selected image is 1672×941 (about 1.78:1) while the world view is about 2.16:1. The image's exact framing and painted microdetail therefore do not transfer automatically to landscape gameplay. No production frame yet demonstrates equivalent visual quality at that size.

**Research:** Raymond Schlitter's [top-down sprite guide](https://www.slynyrd.com/blog/2019/10/21/pixelblog-22-top-down-character-sprites) ties sprite, tile and screen size together and recommends testing the native display. His [animation study](https://www.slynyrd.com/blog/2025/3/24/pixelblog-55-top-down-character-animation) describes a three-quarter top-down projection, checks anatomy through a rotation test, and simplifies detail when it obscures motion. These are production methods, not a warrant to copy his proportions or six-frame cycle.

**Decision to test:** Recompose the corner into the actual 704×326 viewport with playable margins and HUD, rather than cropping the concept mechanically. Make one player neutral in all four facings, one south movement loop, one complete municipal Camera state set, one solid corner and one upright prop. Draw their authoritative ground anchors/footprints from runtime data. Capture native-size, grayscale and 50% views, plus a short movement/occlusion recording. The first review asks whether the hood, device, feet, Camera state, field and routes can be understood without zooming. If the 64×64 actor cannot meet that bar, compare a revised authoring/draw mapping in the same viewport before changing the contract. More source pixels alone are not evidence.

## Viewpoint and world language

**Research:** The top-down animation study explicitly shows upper surfaces and fronts in a three-quarter view, then uses a rotation line-up to catch inconsistent anatomy. The sprite guide warns that vertical overlap can convey depth but arbitrary horizontal overlap confuses it. San Francisco Planning's [architectural periods and styles bulletin](https://default.sfplanning.org/Preservation/bulletins/HistPres_Bulletin_18.PDF) documents asymmetrical Victorian façades, bracketed cornices and varied commercial forms; [SF Public Works' Better Market Street](https://sfpublicworks.org/bettermarketstreet) documents streetcar, curb, signal and streetscape infrastructure. These are references for material and structure, not a claim that SS depicts an exact real intersection.

**Design proposal:** Use the selected image's weathered stone, civic curb, rail edge and warm doorway as a compact value hierarchy. Use an elevated three-quarter projection whose roof, hood crown, newsbox top and Camera dome agree. The exact angle remains open. The midpoint image is a useful candidate, not a locked numerical camera angle. A single corner art proof must compare it against the selected image at runtime aspect ratio and reject any facing that becomes a side-profile cutout.

**Approval test:** Ground seams and object bases share one plane; a player crossing behind/in front of the building and prop neither disappears without a marker nor passes through a depicted barrier. Keep the central play lane and hazard field legible in a dense encounter. If the corner is beautiful but reads as a still illustration only, it fails the benchmark as a *game*.

## Character design and motion

**Research:** The animation study builds a simple common body before costume detail, compares every facing around a rotation, and notes that asymmetric equipment may need unique directional frames rather than mirroring. It also uses variable holds to avoid mechanical motion; its six-frame example shows why frame count by itself does not establish fidelity. The earlier sprite guide starts with distinct facing neutrals and tests motion before detailing.

**User direction:** Keep the hooded player and 16 distinct chronological frames for each applicable movement facing. The prior side-only and duplicate-frame sheets are rejected.

**Design proposals pending proof:** Weathered jacket, strap and Civic Pulse placement are a coherent candidate for the player. The role silhouettes in `visual-reference.md` are candidate ways to express the existing combat roles, **not researched facts about what each character must wear**. For each role, pair a one-line gameplay function from its contract with two rough silhouette alternatives. Compare N/E/S/W neutrals and the attack anticipation at actual phone scale, in grayscale, against the player and other enemies. Choose the shape that communicates identity and attack without relying on tiny trim, extra limbs or fantasy cues. Only then make controlled key poses, in-betweens and secondary cloth/equipment motion. Review stride distance, foot lock and loop seam in motion before completing all 64 movement frames for a walking actor. Stationary roles follow their real state contract.

## Camera and threat readability

**Runtime fact:** Standard Cameras presently render a separate housing and head, explaining the visible stacking defect; `renderCameras` uses a 64×96 box for each. This is a renderer issue to fix after the art proof. The one-family visual direction does not change seeded housing-family logic or fairness.

**User direction:** For the one release level, use one appropriately styled municipal Camera; each Camera needs its own complete registered sheet. The full device must remain recognizable and its states distinct.

**Design proposal pending proof:** The selected image's pole and dome suit the civic street corner, but no city reference establishes that exact fictional mount. Compare the complete municipal design to the existing candidates in the same scene, then choose using these SS-specific criteria: believable base/mount, single silhouette, visible aiming/field origin, Integrity-state change, no false extra lens, and distinction from boss-owned indestructible emitters. A persistent boss marker is a proposal until a no-color encounter review shows it cannot be mistaken for a three-hit Camera. Apple's [Differentiate Without Color Alone evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/differentiate-without-color-alone-evaluation-criteria) support shape or icon alongside color and a grayscale check; they do not prescribe SS's exact glyph.

## Production gate and decision ownership

1. Preserve the selected image and user direction as the **art benchmark**, with the midpoint only a projection candidate.
2. Produce a controlled, editable player turnaround and one south 16-frame loop. Record actual frame holds and preserve authoritative movement timing. A duplicated frame or disconnected cloth fragment is a defect.
3. Produce one complete municipal device state sheet and the representative corner/building/prop in the **same** projection and world scale. Register anchors and state/clip IDs; keep concept crops out of the runtime bundle.
4. Render these in the actual 704×326 scene with HUD, field, one enemy and a dense encounter sample. Capture native-scale stills, grayscale, 50% scale, frame-step and a normal-speed video; overlay authoritative bases and contacts separately.
5. Review fidelity and comprehension together. If detail is lost, revise silhouette/value grouping or canvas mapping, then measure atlas/memory/frame time on the required physical floor before broad asset production. Do not set a numeric budget or claim device pass from a concept.
6. Admit only accepted sources through the asset catalog and provenance chain. Then migrate clips/manifest, remove the stacked Camera composition and run renderer/replay/device QA. D-020 and D-021 remain explicit pending decisions.

This gate answers *how* to approach the benchmark without presenting aesthetic guesses as established research. The art direction is selected; the production translation is not yet verified.
