import os
from re import template

from  fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=ROOT_DIR), name="static")
templates = Jinja2Templates(directory=ROOT_DIR)
@app.get("/",response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})