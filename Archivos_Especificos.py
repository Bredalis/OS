
import os

# Obtener y mostrar archivos que terminen en .py 
for _, _, archivos in os.walk(os.getcwd()):
	for archivo in archivos:
		if archivo.endswith("py"):
			print(f"Archivo con .py: {archivo}")