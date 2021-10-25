#!/usr/bin/env python3
# Selective copy
# Walking through a folder tree and searching for files
# with a certain file extension('.jpg','.pdf')
# and copying from whatever location they are present at to a new folder
import shutil
import os
import argparse

# Makes the program take commandline inputs
parser = argparse.ArgumentParser(description= '''A program, that copies all files in a directory and its subdirectories 
                                                with the specified ending to a new location on your computer.''')
parser.add_argument("INPUT", help="The path to your input directory, where your files are located.")
parser.add_argument("OUTPUT", help="The path to where you want your files to be copied to.")
parser.add_argument("FILETYPE", help="The specific filetype you want to copy. (PDF, JPG, etc.)")
args = parser.parse_args()

# Saves the CLI inputs to python objects
INPUT = args.INPUT
OUTPUT = args.OUTPUT
filetype = args.FILETYPE

# This chunk of code makes the new directory where the files are to be
# transfered, if it already exists it does nothing
try:
    os.makedirs(OUTPUT)
except:
    pass

# pdfcount = 0 is used to count how many pdf files we have in total in the directory. 
# I am doing this to check that all specified files have been copied in the end
pdfcount = 0

if filetype == filetype.upper():
    # At first, the script crawls trough all files in a directory 
    # and all of that directorys underlying subdirectories
    for folders, subfolders, filenames in os.walk(INPUT):
        # Then it is told, not to look into the newly created folder
        # if it is located inside the INPUT folder 
        if OUTPUT in subfolders:
            subfolders.remove(OUTPUT)
        # Here we tell it to count all of the files that ends with the FILETYPE-input
        for filename in filenames:
            if filename.endswith('.'+ args.FILETYPE) or filename.endswith('.'+ args.FILETYPE.lower()):
                pdfcount += 1
        # Finally we tell the program to copy all files that ends with
        # the FILETYPE-input into our OUTPUT directory
        for filename in filenames:
            if filename.endswith('.'+ args.FILETYPE) or filename.endswith('.'+ args.FILETYPE.lower()):
                    shutil.copy(os.path.join(folders,filename), OUTPUT)
else:
    print("ERROR: Your FILETYPE-INPUT needs to bo be capitalized! Please try again.")
    exit()

# This chunk of code counts all the files in OUTPUT with the FILETYPE ending.
endcount = 0
for folders, subfolders, filenames in os.walk(OUTPUT):
    for filename in filenames:
        if filename.endswith('.'+ args.FILETYPE) or filename.endswith('.'+ args.FILETYPE.lower()):
            endcount += 1
#At last i want the  script to tell me how many pdf files it found in the directory, that was our INPUT.
# And then I want i to tell how many pdf files there is in the newly created directory 
print(f"Found {pdfcount} " + args.FILETYPE + " files in the INPUT directory.")
print(f"Found {endcount} " + args.FILETYPE + " files in the OUTPUT directory.")
