
import os

url = "C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/"
es_archivo = os.path.isfile(os.path.join(url, "Python/OS/Alegria.ico"))
es_directorio = os.path.isdir(os.path.join(url, "Icon/Imagenes"))

print("¿Es un archivo?:", es_archivo)
print("¿Es un directorio?:", es_directorio)