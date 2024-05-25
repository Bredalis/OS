
# Libreria

import os

# Obtener y mostrar directorios

for ruta, directorio, archivo in os.walk(os.getcwd()):

	if len(directorio) != 0:
		print(f"Directorio: {directorio}")