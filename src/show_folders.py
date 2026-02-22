
import os


# Get and display directories
for _, directories, _ in os.walk(os.getcwd()):
    if directories:
        print(f"Directories: {directories}")
