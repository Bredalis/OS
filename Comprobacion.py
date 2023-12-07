 
# Comprobar si es un archivo o directorio

import os

es_archivo = os.path.isfile("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Python/OS/Alegria.ico")
es_directorio = os.path.isdir("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Python/OS/Imagenes")

print("¿Es un archivo?:", es_archivo)
print("¿Es un directorio?:", es_directorio)