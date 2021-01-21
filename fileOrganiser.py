import os
import shutil
path = input("Enter the name of the folder that is to be sorted: ")
listFiles = os.listdir(path)
for file in listFiles:
    name, ext = os.path.splitext(file)
    ext = ext[1: ]
    if ext == "":
        continue
    if os.path.exists(path + "/" + ext):
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
    else:
        os.makedirs(path + "/" + ext)
        shutil.move(path + "/" + file, path + "/" + ext + "/" + file)

