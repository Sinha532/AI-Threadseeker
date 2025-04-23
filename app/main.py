from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.data_loader import load_mock_data
from app.search import ThreadSearchEngine

app = FastAPI(title="🧵 ThreadSeeker")
templates = Jinja2Templates(directory="app/templates")

# Load data + setup engine
mock_threads = load_mock_data()
engine = ThreadSearchEngine(mock_threads)

@app.get("/", response_class=HTMLResponse)
def home(request: Request, q: str = ""):
    results = engine.search(q) if q else []
    return templates.TemplateResponse("index.html", {
        "request": request,
        "results": results,
        "query": q
    })
