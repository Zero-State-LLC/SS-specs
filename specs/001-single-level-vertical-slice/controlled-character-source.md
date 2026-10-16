# Controlled character source pilot — BP-002/BP-008

Status: production-method pilot; no artwork or new runtime admitted. Scope remains D-104 / T1045.

## Evidence motivating the pilot

Runtime 987c32a captured the existing three-frame hurt response with the real renderer: event timing passed, but silhouette and facing readability did not. Runtime 4cc9a62 records a higher-detail generated replacement study: costume coherence improved, but manually annotated boot landmarks drifted up to 5.60 pixels at 384px export (about 0.93 logical units). These approximate annotations are diagnostic, not a numerical acceptance threshold. Repeated independent image generation has not supplied the editable source master already required by BP-002.

## Research and choice

DOCUMENTED: Spine's [weights](https://esotericsoftware.com/spine-weights) bind image-mesh vertices to bones; [IK constraints](https://esotericsoftware.com/spine-ik-constraints) control limb endpoints and expose stretch behavior. Its [export guide](https://esotericsoftware.com/spine-export#PNG) supports transparent PNG sequences and omission of a duplicate closing frame. These mechanisms permit offline source animation without adopting a skeletal runtime.

DOCUMENTED: Blender's [IK constraint](https://docs.blender.org/manual/en/5.0/animation/constraints/tracking/ik_solver.html) controls a bone chain using a target and exposes chain length and stretch. The versioned official page was retrieved through search on 2026-10-14; current manual/API direct fetches failed. Confirm properties in the installed 5.2 API before use. Local Blender 5.2.0 LTS build fbe6228777e7 was observed on 2026-10-14.

PROPOSED implementation pilot: use a single editable 3D body/rig as a source for exported sprites. This is selected for a bounded experiment because one source can be viewed from distinct directions and can expose measurable limb/contact constraints. It does not prove a superior aesthetic. A layered painted rig remains an alternative if it better preserves the benchmark; it must author hidden surfaces and facings explicitly. Neither workflow may stretch one side-facing bitmap and call it a different view. No new runtime engine, dependency, physics or player mechanic is authorized by this pilot.

## Pilot sequence and evidence

1. Create a small editable rig with pelvis, torso, head, paired thighs/shins, separate foot targets and explicit joint names. Keep targets independent of the moving pelvis. Disable automatic limb stretch for this anatomical continuity experiment. Save the project and generation recipe, tool version, source hash and coordinate convention.
2. Block a restrained three-key hurt response using one rig. Measure evaluated thigh/shin lengths and ankle-target residual at each key and intermediate sample. Solver correctness is technical evidence only; no benchmark acceptance follows from zero residual. Record values without inventing a visual slip threshold. Include target reachability and joint direction review.
3. Produce a hooded body/costume master matching the selected reference, preserving strap/patch side, hands, boots and hood volume. Validate skin deformation and garment intersections. A stick rig, mannequin or plain low-poly proxy does not meet the art target. Pose/mesh controls must remain editable; a raster embedded in a project is insufficient.
4. Render four neutral facings with one saved camera, scale, illumination and consistent ground root. Record the actual world-to-view mapping and compare against the shared renderer scene; no exact angle is assumed from the concept. Hidden sides need authored geometry/materials. Do not mirror asymmetric equipment.
5. Follow BP-002's south movement-cycle gate, BP-008 world-travel contact checks and the event-facing hurt-to-live-state comparison before expanding other facings. A planted source foot during a stationary hurt does not prove no sliding while the runtime actor travels. Record that distinction explicitly.
6. Export only reviewed poses with fixed canvas/anchor and BP-007 resolution records. Retain exact durations and do not include a redundant closing pose as a distinct frame. Admit a complete family through BP-006 after visual and runtime gates; the source prototype does not switch active metadata.

## Stop conditions and comparison

Reject the pilot as a production solution if it cannot preserve the selected urban hooded character's material treatment, silhouette, distinct elevated facings, foot contact and cloth/hand readability at native size. Correct the master or compare the layered painted alternative; do not lower the benchmark to match a convenient rig. Camera and environment source work remain required and are not replaced by this character experiment.

The existing animation timing, controller speed, damage authority, v1 active delivery, gameplay identities and physical-device review gate remain unchanged. All full-source, art, world-travel, encounter and device acceptance remains open.

## Layered painted source: setup-pose prerequisite

