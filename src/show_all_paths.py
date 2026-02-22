
import os


# Display all paths in the current directory and its subdirectories
for path, _, _ in os.walk(os.getcwd()):
    print(f"Path: {path}")
