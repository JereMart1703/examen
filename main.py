#####  BASICO PARA QUE FUNCIONE
from fastapi import FastAPI , Request,Form
from data.database import database
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#### AÑADIR PARA QUE FUNCIONE LA BASE DE DATOS Y EL MENU

from httpx import request
from data.modelo.menu import Menu
from data.dao.dao_alumnos import DaoAlumnos
from typing import Annotated
app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):

    menu = Menu(True, True)

    alumnos = DaoAlumnos().get_all(database)

    return templates.TemplateResponse(
        request= request, name="default.html", context={"menu": menu,"alumnos": alumnos}
    )


############### DATABASE O PAGINA PRINCIPAL ###########################

@app.get("/database")
def get_alumnos(request: Request):

    menu = Menu(True, True)

    alumnos = DaoAlumnos().get_all(database)

    return templates.TemplateResponse(
        request=request, name="database.html", context={"menu": menu,"alumnos": alumnos}
    )

############# AÑADIR ALUMNOS ###########################

@app.get("/formaddalumnos")
def form_add_alumnos(request: Request):
    menu = Menu(True, True)
    alumnos = DaoAlumnos().get_all(database)
    return templates.TemplateResponse(
        request=request, name="formaddalumnos.html", context={"menu": menu, "alumnos": alumnos}
    )

@app.post("/addalumnos")
def add_alumnos(
    request: Request,
    nombre: Annotated[str, Form()],
    nota1: Annotated[int, Form()],
    nota2: Annotated[int, Form()],
    nota3: Annotated[int, Form()]
):
    dao = DaoAlumnos()
    dao.insert(database, nombre, nota1, nota2, nota3)

    alumnos = dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
        request=request, name="formaddalumnos.html", context={"menu": menu, "alumnos": alumnos}
    )