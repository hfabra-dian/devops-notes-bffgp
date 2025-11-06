from models import Tarea

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def crear_tarea(self, titulo, descripcion):
        tarea = Tarea.crear(titulo, descripcion)
        self.tareas.append(tarea)
        return tarea

    def completar_tarea(self, id):
        for t in self.tareas:
            if t.id == id:
                t.estado = "completada"
                return t
        raise ValueError("Tarea no encontrada")

    def listar_tareas(self):
        return self.tareas

    def eliminar_tarea(self, id):
        self.tareas = [t for t in self.tareas if t.id != id]
