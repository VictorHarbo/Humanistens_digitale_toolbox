#!/usr/bin/env python
import os

# Function to rename multiple files with the same filetype at once
def main():
   i = 0
   #Here you input the path to the files
   path="C:/Users/vhole/Pictures/vikingemuseet/" 
   for filename in os.listdir(path):
      #Here you give the output a name. Be carefull with the ending.  
      my_dest ="Vikingemuseum" + str(i) + ".jpg" 
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()
