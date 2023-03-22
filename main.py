import os
from re import template

from  fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqladmin import Admin, ModelView
from models import *

app = FastAPI()
admin = Admin(app, engine)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
class UserAdmin(ModelView, model=User):
    name = "Челик"
    name_plural = "Челики"
    icon = "fa-solid fa-user"
    
    column_list = [User.id, User.name]


admin.add_view(UserAdmin)

app.mount("/static", StaticFiles(directory=ROOT_DIR), name="static")
templates = Jinja2Templates(directory=ROOT_DIR)
@app.get("/",response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})