
# Libreria

import os

# Borrar multicarpetas

remover = os.removedirs('A/B/C')

url = 'C:/Users/Angelica Gerrero/Desktop/LenguajesDeProgramacion/Python/OS/OS'
renombrar = os.rename(url, 'Modulo.py')
estadistica = os.stat('Modulo.py')

print(f'Remover: {remover}')
print(renombrar)
print(f'Operacion estadistica: {estadistica}')