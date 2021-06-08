import os
import shutil
# write the name of the directory here that needs to go sorted
path = input("Enter the name of the directory to be sorted")

# This will create a properly organized list with all the files that are in the directory 
listoffiles = os.listdir(path)

# This will go through each and every file in the directory
for file in listoffiles:

    # splittext() will split the file name into its name and extension in respective variables  
    name,ext = os.path.splitext(file)
    
    # this is going to store the extension type
    # it takes out only the extension excluding '.' 
    ext= ext[1:]
   
    
    # this forces the next iteration that is if it is a directory
    if ext == '':
        continue
    
    # this will move the file to the directory where the name 'ext' already exists 
    if os.path.exists(path+'/'+ ext):
        shutil.move(path+'/'+file, path + '/'+ ext+ '/'+ file )
    
    # this will create a new directory if the directory does not exist
    else : 
        os.makedirs(path + '/'+ ext)
        shutil.move(path+'/'+file, path + '/'+ ext+ '/'+ file )