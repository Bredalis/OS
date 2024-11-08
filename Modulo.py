
import os

try:
	# Cambiar al directorio especificado y listar su contenido
	url = "C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Practica"
	os.chdir(url)
	directorios = os.listdir()

	print(f"Ruta actual: {os.getcwd()}")
	print(f"Contenido del directorio: {directorios}")

except FileNotFoundError:
	print(f"Error: El directorio '{url}' no existe.")

except Exception as e:
	print(f"Error inesperado: {e}")