from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ui.drift import scan_repo
from ui.devin_client import create_devin_session

app = FastAPI(title="DocPulse")
templates = Jinja2Templates(directory="ui/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "scan_result": None,
            "session_result": None,
            "error": None,
        },
    )


@app.post("/scan", response_class=HTMLResponse)
def scan(request: Request):
    result = scan_repo(".")
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "scan_result": result,
            "session_result": None,
            "error": None,
        },
    )


@app.post("/run", response_class=HTMLResponse)
def run(request: Request, repo_name: str = Form(...)):
    scan_result = scan_repo(".")
    session_result = None
    error = None

    try:
        if scan_result["drift_found"]:
            session_result = create_devin_session(repo_name, scan_result["findings"])
    except Exception as exc:
        error = str(exc)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "scan_result": scan_result,
            "session_result": session_result,
            "error": error,
            "repo_name": repo_name,
        },
    )