#!/usr/bin/env python3
"""Targeted prose regressions; not a simulation or release-acceptance test.

Run from any directory: python3 -B scripts/test_spec_consistency.py
"""
from pathlib import Path
from copy import deepcopy
import hashlib
import json
import re
import unittest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "specs/001-single-level-vertical-slice"


class SpecConsistencyTests(unittest.TestCase):
    def test_receipt_archive_status_and_decision_references(self):
        migration = (SPEC / "receipt-contract-migration.md").read_text()
        decisions = (SPEC / "decisions.md").read_text()
        tasks = (SPEC / "tasks.md").read_text()
        self.assertIn("Decision: D-123.", migration)
        self.assertIn("## D-123 — versioned diagnostic receipt", decisions)
        self.assertIn("T1061 Adopt the D-123 receipt repair", tasks)
        for status in (".currentUnverified", ".historicalUnverified", ".unrecognized"):
            self.assertIn(status, migration)
            self.assertIn(status, decisions)
        self.assertIn("Reading alone does not certify schema conformance", migration)

    def test_receipt_v2_contract_regressions(self):
        # Synthetic shape coverage, not a claim of runtime serialization evidence.
        schema = json.loads((ROOT / "contracts/run-receipt-002.schema.json").read_text())
        validator = Draft202012Validator(schema)
        receipt = {
            "schemaVersion": "run-receipt-002",
            "identity": {"rulesetVersion": "ss-rules-014", "contentVersion": "civic-seam-content-009",
                         "arenaVersion": "civic-seam-arena-004", "replaySchemaVersion": "runtime-kernel-001"},
            "seed": 1, "outcome": "failure", "elapsedTicks": 1, "finalDigest": "a" * 64,
            "player": {"finalIntegrity": 0, "damageTaken": 100, "integrityRestored": 0},
            "exposure": {"final": 0, "peak": 0, "finalState": "hidden", "lockdownEntered": False},
            "combat": {"damageDealt": 0, "defeatsByArchetype": {}},
            "objectives": {
                "combatAuthority": {"mobEncountersComplete": 0, "mobEncountersRequired": 3, "currentNode": "M-A",
                                    "elite": {"id": "improper-search-daemon", "defeated": False},
                                    "boss": {"id": "algorithmic-moderate", "defeated": False, "phasesReached": []},
                                    "complete": False},
                "networkBlackout": {"camerasDestroyed": 0, "camerasTotal": 8, "complete": False},
                "extractionArmed": False},
            "cameraPlacement": {"version": "camera-placement-001", "placementSeed": 1, "selectedSockets": [
                {"socketId": "socket-01", "cameraEntityId": 18446744073709551615, "housingFamily": "municipalDome"}]},
            "cameraDestructions": [{"cameraId": "18446744073709551615", "tick": 1,
                                    "housingFamily": "municipalDome", "wasDetectingPlayer": False,
                                    "source": "civicPulse", "exposureBefore": 0, "exposureAfter": 0,
                                    "triggeredLockdown": False}],
            "camerasDamaged": 1, "camerasDestroyed": 1, "tamperExposureApplied": 0,
            "cameraObjective": {"destroyed": 1, "total": 8, "complete": False},
            "upgrade": None, "boss": {"phasesReached": [], "defeated": False}, "diagnostics": [],
            "presentation": {"tutorialsEnabled": True, "hudScale": 1000, "handedness": "right",
                             "reducedMotion": False, "reducedFlash": False, "reducedSensory": False}}
        for outcome in ("success", "failure", "invalid"):
            for upgrade in (None, *({"id": item, "contractVersion": "upgrades-003"}
                                   for item in ("signalJammer", "ricochetPulse", "ghostStep"))):
                candidate = deepcopy(receipt)
                candidate.update(outcome=outcome, upgrade=upgrade)
                validator.validate(candidate)

        def objects(value, path=()):
            if isinstance(value, dict):
                yield path, value
                for key, child in value.items():
                    yield from objects(child, path + (key,))
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    yield from objects(child, path + (index,))

        def at(value, path):
            for key in path:
                value = value[key]
            return value

        # Every fixed object's required keys and additional-property boundary.
        for path, value in objects(receipt):
            if path == ("combat", "defeatsByArchetype"):
                continue
            for key in value:
                candidate = deepcopy(receipt)
                del at(candidate, path)[key]
                self.assertFalse(validator.is_valid(candidate), (path, key))
            candidate = deepcopy(receipt)
            at(candidate, path)["unexpected"] = True
            self.assertFalse(validator.is_valid(candidate), path)

        for path, value in [(("schemaVersion",), "run-receipt-001"),
                            (("identity", "rulesetVersion"), "ss-rules-999"),
                            (("seed",), 18446744073709551616),
                            (("finalDigest",), "a" * 64 + "\n"),
                            (("cameraDestructions", 0, "cameraId"), "1\n"),
                            (("objectives", "extractionArmed"), "false"),
                            (("exposure", "finalState"), "unknown"),
                            (("upgrade",), "signalJammer"),
                            (("upgrade",), {"id": "unknown", "contractVersion": "upgrades-003"}),
                            (("upgrade",), {"id": "ghostStep"}),
                            (("upgrade",), {"id": "ghostStep", "contractVersion": "upgrades-003", "extra": 1})]:
            candidate = deepcopy(receipt)
            at(candidate, path[:-1])[path[-1]] = value
            self.assertFalse(validator.is_valid(candidate), path)
        versions = json.loads((ROOT / "contracts/versions.json").read_text())
        self.assertEqual(versions["componentContracts"]["runReceipt"], "run-receipt-002")
        self.assertEqual(hashlib.sha256((ROOT / "contracts/run-receipt-001.schema.json").read_bytes()).hexdigest(),
                         "b163b06de53e56bdc93610ac463eacc9c3af8eca97c51c38187d430b405bb325")

    def test_lockdown_epochs_and_release_timing(self):
        spec = (SPEC / "spec.md").read_text()
        exposure = (SPEC / "exposure.md").read_text()
        order = (SPEC / "simulation-order.md").read_text()
        fr = next(line for line in spec.splitlines() if "**FR-016:**" in line)
        self.assertIn("once per latch epoch", fr)
        self.assertNotIn("exactly once per run", fr)
        self.assertNotIn("nothing but recovery ever lowers", exposure)
        self.assertIn("Before the Court release", exposure)
        self.assertIn("once per latch epoch", order)
        vector = next(line for line in exposure.splitlines() if "| EX-021 |" in line)
        self.assertIn("700/`lockdown`", vector)
        self.assertNotIn("ends at 1000", vector)
        self.assertIn("floor above 700 does not raise it", exposure)

    def test_result_surfaces_remain_separate(self):
        spec = (SPEC / "spec.md").read_text()
        shell = (SPEC / "run-shell.md").read_text()
        acceptance = (SPEC / "acceptance.md").read_text()
        fr = next(line for line in spec.splitlines() if "**FR-045:**" in line)
        for boundary in ("receipt", "terminal card", "Share", "rehearsal"):
            self.assertIn(boundary, fr)
        self.assertIn("no seed, no receipt, no identifier", shell)
        for check in ("receipt", "terminal card", "Share", "RS-036", "RS-041"):
            self.assertIn(check, next(line for line in acceptance.splitlines() if "A-012 " in line))
        self.assertNotIn("is undecided", shell.split("### 7.2", 1)[1].split("### 7.3", 1)[0])

    def test_result_authorities_preserve_medals_and_serialization_limits(self):
        spec = (SPEC / "spec.md").read_text()
        acceptance = (SPEC / "acceptance.md").read_text()
        receipts = (SPEC / "events-receipts-replays.md").read_text()
        fr = next(line for line in spec.splitlines() if "**FR-045:**" in line)
        card = fr.split("terminal card", 1)[1].split("Share MUST", 1)[0]
        self.assertIn("medal", card)
        gate = next(line for line in acceptance.splitlines() if "A-012 " in line)
        self.assertIn("medal", gate)
        for text in (fr, gate):
            self.assertIn("when state can be serialized", text)
        surface = receipts.split("## Result screen", 1)[1].split("## Acceptance vectors", 1)[0]
        self.assertNotIn("Required visible fields:", surface)
        self.assertIn("FR-045", surface)
        self.assertIn("D-081", surface)
        self.assertIn("D-095", surface)
        self.assertIn("evidence-only", surface)

    def test_environment_inventory_matches_manifest(self):
        manifest = json.loads((ROOT / "contracts/presentation-assets-003.json").read_text())
        ids = manifest["environmentAssetIds"]
        prose = (SPEC / "visual-assets.md").read_text()
        declared = re.search(r"The array names (\d+) IDs:", prose)
        assert declared is not None, "missing environment count"
        self.assertEqual(int(declared[1]), len(ids))
        table = prose.split("The array names", 1)[1].split("The solid IDs", 1)[0]
        covered = []
        for label, prefix in (("Ground tiles", "env_ground_"), ("Solids", "env_solid_"),
                              ("Camera housings", "env_camera_"), ("Street props", "env_prop_"),
                              ("Motif sheets", "env_motif_"), ("Fog layers", "env_fog_")):
            subset = [asset for asset in ids if asset.startswith(prefix)]
            row = re.search(r"\| " + label + r" \| (\d+) \|", table)
            assert row is not None, label
            self.assertEqual(int(row[1]), len(subset), label)
            covered.extend(subset)
        self.assertEqual(set(covered), set(ids))
        self.assertEqual(len(covered), len(set(covered)))

    def test_task_summary_matches_canonical_checkboxes(self):
        tasks = (SPEC / "tasks.md").read_text()
        rows = re.findall(r"^- \[([ x])\] (T\d+[A-Z]?)\b", tasks, re.M)
        self.assertEqual(len(rows), len({task for _, task in rows}))
        open_ids = {task for state, task in rows if state == " "}
        summary = tasks.split("## Open task reconciliation", 1)[1].split("A harness is", 1)[0]
        declared = re.search(r"The (\d+) unchecked tasks", summary)
        assert declared is not None, "missing open-task count"
        self.assertEqual(int(declared[1]), len(open_ids))
        grouped = re.findall(r"\bT\d+[A-Z]?\b", summary.split("They group", 1)[1])
        self.assertEqual(set(grouped), open_ids)
        self.assertEqual(len(grouped), len(open_ids))
        kanban = (ROOT / "docs/kanban.md").read_text()
        self.assertIn("T807 remains checked", kanban)
        self.assertIn("SS-runtime #32", kanban)
        self.assertNotIn("does not close T903, T904, T802, or T807", kanban)


if __name__ == "__main__":
    unittest.main(verbosity=2)
