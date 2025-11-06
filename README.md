Grupo conformado por Camilo Bedoya, Henry Fabra, Diego Franco, Gustavo Becerra y Luis Parra.

Resultados pytest sin API

rootdir: D:\data\app_taller_20251106
plugins: anyio-3.7.1
collected 5 items

test/test.py::test_crear_tarea PASSED                                                                                                                                                                    [ 20%] 
test/test.py::test_completar_tarea PASSED                                                                                                                                                                [ 40%] 
test/test.py::test_listar_tareas PASSED                                                                                                                                                                  [ 60%] 
test/test.py::test_eliminar_tarea PASSED                                                                                                                                                                 [ 80%]
test/test.py::test_titulo_obligatorio PASSED 

Y a nivel de API tuvimos el siguiente error

test\test_api.py:46: TypeError
=========================================================================================== short test summary info =========================================================================================== 
FAILED test/test_api.py::test_crear_tarea - TypeError: AsyncClient.__init__() got an unexpected keyword argument 'app'
FAILED test/test_api.py::test_titulo_obligatorio - TypeError: AsyncClient.__init__() got an unexpected keyword argument 'app'
FAILED test/test_api.py::test_listar_tareas - TypeError: AsyncClient.__init__() got an unexpected keyword argument 'app'
FAILED test/test_api.py::test_completar_tarea - TypeError: AsyncClient.__init__() got an unexpected keyword argument 'app'
FAILED test/test_api.py::test_eliminar_tarea - TypeError: AsyncClient.__init__() got an unexpected keyword argument 'app'