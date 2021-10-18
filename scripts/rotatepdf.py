#!/usr/bin/env python3
import argparse
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir

# Argument parser. Makes the script take command line inputs
parser = argparse.ArgumentParser(description=''' A program capable of rotating PDF files.
                    If you have a single PDF, that you want to rotate 
                    you specify the path to the file as INPUT. The program cannot overwrite the original file.
                    You need to specify a new output pdf. WARNING: IF YOU TRY TO RUN THE PROGRAM WITH INPUT AND OUTPUT AS THE SAME FILE,
                    YOU WILL ERASE THE ORIGINAL FILE! 
                    ''')
parser.add_argument("INPUT", help="Your input file, remember the .pdf ending. If batch processing provide path to folder.")
parser.add_argument("OUTPUT", help="Your output file, remember the .pdf ending. If batch processing provide path to folder.")
parser.add_argument("VALUE", type=int, help="Enter how many degrees the file should be turned clockwise (90, 180 or 270)" )
parser.add_argument("-b", "--batch", action="store_true", help='''Use this argument to process multiple files. 
                    If you are using this argument you have to specify where the files are located.
                    This changes how the INPUT and OUTPUT arguments work. When batch processing the INPUT
                    and OUTPUT arguments takes folders and not individual files.
                    ''')
args = parser.parse_args()

### TODO: Make the program check if INPUT and OUTPUT is the same. If yes, then quit program

# Makes the user choose how the files should be turned from the VALUE argument
value = args.VALUE
# Check if VALUE input is valid
if value != 90 and value != 180 and value != 270:
    print("ERROR: You have to specify the VALUE as either 90, 180 or 270.")
    exit()

#Turns all pdf files in the INPUT folder, if --batch/-b is used
if args.batch:
    input_dir = args.INPUT
    output_dir = args.OUTPUT

    # Check whether the specified path exists or not
    isExist = os.path.exists(output_dir)
    if not isExist:
    # Create a new directory because it does not exist 
     os.makedirs(output_dir)

    for x in listdir(input_dir):
        if not x.endswith('.pdf'):
            continue
        pdf_in = open(input_dir + "/" + x, 'rb')
        pdf_reader = PdfFileReader(pdf_in, strict=False)
        pdf_writer = PdfFileWriter()
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            page.rotateClockwise(value)
            pdf_writer.addPage(page)
        pdf_out = open(output_dir + "/" + x, 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()
    
    print("Your files have been succesfully rotated")

# Turns the INPUT pdf file and saves it as OUTPUT argumentname.
else:
    pdf_in = open(args.INPUT, 'rb')
    pdf_reader = PdfFileReader(pdf_in, strict=False)
    pdf_writer = PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(value)
        pdf_writer.addPage(page)
    pdf_out = open(args.OUTPUT, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()

    print("Your file has been succesfully rotated")