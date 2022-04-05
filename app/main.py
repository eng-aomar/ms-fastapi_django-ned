
from urllib.request import Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import pathlib
app = FastAPI()
BASE_DIR = pathlib.Path(__file__).parent
UPLOAD_DIR = BASE_DIR / "uploads"

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse) # http GET -> JSON
def home_view(request:Request ):
    return templates.TemplateResponse("home.html", {"request": request, "abc": 123})


@app.post("/")
def home_detail_view():
    return {"Hello": "World"}
