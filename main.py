import os
from re import S, template

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from reportlab.pdfgen.canvas import Canvas
import subprocess

app = FastAPI()

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount("/static", StaticFiles(directory=ROOT_DIR), name="static")
templates = Jinja2Templates(directory=ROOT_DIR)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process_data")
async def create_pdf():
    c = Canvas("myFile.pdf")

    c.drawCentredString(
        600, 800, 'OPENED... Welcome to ReportLab! This is my FIRST App...' )

    c.save()

    subprocess.Popen(['myFile.pdf'], shell=True)
