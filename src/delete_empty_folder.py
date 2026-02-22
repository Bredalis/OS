
import os


path = "url"

try:
    os.rmdir(path)
    print(f"Directory deleted: '{path}'")

except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")

except OSError:
    print(f"Could not delete directory '{path}'. Make sure it is empty.")

except Exception as e:
    print(f"Unexpected error: {e}")
