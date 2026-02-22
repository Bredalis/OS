
import os


try:
    # Change to the specified directory and list its contents
    path = "url"
    os.chdir(path)
    directories = os.listdir()

    print(f"Current path: {os.getcwd()}")
    print(f"Directory contents: {directories}")

except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")

except Exception as e:
    print(f"Unexpected error: {e}")
