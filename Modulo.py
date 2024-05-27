
import os

ruta = os.getcwd()

# Cambiar de directorio actual

url = "C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/BBDD/Programas"
nueva_ruta = os.chdir(url)
directorios = os.listdir()

print(f"Obtener ruta: {ruta}")
print(f"Lista de directorios: {directorios}")