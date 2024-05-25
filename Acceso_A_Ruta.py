
# Libreria

import os

# Obtener y mostrar la ruta

for ruta, directorio, archivo in os.walk(os.getcwd()):	
	print(f"Ruta: {ruta}")