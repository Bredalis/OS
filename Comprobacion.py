
import os

url = "C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/"
es_archivo = os.path.isfile(url + "Python/OS/Alegria.ico")
es_directorio = os.path.isdir(url + "Icon/Imagenes")

print("¿Es un archivo?:", es_archivo)
print("¿Es un directorio?:", es_directorio)