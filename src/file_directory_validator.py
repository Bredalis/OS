
import os


url = "URL"
is_file = os.path.isfile(os.path.join(url, "url_for_file"))
is_directory = os.path.isdir(os.path.join(url, "url_for_directory"))

print("Is it a file?:", is_file)
print("Is it a directory?:", is_directory)
