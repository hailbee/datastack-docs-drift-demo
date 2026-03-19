import os
import httpx


DEVIN_API_KEY = os.getenv("DEVIN_API_KEY", "")
USE_MOCK_DEVIN = os.getenv("USE_MOCK_DEVIN", "false").lower() == "true"


def build_prompt(repo_name: str, findings: list[str]) -> str:
    findings_text = "\n".join(f"- {item}" for item in findings)

    return f"""
You are helping fix documentation drift in the repository {repo_name}.

Goal:
Inspect the codebase and update stale documentation so that docs match the current API behavior.

Known findings from an upstream scanner:
{findings_text}

Primary source of truth:
- FastAPI app in app/main.py
- OpenAPI output from the FastAPI application

Please:
1. Verify the current API behavior from the code.
2. Update README.md, docs/api.md, and examples/curl_examples.md.
3. Correct outdated endpoint names, request body fields, and example responses.
4. Do not change application behavior unless absolutely necessary.
5. Open a PR with a concise summary of what drift was found and what docs were updated.

Success criteria:
- Docs reference GET /purchases/{{purchase_id}} instead of GET /orders/{{order_id}}
- POST /users docs match the actual request fields
- Curl examples and response examples are aligned with the code
""".strip()


def create_devin_session(repo_name: str, findings: list[str]) -> dict:
    prompt = build_prompt(repo_name, findings)

    if USE_MOCK_DEVIN:
        return {
            "mode": "mock",
            "session_id": "mock-session-123",
            "status": "created",
            "url": "https://example.com/mock-devin-session",
            "prompt": prompt,
        }

    if not DEVIN_API_KEY:
        raise RuntimeError("Missing DEVIN_API_KEY")

    headers = {
        "Authorization": f"Bearer {DEVIN_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "prompt": prompt
    }

    with httpx.Client(timeout=60.0) as client:
        response = client.post(
            "https://api.devin.ai/v1/sessions",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        data = response.json()

    return {
        "mode": "real",
        "session_id": data.get("session_id") or data.get("id") or "unknown",
        "status": data.get("status", "created"),
        "url": data.get("url") or data.get("web_url") or "",
        "raw": data,
    }