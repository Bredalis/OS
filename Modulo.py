
# Libreria

import os

# Comandos

ruta = os.getcwd()

# Cambiar de directorio actual
nueva_ruta = os.chdir(r"C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/BBDD/Programas")
directorios = os.listdir()

print(f"Obtener ruta: {ruta}")
print(f"Lista de directorios: {directorios}")