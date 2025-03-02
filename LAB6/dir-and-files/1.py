print("FIRST TASK")
import os
def dirs_files(path):
    dirs__files = os.listdir(path)
    dirs = [a for a in dirs__files if os.path.isdir(os.path.join(path, a))]
    files = [a for a in dirs__files if os.path.isfile(os.path.join(path, a))]
    
    return dirs, dirs__files, files

path = r"C:\Users\baqzh\OneDrive\Рабочий стол\labaratory works"
for a in dirs_files(path): print(a)