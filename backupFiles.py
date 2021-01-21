import os
import shutil
source = input("Enter Source Folder Name: ")
destination = input("Enter destination Folder Name: ")
source = source + "/"
destination = destination + "/"
listOfFiles = os.listdir(source)
for File in listOfFiles:
    shutil.copy((source + File), destination)