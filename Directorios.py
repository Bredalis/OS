
import os

# Obtener y mostrar directorios
for _, directorios, _ in os.walk(os.getcwd()):
	if directorios:
		print(f"Directorios: {directorios}")