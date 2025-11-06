import sys
import os

# Agregar la carpeta padre (proyecto) al path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)