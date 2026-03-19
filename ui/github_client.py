import os
import httpx

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
GITHUB_OWNER = os.getenv("GITHUB_OWNER", "")
GITHUB_REPO = os.getenv("GITHUB_REPO", "")

DEFAULT_LABELS = [
    ("documentation", "0075ca", "Documentation updates"),
    ("automation", "5319e7", "Automation-generated workflow"),
    ("devin-generated", "1d76db", "Created by Devin workflow"),
]


def _headers():
    if not GITHUB_TOKEN:
        raise RuntimeError("Missing GITHUB_TOKEN")
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def ensure_labels_exist():
    with httpx.Client(timeout=30.0) as client:
        for name, color, description in DEFAULT_LABELS:
            resp = client.post(
                f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/labels",
                headers=_headers(),
                json={
                    "name": name,
                    "color": color,
                    "description": description,
                },
            )
            if resp.status_code in (200, 201):
                continue
            if resp.status_code == 422:
                # label already exists
                continue
            resp.raise_for_status()


def apply_labels_to_pr(pr_number: int):
    ensure_labels_exist()

    labels = [name for name, _, _ in DEFAULT_LABELS]

    with httpx.Client(timeout=30.0) as client:
        resp = client.post(
            f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/issues/{pr_number}/labels",
            headers=_headers(),
            json={"labels": labels},
        )
        resp.raise_for_status()
        return resp.json()