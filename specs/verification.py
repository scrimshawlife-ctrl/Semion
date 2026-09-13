"""Check advisory spec integrity, not runtime conformance. No network or data writes."""
import copy
import json
import re
import shutil
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = "e5ed91bd90afb0429cf816504c7d5e622bbbc153"
FIELDS = ["Purpose", "Actors", "Triggers", "Preconditions", "Inputs", "Happy path",
          "Alternate/failure paths", "State transitions", "Terminal states", "Side effects",
          "Invariants", "Permissions", "Observability/audit", "Acceptance criteria",
          "Dependencies", "Unresolved items"]
STAGES = ["Constitution/doctrine", "Domain model", "Requirements", "Journeys", "Workflows",
          "State machines", "Contracts", "Data model", "Security/privacy/governance",
          "Architecture", "Acceptance criteria", "Traceability", "Tasks", "Verification"]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def workflow_errors(text):
    errors = []
    chunks = re.split(r"(?m)^## (WF-\d{3})\s*$", text)
    ids = chunks[1::2]
    if len(ids) != len(set(ids)) or not ids:
        errors.append("workflow ids")
    for wid, body in zip(chunks[1::2], chunks[2::2]):
        for field in FIELDS:
            matches = re.findall(r"(?m)^\| " + re.escape(field) + r" \| (.+) \|$", body)
            if len(matches) != 1 or not matches[0].strip():
                errors.append(wid + ":" + field)
    return errors


def requirement_errors(text):
    ids = re.findall(r"(?m)^\| (REQ-\d{3}) \|", text)
    return not ids or len(ids) != len(set(ids))


def trace_errors(trace, definitions):
    errors = []
    rows = trace["rows"]
    ids = [r["requirement"] for r in rows]
    if set(ids) != definitions["REQ"] or len(ids) != len(set(ids)):
        errors.append("requirement coverage")
    for row in rows:
        for key, prefix in [("requirement", "REQ"), ("workflow", "WF"),
                            ("acceptance", "AC"), ("task", "TASK")]:
            if row[key] not in definitions[prefix]:
                errors.append(key)
        for key, prefix in [("state_machines", "SM"), ("contracts", "CON")]:
            if not row[key] or any(v not in definitions[prefix] for v in row[key]):
                errors.append(key)
        if row["runtime_status"] != "NOT_COMPUTABLE" or not row["evidence"].strip():
            errors.append("unsupported conformance")
        if not (ROOT / row["verification"]).is_file():
            errors.append("verification path")
    for key, prefix in [("workflow", "WF"), ("acceptance", "AC"), ("task", "TASK")]:
        if {r[key] for r in rows} != definitions[prefix]:
            errors.append("unmapped " + key)
    return errors


def main():
    workflows = read("specs/workflows.md")
    requirements = read("specs/requirements.md")
    definitions = {
        "WF": set(re.findall(r"(?m)^## (WF-\d{3})\s*$", workflows)),
        "REQ": set(re.findall(r"(?m)^\| (REQ-\d{3}) \|", requirements)),
        "SM": set(re.findall(r"(?m)^\| (SM-\d{3}) \|", read("specs/state-machines.md"))),
        "CON": set(re.findall(r"(?m)^## (CON-\d{3}) ", read("specs/contracts.md"))),
        "AC": set(re.findall(r"(?m)^## (AC-\d{3})\s*$", read("specs/acceptance.md"))),
        "TASK": set(re.findall(r"(?m)^\| (TASK-\d{3}) \|", read("specs/completion-tasks.md"))),
        "DEC": set(re.findall(r"(?m)^\| (DEC-\d{3}) \|", read("specs/decisions.md"))),
    }
    assert not workflow_errors(workflows)
    assert not requirement_errors(requirements)
    trace = json.loads(read("specs/traceability.json"))
    assert trace["methodology"] == STAGES
    index = read("docs/START_HERE.md")
    for n, stage in enumerate(STAGES, 1):
        assert f"| {n} {stage} |" in index
    assert not trace_errors(trace, definitions)
    assert workflow_errors(workflows.replace("| Permissions |", "| Removed |", 1))
    row = next(line for line in requirements.splitlines() if line.startswith("| REQ-"))
    assert requirement_errors(requirements + "\n" + row)
    broken = copy.deepcopy(trace)
    broken["rows"][0]["workflow"] = "WF-999"
    assert trace_errors(broken, definitions)
    broken = copy.deepcopy(trace)
    broken["rows"][0]["runtime_status"] = "PASS"
    assert trace_errors(broken, definitions)

    git = shutil.which("git") or r"C:\Program Files\Git\cmd\git.exe"
    def command(*args):
        return subprocess.check_output([git, *args], cwd=ROOT, text=True, encoding="utf-8")
    changed = set(command("diff", "--name-only", BASE).splitlines())
    changed.update(command("ls-files", "--others", "--exclude-standard").splitlines())
    # This exact sanitized receipt is intentionally included even if out/ is ignored.
    receipt = "out/audit/spec-completion.latest.json"
    if (ROOT / receipt).is_file():
        changed.add(receipt)
    assert changed
    allowed = {"README.md", "STATUS.md", "ARCHITECTURE.md"}
    for rel in sorted(changed):
        assert rel in allowed or rel.startswith(("specs/", "docs/", "out/audit/")), rel
        text = read(rel)
        assert "Provenance:" in text and BASE in text, rel
        if rel.endswith(".md"):
            for prefix, ids in definitions.items():
                for ref in re.findall(r"\b" + prefix + r"-\d{3}\b", text):
                    assert ref in ids, (rel, ref)
            for link in re.findall(r"\]\(([^)]+)\)", text):
                if ":" in link or link.startswith("#"):
                    continue
                target = (ROOT / rel).parent / unquote(link.split("#", 1)[0])
                target = target.resolve()
                assert target.is_relative_to(ROOT) and target.exists(), (rel, link)
    assert json.loads(read("schemas/semion.frame.v0.schema.json")) == json.loads(read("contracts/semion.frame.v0.json"))
    subprocess.run([git, "diff", "--check", BASE], cwd=ROOT, check=True)
    print("SEMION_SPEC_PASS " + " ".join(f"{k}={len(v)}" for k, v in definitions.items())
          + f" stages={len(STAGES)} workflow_fields={len(FIELDS)} negative_controls=4 changed_files={len(changed)}")


if __name__ == "__main__":
    main()

# Provenance: Notion Sprint 001 Hub [not inspected; Semion handoff read 2026-09-13 UTC] + Loop 805 Slice N/A (Semion advisory) + Hash: e5ed91bd90afb0429cf816504c7d5e622bbbc153 (base)
