#!/usr/bin/env python3
#Selective copy
#  Walking through a folder tree and searching for files
#  with a certain file extension('.jpg','.pdf')
#  and copying from whatever location they are present at to a new folder
import shutil, os #imports modules that are used in the script

source ="C:/Users/user/folder/folder/" #Path to where the files are located
newdir = "C:/Users/user/folder/folder/new_folder/" #Path to where the files should be copied

#This chunk of code makes the new directory where the files are to be transfered, if it already exists it does nothing
try:
    os.makedirs(newdir)
except:
    pass

#This next chunk does a couple of things.
# pdfcount = 0 is used to count how many pdf files we have in total in the directory. I am doing this to check that all .pdf files have been copied in the end
pdfcount = 0
#At first, the script crawls trough all files in a directory and all of that directorys underlying subdirectories
for folders, subfolders, filenames in os.walk(source):
    #Then it is told, not to look into the folder Samlede_tekster
    if 'Samlede_tekster' in subfolders:
        subfolders.remove('Samlede_tekster')
    #Here we tell it to count all of the files that ends in .pdf
    for filename in filenames:
        if filename.endswith('.pdf'):
            pdfcount += 1
    #finally we tell the computer to copy all files that ends with .pdf into our "newdir"
    for filename in filenames:
        if filename.endswith('.pdf'):
                shutil.copy(os.path.join(folders,filename), newdir)

#This new chunk of code counts all the pdf files in "newdir"
endcount = 0
for folders, subfolders, filenames in os.walk(newdir):
    for filename in filenames:
        if filename.endswith('.pdf'):
            endcount += 1
#At last i want the  script to tell me how many pdf files it found in the directory, that was our source.
# And then I want i to tell how many pdf files there is in the newly created directory 
print(f"Found {pdfcount} PDF files in source directory.")
print(f"Found {endcount} PDF files in the newly created directory.")
