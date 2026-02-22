
import os


# Get and display files ending in .py
for _, _, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith("py"):
            print(f"File with .py: {file}")
