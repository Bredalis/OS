
import os

# Verificar si existe la ruta
def verificar_si_existe(ruta):
    if not os.path.exists(ruta):
        print(f"Error: La ruta '{ruta}' no existe.")
        return False
    return True

try:
    # Borrar subcarpetas si existen
    ruta_remover = "A/B/C"
    if verificar_si_existe(ruta_remover):
        os.removedirs(ruta_remover)
        print(f"El directorio '{ruta_remover}' ha sido eliminado.")

    # Renombrar y obtener estadísticas del archivo
    ruta = "C:/Users/Bradalis/Desktop/LenguajesDeProgramacion/Python/OS/OS"
    nuevo_nombre = "Modulo.py"
    
    if verificar_si_existe(ruta):
        os.rename(ruta, nuevo_nombre)
        print(f"Estadísticas del archivo '{nuevo_nombre}': {os.stat(nuevo_nombre)}")

except FileNotFoundError as e:
    print(f"Error: {e}")

except OSError as e:
    print(f"No se pudo borrar el directorio o renombrar el archivo: {e}")

except Exception as e:
    print(f"Error inesperado: {e}")