
import os

# Crear una carpeta y subcarpetas
os.mkdir("Folder")
os.makedirs("A/B/C")

# Obtener y mostar la ruta actual
print(f"Ruta: {os.getcwd()}")