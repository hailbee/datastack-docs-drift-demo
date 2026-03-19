from pathlib import Path

DOC_FILES = [
    "README.md",
    "docs/api.md",
    "examples/curl_examples.md",
]

EXPECTED_STRINGS = [
    "POST /users",
    "GET /purchases/{purchase_id}",
    "email",
    "full_name",
]

OUTDATED_STRINGS = [
    "GET /orders/{order_id}",
    '"name":"Jane Doe"',
    "| name | string | yes |",
]


def scan_repo(root: str = ".") -> dict:
    findings = []

    for rel_path in DOC_FILES:
        path = Path(root) / rel_path
        if not path.exists():
            findings.append(f"{rel_path} is missing")
            continue

        content = path.read_text()

        if "GET /orders/{order_id}" in content:
            findings.append(f"{rel_path} references outdated endpoint GET /orders/{{order_id}}")

        if '"name":"Jane Doe"' in content or '"name": "Jane Doe"' in content:
            findings.append(f"{rel_path} uses outdated user creation example with field 'name'")

        if "| name | string | yes |" in content:
            findings.append(f"{rel_path} documents outdated request schema for POST /users")

    return {
        "drift_found": len(findings) > 0,
        "findings": findings,
        "expected": EXPECTED_STRINGS,
        "outdated": OUTDATED_STRINGS,
    }