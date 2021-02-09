#Script that renames a lot of files with the same ending and keeps the order of the files.

import os
path = 'path to files' #Here you insert the path to the files. Remember to end with a /
files = os.listdir(path)
for file in files:
   #Here you tell the computer what to rename the files. Add name in name_of_files and ending in .ending REMEMBER to keep the dot.
   os.rename(os.path.join(path, file), os.path.join(path, 'name_of_files' + file + '.endning')) 