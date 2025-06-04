#####  BASICO PARA QUE FUNCIONE
from fastapi import FastAPI , Request,Form
from data.database import database
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#### AÑADIR PARA QUE FUNCIONE LA BASE DE DATOS Y EL MENU
### PONER DESDE EL PRINCIPIO Y T AHORRAS PROBLEMAS

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


############### DATABASE O PAGINA PRINCIPAL PARA VER LA TABLA ###########################

@app.get("/database")
def get_alumnos(request: Request):

    menu = Menu(True, True)

    alumnos = DaoAlumnos().get_all(database)

    return templates.TemplateResponse(
        request=request, name="database.html", context={"menu": menu,"alumnos": alumnos}
    )


############ TABLA CON MEJORES NOTAS ########################

@app.get("/vernotas")
def ver_notas(request: Request):
    menu = Menu(True, True)
    dao = DaoAlumnos() # SE PONE EL NOMBRE DEL CLASS DEL DAO_ALUMNOS.PY
    alumnos = dao.get_all(database) #PONES EL NOMBRE DEL TEMA IGUALADO A DAO GET ALL DATABASE , SI TE PIDE HOSPITAL PUES HOSPITAL = , ALUMNOS , PUES ALUMNOS =

    return templates.TemplateResponse(
        request=request,
        name="vernotas.html",
        context={"menu": menu, "alumnos": alumnos}
    ) # ESTO SE SIEMPRE LO MISMO MENOS EL NAME DEL HTML

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
        request=request, name="addalumnos.html", context={"menu": menu, "alumnos": alumnos}
    )


################## ELIMINAR ALUMNOS ##############################


@app.get("/fromdelalumnos")
def form_del_alumnos(request: Request):
    menu = Menu(True, True)
    dao = DaoAlumnos()
    
    alumnos = dao.get_all(database)
    return templates.TemplateResponse(
        request=request,
        name="formdelalumnos.html",
        context={"menu": menu, "alumnos": alumnos}
    )

@app.post("/delalumnos")
def del_alumnos(request: Request, alumno_id: Annotated[int, Form()]):
    dao = DaoAlumnos()
    dao.delete(database, alumno_id)
    alumnos = dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
        request=request,
        name="delalumnos.html",
        context={"menu": menu, "alumnos": alumnos}
    )

############## ACTUALIZAR #########################

@app.get("/formupdatenotas")
def form_update_notas(request: Request):
    dao = DaoAlumnos()
    alumnos = dao.get_all(database)
    menu = Menu(True, True)
    return templates.TemplateResponse(
        request=request,
        name="formupdatenotas.html",
        context={"menu": menu, "alumnos": alumnos}
    )
