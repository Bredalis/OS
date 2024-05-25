
# Libreria

import os

# Obtener y mostrar archivos

for ruta, directorio, archivo in os.walk(os.getcwd()):
	for i in archivo:

		if i[0] == "A" or i[0] == "M":

			# Acceso a archivos que inician con A o M
			print(f"Archivo con A o M de de inicio: {i}")

	# Obtener y mostrar url
	print(ruta + "\\" + i)