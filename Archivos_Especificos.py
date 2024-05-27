
import os 

# Obtener y mostrar archivos que terminen en .py 

for ruta, directorio, archivo in os.walk(os.getcwd()):
	print(f"Archivos: {archivo}")

	for i in archivo:

		if ".py" in i:			
			print(f"Archivo con .py: {i}")