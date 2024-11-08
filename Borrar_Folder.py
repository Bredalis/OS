
import os

ruta = "C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Python/OS/Folder"

try:
	os.rmdir(ruta)
	print(f"Directorio borrado: '{ruta}'")

except FileNotFoundError:
	print(f"Error: El directorio '{ruta}' no existe.")

except OSError:
	print(f"No se pudo borrar el directorio '{ruta}'. Asegúrate de que esté vacío.")

except Exception as e:
	print(f"Error inesperado: {e}")