DOCUMENTED: Spine's [image preparation](https://esotericsoftware.com/spine-images) uses separate images for independently moving parts and preserves placement through layered imports. Its [mesh guide](https://esotericsoftware.com/spine-meshes) describes image polygons, deformation and weighted bones. These are authoring mechanisms, not evidence that a particular cut or generated replacement preserves the benchmark.

OBSERVED (2026-10-14): the south layered study reconstructed the original composite exactly, yet its rough thigh masks included coat pixels. A generated replacement leg aligned at two manually marked points but had a narrower silhouette, different boot proportions and incompatible texture. It is rejected. Exact reconstruction and landmark residuals alone therefore cannot admit this source.

For the already-authorized layered alternative, complete these source checks before the first movement cycle:

- Preserve the approved neutral image as the comparison baseline. Record anatomical side, canvas, root and source hashes. Review each isolated part and the assembly; a mask must not assign coat, straps or equipment to a limb merely because those pixels lie inside a rectangle or polygon.
- Separate visible-pixel extraction from authored hidden surfaces. Save the original masks and each underpaint separately. Keep the costume's visible contour and material treatment in the assembled neutral unless an explicit reviewed revision replaces it. Do not use nonuniform registration to conceal a mismatched replacement limb.
- Establish joints from the retained source and record manual annotations as approximate. Compare the whole limb contour, knee placement, boot width and sole, not just two fitted points. Numerical fitting does not establish anatomy or visual acceptance.
- Author overlap behind shoulders, elbows, hips and knees; separate boots and coat controls where they must move independently. Exercise the intended pose range with the layers visible individually and assembled. Reject exposed cut gaps, detached joints, coat tearing and equipment attached to the wrong moving part. A static neutral reconstruction does not satisfy this check.
- Save editable controls and the source project. Only after setup-pose and joint-range review proceed to the existing south 16-frame cycle and runtime world-travel checks. Retain the four-facing, exact-duration, complete-family and device gates already specified; this clarification does not replace them.

These checks implement BP-002's existing editable-source requirement. They introduce no gameplay behavior, automatic silhouette threshold, new production dependency or runtime skeletal system.

## Elevated motion: depth and contact prerequisite

DOCUMENTED (2026-10-14): Spine's [mix-and-match example](https://esotericsoftware.com/spine-examples-mix-and-match) uses weighted meshes and depth controls, separately authored hidden surfaces, and dedicated garment controls. Its [directional-animation guidance](https://esotericsoftware.com/forum/d/25378-animating-different-directions) points to a multi-direction source using shared bones. Its [IK guide](https://esotericsoftware.com/spine-ik-constraints) describes endpoint constraints and explicit stretch/compress settings and limitations. These support candidate authoring mechanisms; they do not prescribe SS camera elevation, gait, timing, contact intervals or acceptable deformation.

OBSERVED: runtime review source `435b984` supplies eighteen raster layers and eight linked 2D joint controls. Its neutral preservation and rigid-chain checks pass, but it cannot yet show an elevated limb moving toward/away from the view or hold a planted sole against world travel. This scaffold is not a south movement cycle.

Clarification of BP-002/BP-008: record the coordinate space of every length and contact measurement. Source/anatomical segment length and projected screen length are different quantities. A projected segment can shorten as its orientation changes relative to the view; constant 2D image-space length neither proves nor defines correct elevated motion. If the layered source has no underlying 3D geometry, label its pivot/length values as 2D annotations and do not report anatomical length preservation. Preserve costume proportions through reviewed source keys and deformation, not a screen-length assertion alone.

Before in-betweening the south cycle, compare its contact/support/passing/extension keys with visible depth treatment: limb overlap/draw order, knee and boot perspective, hood volume and garment attachment. Use an authored mesh/depth treatment or explicit attachment variants where rigid cutout rotation fails. The prohibition on stretching a mismatched replacement into registration remains; it does not prohibit intentionally authored perspective deformation that is documented and visually reviewed. No particular mesh topology, projection angle, numerical deformation tolerance or new software dependency is selected here.

Boot controls must distinguish an annotated visible sole point from an authored heel/toe contact model. Hidden heel/toe positions are NOT_COMPUTABLE from the neutral silhouette alone. Author the missing surfaces/landmarks in the source, identify their status, and review their contact phases before claiming heel/toe drift measurements. Keep contact targets independent of the moving body where constraints require it. A successful source-space IK solve does not establish BP-008 world-space contact; retain the actual simulation-travel comparison and its unchanged speed/cadence.
