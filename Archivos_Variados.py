
import os

# Obtener y mostrar archivos que inician con 'A' o 'M'
for ruta, _, archivos in os.walk(os.getcwd()):
	for archivo in archivos:
		if archivo.startswith(("A", "M")):			
			print(f"Archivo con A o M en el inicio: {archivo}")

	print(os.path.join(ruta, archivo))
	print(ruta)