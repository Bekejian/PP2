import os

file_path = "exampleford.txt"

if os.path.exists(file_path) and os.access(file_path, os.W_OK):
    os.remove(file_path)
    print("File deleted!")
else:
    print("Can not find file")