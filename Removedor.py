
# Libreria

import os

# Borrar multicarpetas

remover = os.removedirs("A/B/C")
renombrar = os.rename("C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Python/OS/OS", "Modulo.py")
estadistica = os.stat("Modulo.py")

print(f"Remover: {remover}")
print(renombrar)
print(f"Operacion estadistica: {estadistica}")