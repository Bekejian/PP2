import os
print("SECOND TASK") 
def path_access(path: str):
    return {
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }
        
path = r"C:\Users\baqzh\OneDrive\Рабочий стол\labaratory works"
for k, v in path_access(path).items(): 
    print(k, ":", v)