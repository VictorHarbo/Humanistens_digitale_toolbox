# Commandline cheat sheet
We all know how to operate computers through graphical interfaces such as Windows or MacOS. We can open folders by clicking on them and copy files between folders. We use the mouse på point and click to open programs and files. This is what most of us consider the normal way to operate a computer.  

But there is another way: the command line. In these environment you don't operate the computer by clicking around graphical user interfaces - instead you operate the computer via written commands. You can navigate around your folders and even run programs that is operated from the command line. In this little cheatsheet we show just a few of the simple commands to be used on the command line. Command lines offers a wide variety of functionality and if you venture on beyond this little cheatsheet you will find a world of powerfull commmands. But be aware - command lines doesn't usually ask "Are you sure you want to delete these files?" - on the other hand it doesn't do anything on less you've asked it to do it. This is just to say: make sure you're certain what your command does before giving the command - or if you are testing a command make sure to do it on backed up material. 

# Usefull commands
Mac-users will find their commandline in the program called "Terminal", while Windows users will find it in the program called "PowerShell". Below you will see an explanation of all commands and in the grey boxes you will see an example on how to use the command on the command line. 

## Where am I? pwd - Print Working Directory
When opening a command line thing might look scary - First thing is to realise where on your computer the command line is right now - this is comparable to when you open FileExplorer or Finder it will have a default place where it starts - eg Documents. Using the command *pwd* you command the line to tell you where you are:  
```
pwd
```
## How do change the working directory? cd - Change Directory
We know where we are, but how do we navigate to the folder where we are interesting in working? The answers is the command *cd* followed by the path to a directory:  
```
cd /Users/YourUsername/Desktop
```
Above command will change the directory to the users desktop.  
A good thing to remember is that command lines normally doesn't agree with space in either filenames or foldernames. If your commands are acting up it could very well be that you have a folder name or a filname that contain a space.  

When you have changed into a folder and you want to change into a folder within that folder (E.g. you have navigated to the desktop and now you want to change directory into the folder "Pictures", which you have on your desktop) you dont have to give *cd* the entire path:
```
cd Pictures
```
*cd* only needs the name of a folder - if that folder is located within the current working directory.  

But how do we return to the desktop again? We could use the full path as above, but there is a short cut:
```
cd ..
```
This will take you to the folder above the one you're at. It help to think of your folders and files as a structered three folders are alway located within folders (until you reach the root) and this function will take you to the parent folder of the one you're currently at. 
## What is in this folder? ls - list files
So we have succesfully changed our working directory to the folder we want to work in - but how can we see what is in the folder? Here we use *ls* which will return the names of the files and folders in your current working directory.
```
ls
```

Is the output somewhat chaotic? Use the flag *-l* to order the output as a single column list:

```
ls -l
```
## How to create a folder? mkdir - make directory
Let's say that we want to create a new folder in our working directory. For that purpose we use the command *mkdir* and the name for our new folder:
```
mkdir new_folder_name
```
This will create a new folder with the name "new_folder_name" 
## How to copy files? cp - copy
If we want to copy a file within the same directory, we do this with the command *cd*:  
```
cp name_of_a_file.pdf copy_of_a_file.pdf
```
This will create a copy of the file "name_of_a_file.pdf" with the new filename "copy_of_a_file.pdf" 