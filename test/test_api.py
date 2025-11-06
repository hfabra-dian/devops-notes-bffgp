import pytest
from httpx import AsyncClient
from main import app
 
@pytest.mark.asyncio
async def test_crear_tarea():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/tareas", params={"titulo": "Comprar leche", "descripcion": "Ir al supermercado"})
        assert response.status_code == 200
        data = response.json()
        assert data["titulo"] == "Comprar leche"
        assert data["estado"] == "pendiente"
 
@pytest.mark.asyncio
async def test_titulo_obligatorio():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/tareas", params={"titulo": "", "descripcion": "Sin título"})
        assert response.status_code == 400
        assert "título" in response.json()["detail"]
 
@pytest.mark.asyncio
async def test_listar_tareas():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Crear dos tareas
        await ac.post("/tareas", params={"titulo": "Tarea 1", "descripcion": "Desc 1"})
        await ac.post("/tareas", params={"titulo": "Tarea 2", "descripcion": "Desc 2"})
        # Listar tareas
        response = await ac.get("/tareas")
        assert response.status_code == 200
        data = response.json()
        assert len(data) >= 2
 
@pytest.mark.asyncio
async def test_completar_tarea():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Crear tarea
        resp = await ac.post("/tareas", params={"titulo": "Lavar ropa", "descripcion": "Usar detergente"})
        tarea_id = resp.json()["id"]
        # Completar tarea
        response = await ac.put(f"/tareas/{tarea_id}")
        assert response.status_code == 200
        assert response.json()["estado"] == "completada"
 
@pytest.mark.asyncio
async def test_eliminar_tarea():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Crear tarea
        resp = await ac.post("/tareas", params={"titulo": "Eliminar", "descripcion": "Prueba"})
        tarea_id = resp.json()["id"]
        # Eliminar tarea
        response = await ac.delete(f"/tareas/{tarea_id}")
        assert response.status_code == 200
        # Verificar que no esté en la lista
        lista = await ac.get("/tareas")
        assert all(t["id"] != tarea_id for t in lista.json())