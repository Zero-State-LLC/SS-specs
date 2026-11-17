# Intent

**Author:** Jcode, on behalf of the QA continuation request

**Date:** 2026-11-15

**Status:** accepted

**Acceptance:** Owner explicitly accepted the versioned-receipt direction and authorized execution on 2026-11-15 at 23:18 UTC.
**Next stage:** `spec.md`

## Problem

**OBSERVED:** a successful run archived by SS-runtime `df8473713a3d37aeca05d4e1110f979f197b9ceb` fails the exact bundled `run-receipt-001` schema in three places. Runtime defect #233 and evidence PR #234 retain the actual JSON and independent failing validator. Existing receipt unit suites pass without establishing schema compatibility.

**OBSERVED:** the disagreement is inside the pinned specification as well as between schema and runtime. At SS-specs `b1ed874e1e8eb0e61b2174b9093201e9a61e1a4b`:

- `camera-destruction.md` §16 requires root `camerasDamaged`, `camerasDestroyed`, `tamperExposureApplied` and `cameraObjective`. The receipt schema does not declare these properties and forbids additional root properties.
- `encounter-objectives.md` §6 documents `objectives.extractionArmed`; the schema instead requires `objectives.extraction` without defining its shape.
- `upgrades.md` Selection requires the selected upgrade to be recorded by ID and contract version. The schema permits an object or null without defining the object, while runtime emits a string or null.

An archive that cannot be validated undermines the existing diagnostic evidence contract. Changing tests to match the serializer, deleting documented evidence, or broadly relaxing the schema would conceal the disagreement rather than resolve it.

## Proposed outcome

**PROPOSED:** one explicitly accepted receipt contract defines the complete serialized evidence shape and agrees with Camera, objective and upgrade requirements. A real successful, failed or serializable invalid run validates against the contract it declares. A receipt without a selected upgrade remains representable. Selected upgrade evidence identifies both the upgrade and its contract version.

**PROPOSED:** preserve the documented Camera summary evidence and the `extractionArmed` objective meaning. Do not introduce a second Extraction condition or make Camera destruction gate Extraction. Define a narrowly specified upgrade object rather than permitting arbitrary data or discarding contract-version evidence.

**PROPOSED:** prefer a separately versioned receipt successor, with explicit adoption and historical-read policy, over silently changing the meaning of archived `run-receipt-001` data. Preserve original archived bytes and their declared identities. Old invalid receipts remain historical evidence, not retroactively certified conformant data.

**PROPOSED:** acceptance requires schema validation of actual runtime serialization across representative terminal outcomes and upgrade paths, in addition to existing field-level assertions. Invalid shapes, unknown identities and missing required evidence must be rejected by validation. No existing test or assertion is weakened to make a red check green.

## Affected users/systems

- Players and local diagnostic reviewers rely on truthful complete-run evidence.
- Canonical receipt, Camera, encounter-objective and upgrade contracts must agree.
- Runtime serialization, receipt archiving/reading, bundled contract identity and contract-parity evidence may need coordinated adoption after specification acceptance.
- Existing replay and golden-state evidence must show that receipt-only work does not alter gameplay.

## Constraints/non-goals

- This accepted intent authorizes specification and implementation of the versioned diagnostic contract. It does not itself adopt a schema, mark the defect fixed, authorize merging PRs or close acceptance gates.
- Preserve Constitution Articles III, IV and VII and the one-level scope. No gameplay, simulation ordering, upgrade effects, Camera rules, Extraction predicate, ruleset/content/arena or replay digest change is intended.
- Preserve canonical ordering, atomic archive writes and the existing 50-receipt retention contract. Do not rewrite or delete historical receipts as a migration shortcut.
- No networking, analytics upload, new dependencies or generalized schema framework is proposed by this intent.
- Existing terminal-card and Share behavior are not redefined by diagnostic receipt fields.
- This work does not close physical-device, art, playtest or expansion acceptance gates.

## Open questions

1. Does the owner accept preserving the Camera summaries and `extractionArmed`, while making selected upgrade ID plus contract version explicit?
2. Is a separately versioned receipt successor required, or does the owner classify this as a correction to the existing contract? Either route needs an explicit compatibility decision, not an opportunistic allowance for the current output.
3. Which historical receipt identities/shapes remain readable, and how is nonconformance reported without modifying their bytes? Do not assume existing archive readers validate schemas.
4. Which exact field names, nested constraints and representative outcome matrix should the subsequent specification lock? This draft does not assign new requirement IDs or declare a migration complete.

## Verified claims

- **OBSERVED:** runtime #233 reproduction reports forbidden root summary fields, missing `objectives.extraction`, and a string upgrade rejected by object/null type. Evidence is in runtime PR #234, `docs/review/qa-2026-11-15/`.
- **OBSERVED:** pinned `camera-destruction.md:331-354`, `encounter-objectives.md:92-117` and `upgrades.md:16` contain the requirements above. The relevant schema, objective and upgrade artifacts are unchanged between the runtime pin and checked specs main `983a4ca3427bd8a9d30056bccf356fe0f715312e`.
- **OBSERVED:** `contracts/versions.json` registers `runReceipt` as `run-receipt-001` and upgrades as `upgrades-003`.
- **OBSERVED:** `SS-runtime/Sources/SurveillanceCore/Acceptance/ReceiptArchive.swift` checks serialization availability and digest-prefix length when writing, not whole-receipt JSON-schema conformance. Its read path reads stored JSON text rather than certifying schema validity.

## Assumed claims

- **INFERRED:** a versioned diagnostic-envelope repair can preserve gameplay state digests. This must be demonstrated after acceptance, not assumed from the intent.
- **NOT_COMPUTABLE:** compatibility with consumers outside the inspected local archive and runtime tests. Inventory them before adopting a migration or claiming that none exist.
