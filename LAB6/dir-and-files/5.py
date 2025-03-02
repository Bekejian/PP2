import os
print("FIFTH TASK")
def writesome(list_of_elements):
    with open("file2.txt", 'a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome([12345, 56789, "BAQZHAN", "CHINA",])