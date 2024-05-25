
# Libreria

import os

# Borrar multicarpetas

remover = os.removedirs("A/B/C")

url = "C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Python/OS/OS"

print(f"Remover: {remover}")
print(os.rename(url, "Modulo.py"))
print(f"Operacion estadistica: {os.stat("Modulo.py")}")