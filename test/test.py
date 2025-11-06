
import pytest
from gestor import GestorTareas
# Suponemos que existe una clase Tarea y un gestor GestorTareas
# que implementaremos después del diseño de pruebas.

@pytest.fixture
def gestor():
    return GestorTareas()

def test_crear_tarea(gestor):
    tarea = gestor.crear_tarea("Comprar leche", "Ir al supermercado")
    assert tarea.titulo == "Comprar leche"
    assert tarea.estado == "pendiente"
    assert tarea.descripcion == "Ir al supermercado"

def test_completar_tarea(gestor):
    tarea = gestor.crear_tarea("Lavar ropa", "Usar detergente")
    gestor.completar_tarea(tarea.id)
    assert tarea.estado == "completada"

def test_listar_tareas(gestor):
    gestor.crear_tarea("Tarea 1", "Descripción 1")
    gestor.crear_tarea("Tarea 2", "Descripción 2")
    lista = gestor.listar_tareas()
    assert len(lista) == 2
    assert all(hasattr(t, "titulo") for t in lista)

def test_eliminar_tarea(gestor):
    tarea = gestor.crear_tarea("Tarea a eliminar", "Descripción")
    gestor.eliminar_tarea(tarea.id)
    lista = gestor.listar_tareas()
    assert tarea not in lista

def test_titulo_obligatorio(gestor):
    with pytest.raises(ValueError) as e:
        gestor.crear_tarea("", "Descripción sin título")
    assert "título es obligatorio" in str(e.value)
