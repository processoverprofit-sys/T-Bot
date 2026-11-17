"""Standalone educational example; not a component of T-Bot."""


def review_gate(verdict: str, approved: bool) -> dict:
    """Return a fictional review record. No external action is performed."""
    accepted = verdict == "ALLOW" and approved is True
    return {
        "decision": "ALLOW" if accepted else "REJECT",
        "dummy_action_count": int(accepted),
    }


if __name__ == "__main__":
    import json

    for verdict, approved in [("DENY", True), ("UNKNOWN", True), ("ALLOW", False), ("ALLOW", True)]:
        print(json.dumps({"input": {"verdict": verdict, "approved": approved},
                          "output": review_gate(verdict, approved)}, sort_keys=True))
