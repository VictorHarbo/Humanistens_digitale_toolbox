#Script that renames a lot of files with the same ending and keeps the order of the files.
import os
import re
path = '/Users/path/to/files/' # Here you insert the path to the files. Remember to end with a /

# These lines makes sure, that our files keep the same order!
files = os.listdir(path)
files.sort(key=lambda var:[int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])

for i, file in enumerate(files):
   # Here you tell the computer what to rename the files. Add name in name_of_files and ending in .ending REMEMBER to keep the dot.
    os.rename(path + file, path + "name_of_files_{}".format(i)+".ending")  