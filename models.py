from pydantic import BaseModel
from typing import Optional
import uuid

class Tarea(BaseModel):
    id: str
    titulo: str
    descripcion: Optional[str] = None
    estado: str = "pendiente"

    @staticmethod
    def crear(titulo: str, descripcion: str):
        if not titulo.strip():
            raise ValueError("El título es obligatorio")
        return Tarea(id=str(uuid.uuid4()), titulo=titulo, descripcion=descripcion)
