import os
import shutil
source = input("Enter your source folder name")
destination = input("Enter your destination")
source = source + '/'
destination = destination + '/'
listoffiles = os.listdir(source)

for file in listoffiles:
    shutil.move((source+file), destination)
    