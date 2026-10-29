"""Evidence-first root exploration briefs; standalone standard-library prototype.

This module does not discover/approve a new financial root. Data adapter validates
source facts and time availability, Alpha agents produce candidates, and an
independent reviewer compares claims to the full historical root archive.
"""
import argparse
import hashlib
import json
import sys

ROLES = {f"{p}{n:02d}" for p, m in (("A", 6), ("B", 3), ("C", 5), ("D", 2)) for n in range(1, m + 1)}
KINDS = {"observation", "literature_question", "explanation_gap"}
QUESTIONS = {
    "observation": "从客观观察出发提出相互竞争的金融解释，明确可区分解释的观察条件，再探索合法日频Alpha表达。",
    "literature_question": "从文献未解问题出发提出可检验的解释，区分来源事实与新假设，再探索合法日频Alpha表达。",
    "explanation_gap": "从观察和既有解释的差异出发，形成不同的可证伪解释，再探索合法日频Alpha表达。",
}
FIELDS = ("seed_id", "kind", "statement", "role_ids", "source_refs", "required_fields", "first_usable_at", "source_snapshot")

def _string(value):
    return isinstance(value, str) and bool(value.strip())

def _list_of_strings(value, *, required=False):
    return (isinstance(value, list) and all(_string(x) for x in value)
            and len(value) == len(set(value)) and (bool(value) or not required))

def _verify_seed(seed):
    if not isinstance(seed, dict) or any(x not in seed for x in FIELDS):
        raise ValueError("seed fields are incomplete")
    if any(not _string(seed[k]) for k in ("seed_id", "statement", "first_usable_at", "source_snapshot")):
        raise ValueError("seed metadata must be nonempty")
    if seed["kind"] not in KINDS:
        raise ValueError("unknown evidence entry kind")
    if not _list_of_strings(seed["source_refs"], required=True):
        raise ValueError("source_refs required")
    if not _list_of_strings(seed["role_ids"], required=True) or set(seed["role_ids"]) - ROLES:
        raise ValueError("invalid role_ids")
    if not _list_of_strings(seed["required_fields"]):
        raise ValueError("invalid required_fields")

def prepare(document):
    """Build a reproducible *research question* for each supported role/seed."""
    if not isinstance(document, dict) or not isinstance(document.get("seeds"), list):
        raise ValueError("expected object with seeds list")
    briefs, seen = [], set()
    for seed in document["seeds"]:
        _verify_seed(seed)
        if seed["seed_id"] in seen:
            raise ValueError("duplicate seed_id")
        seen.add(seed["seed_id"])
        for role in seed["role_ids"]:
            canonical = json.dumps({"seed": seed, "role": role}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
            briefs.append({
                "probe_id": "probe_" + hashlib.sha256(canonical.encode()).hexdigest()[:16],
                "role_id": role,
                "seed_id": seed["seed_id"],
                "entry_kind": seed["kind"],
                "observation_or_question": seed["statement"],
                "research_task": QUESTIONS[seed["kind"]],
                "source_refs": seed["source_refs"],
                "required_fields": seed["required_fields"],
                "first_usable_at": seed["first_usable_at"],
                "source_snapshot": seed["source_snapshot"],
                "submission_contract": "existing_alpha_candidate",
                "new_root_verified": False,
            })
    return {"version": "root-exploration-v0", "briefs": briefs}

def review_packet(proposal, archive):
    """Show a full archive to independent reviewer, with no automated novelty verdict."""
    needed = ("probe_id", "mechanism_claim", "necessary_observation", "falsifiable_prediction")
    if not isinstance(proposal, dict) or any(not _string(proposal.get(k)) for k in needed):
        raise ValueError("proposal needs claim, observation and falsifiable prediction")
    if not isinstance(archive, dict) or not isinstance(archive.get("roots"), list):
        raise ValueError("archive must have roots list")
    for root in archive["roots"]:
        if not isinstance(root, dict) or any(not _string(root.get(k)) for k in ("root_id",) + needed[1:]):
            raise ValueError("archive root is incomplete")
    return {
        "version": "root-exploration-v0",
        "review_status": "requires_independent_review",
        "candidate": proposal,
        "full_root_archive": archive["roots"],
        "review_questions": [
            "哪一已有root具有同样的金融机制主张？",
            "是否需要不同的必要观察，而非仅更换公式或参数？",
            "哪种可证伪预测能将它与最近邻旧解释区分？",
            "现有数据的可用时点能否支持检验？",
        ],
        "automatic_new_root_verdict": None,
    }

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sp = parser.add_subparsers(dest="command", required=True)
    sp.add_parser("prepare").add_argument("seeds_file")
    review = sp.add_parser("review")
    review.add_argument("proposal_file")
    review.add_argument("archive_file")
    args = parser.parse_args(argv)
    def read(path):
        with open(path, encoding="utf8") as f:
            return json.load(f)
    try:
        result = (prepare(read(args.seeds_file)) if args.command == "prepare"
                  else review_packet(read(args.proposal_file), read(args.archive_file)))
    except (OSError, ValueError, json.JSONDecodeError) as ex:
        print("ERROR:", ex, file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
