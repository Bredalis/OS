
import os

# Mostrar todas las rutas en el directorio actual y sus subdirectorios
for ruta, _, _ in os.walk(os.getcwd()):	
	print(f"Ruta: {ruta}")