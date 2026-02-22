
import os


# Get and display files starting with 'A' or 'M'
for path, _, files in os.walk(os.getcwd()):
    for file in files:
        if file.startswith(("A", "M")):
            print(f"File starting with A or M: {file}")

        print(os.path.join(path, file))
    print(path)
