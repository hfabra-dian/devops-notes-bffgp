from fastapi import FastAPI, HTTPException
from gestor import GestorTareas
from models import Tarea

app = FastAPI()
gestor = GestorTareas()

@app.post("/tareas", response_model=Tarea)
def crear_tarea(titulo: str, descripcion: str):
    try:
        return gestor.crear_tarea(titulo, descripcion)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/tareas", response_model=list[Tarea])
def listar_tareas():
    return gestor.listar_tareas()

@app.put("/tareas/{id}", response_model=Tarea)
def completar_tarea(id: str):
    try:
        return gestor.completar_tarea(id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tareas/{id}")
def eliminar_tarea(id: str):
    gestor.eliminar_tarea(id)
