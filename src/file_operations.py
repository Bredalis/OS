
import os


def check_if_exists(path):
    """Verify if the path exists."""
    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        return False
    return True


try:
    # Delete subfolders if they exist
    path_to_remove = "A/B/C"
    if check_if_exists(path_to_remove):
        os.removedirs(path_to_remove)
        print(f"The directory '{path_to_remove}' has been deleted.")

    # Rename file and get statistics
    path = "url"
    new_name = "Modulo.py"

    if check_if_exists(path):
        os.rename(path, new_name)
        print(f"File statistics for '{new_name}': {os.stat(new_name)}")

except FileNotFoundError as e:
    print(f"Error: {e}")

except OSError as e:
    print(f"Could not delete directory or rename file: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
