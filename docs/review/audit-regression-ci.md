# Specification audit regression CI coverage

Tracking: SS-specs #112. Follows the reconciliation in #111.

## Change

The existing `validate` job now runs
`python3 -B scripts/test_spec_consistency.py` before canonical validation.
The workflow still runs on every pull request and push to `main`.
No job, trigger, existing validation command, dependency, contract, or product
requirement is removed or weakened.

## Verification

- Before the change, a parsed-workflow assertion failed because the regression
  script was absent. After the change, it finds exactly one new guard step.
- Removing that step from the parsed new workflow reproduces the parsed baseline
  exactly, including all existing jobs, commands, and triggers.
- All five specification consistency regressions pass locally.
- Canonical specification validation passes locally.
- GitHub execution of the new step must pass before this change is considered
  CI-validated. Local workflow inspection is not remote execution evidence.

These are targeted prose/inventory regressions. They do not close playtest,
physical-device, production-art, or owner-decision gates.
