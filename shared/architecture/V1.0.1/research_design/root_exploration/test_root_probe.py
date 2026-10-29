"""Synthetic-only smoke and regression tests; no company data."""
import copy
import unittest
from root_probe import prepare, review_packet

SEED = {
    "seed_id": "demo", "kind": "observation",
    "statement": "仅合成演示：相同收益集合不同出现顺序，价格路径可能不同。",
    "role_ids": ["A04"], "source_refs": ["synthetic-only"],
    "required_fields": ["minute_close"],
    "first_usable_at": "after_trade_day_t", "source_snapshot": "synthetic-v0"
}

class RootProbeTests(unittest.TestCase):
    def test_deterministic_and_source_traceable(self):
        x = prepare({"seeds": [SEED]})
        self.assertEqual(x, prepare({"seeds": [copy.deepcopy(SEED)]}))
        self.assertEqual(x["briefs"][0]["role_id"], "A04")
        self.assertFalse(x["briefs"][0]["new_root_verified"])
        self.assertEqual(x["briefs"][0]["source_refs"], ["synthetic-only"])

    def test_missing_source_and_invalid_role(self):
        bad = copy.deepcopy(SEED)
        bad["source_refs"] = []
        with self.assertRaises(ValueError):
            prepare({"seeds": [bad]})
        bad = copy.deepcopy(SEED)
        bad["role_ids"] = ["Z99"]
        with self.assertRaises(ValueError):
            prepare({"seeds": [bad]})

    def test_distinct_entry_kinds(self):
        inputs = []
        for kind in ("observation", "literature_question", "explanation_gap"):
            item = copy.deepcopy(SEED)
            item["kind"] = kind
            item["seed_id"] = kind
            inputs.append(item)
        briefs = prepare({"seeds": inputs})["briefs"]
        self.assertEqual(len(set(b["research_task"] for b in briefs)), 3)

    def test_novelty_not_self_approved(self):
        p = {"probe_id": "demo", "mechanism_claim": "claim", "necessary_observation": "obs",
             "falsifiable_prediction": "prediction"}
        a = {"roots": [{"root_id": "R01", "mechanism_claim": "claim",
                        "necessary_observation": "obs", "falsifiable_prediction": "prediction"}]}
        x = review_packet(p, a)
        self.assertIsNone(x["automatic_new_root_verdict"])
        self.assertEqual(x["review_status"], "requires_independent_review")

if __name__ == "__main__":
    unittest.main()
