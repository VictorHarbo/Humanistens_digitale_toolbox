#!/usr/bin/env python3
import argparse
from PyPDF2 import PdfFileWriter,PdfFileReader,PdfFileMerger

# TODO: Update descriptions and argument help to match this program

# Makes the program take commandline inputs
parser = argparse.ArgumentParser(description= '''A program, that crops pdf-files. The standard output is cropped on the middle. It can crop at a selected value with the -m flag.''')
parser.add_argument("INPUT", help="The path to your input pdf file.")
parser.add_argument("OUTPUT", help="The path to your output pdf file. It is always a good idea to make the output something else than the input.")
parser.add_argument("-m", "--manual", action="store_true", help='''Use this argument to change the crop value,
                    if the pages doesn't fit. A number lower than the middle coordinate will crop the page 
                    further to the left and a number higher than the middle coordinate will crop the page 
                    furhter to the right. This is a prosess of trial and error.
                    ''')
args = parser.parse_args()

# Save the CLI inputs to variables
INPUT = args.INPUT
OUTPUT = args.OUTPUT

# TODO: Add print statement, that tells that the crop has been done succesfully 
# TODO: User-input, that applies to grouped coordinates
# or 
# TODO: Make it possible to move middle by percentage or +/- 10 pixels
 
# Manually assigning where to crop the page in CLI
if args.manual:
    with open(INPUT, "rb") as in_f:
        input1 = PdfFileReader(in_f)
        input2 = PdfFileReader(in_f)
        output = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            ### Create left page ###
            L_page = input1.getPage(i)

            # Scales the page to A3
            L_page.scaleTo(420,297)
            
            # Save the coordinates of the PDF corners:
            L_LowerLeft = L_page.cropBox.getLowerLeft()
            L_LowerRight = L_page.cropBox.getLowerRight()
            L_UpperLeft = L_page.cropBox.getUpperLeft()
            L_UpperRight = L_page.cropBox.getUpperRight()

            # Breaks coordinates into integers
            # and creates the middle X coord:
            L_Top_X_coord = L_UpperRight[0]
            L_Bot_X_coord = L_LowerLeft[0]
            L_Top_Y_coord = L_UpperRight[1]
            L_Bot_Y_coord = L_LowerLeft[1] 
            L_middle_X_coord = L_Top_X_coord / 2

            # Takes the user-input coordinate:
            print("The middle of the INPUT file is located at this coordinate: ", L_middle_X_coord)
            print("At what coordinate do you want to crop the pages? \n(A lower coordinate crops the pages further to the left and a heigher coordinate crops further to the right) ")
            manual_coord = input("Your coordinate: ")
        
            # Adds left page to output:
            L_page.trimBox.lowerLeft = (0, 0)
            L_page.trimBox.upperRight = (manual_coord, L_Top_Y_coord)
            L_page.cropBox.lowerLeft = (0, 0)
            L_page.cropBox.upperRight = (manual_coord, L_Top_Y_coord)
            output.addPage(L_page)

            ### Create right page ###
            R_page = input2.getPage(i)

            # Scales the page to A3
            R_page.scaleTo(420,297)

            # Save the coordinates of the PDF corners
            R_LowerLeft = R_page.cropBox.getLowerLeft()
            R_LowerRight = R_page.cropBox.getLowerRight()
            R_UpperLeft = R_page.cropBox.getUpperLeft()
            R_UpperRight = R_page.cropBox.getUpperRight()

            # Breaks coordinates into integers
            # and creates the middle X coord
            R_Top_X_coord = R_UpperRight[0]
            R_Bot_X_coord = R_LowerLeft[0]
            R_Top_Y_coord = R_UpperRight[1]
            R_Bot_Y_coord = R_LowerLeft[1] 
            R_middle_X_coord = R_Top_X_coord / 2

            # Adds right page to output
            R_page.trimBox.lowerLeft = (manual_coord, R_Bot_Y_coord)
            R_page.trimBox.upperRight = (R_Top_X_coord, R_Top_Y_coord)
            R_page.cropBox.lowerLeft = (manual_coord, R_Bot_Y_coord)
            R_page.cropBox.upperRight = (R_Top_X_coord, R_Top_Y_coord)
            output.addPage(R_page)

        with open(OUTPUT, "wb") as out_f:
            output.write(out_f)
        
    print("Your PDF file has been cropped. You can find it at this location: " + OUTPUT)

# Crops page at the middle coordinate
else:
    with open(INPUT, "rb") as in_f:
        input1 = PdfFileReader(in_f)
        input2 = PdfFileReader(in_f)
        output = PdfFileWriter()

        numPages = input1.getNumPages()

        for i in range(numPages):
            # Create left page
            L_page = input1.getPage(i)

            # Scales the page to A3
            L_page.scaleTo(420,297)

            # Save the coordinates of the PDF corners
            L_LowerLeft = L_page.cropBox.getLowerLeft()
            L_LowerRight = L_page.cropBox.getLowerRight()
            L_UpperLeft = L_page.cropBox.getUpperLeft()
            L_UpperRight = L_page.cropBox.getUpperRight()

            # Breaks coordinates into integers
            # and creates the middle X coord
            L_Top_X_coord = L_UpperRight[0]
            L_Bot_X_coord = L_LowerLeft[0]
            L_Top_Y_coord = L_UpperRight[1]
            L_Bot_Y_coord = L_LowerLeft[1] 
            L_middle_X_coord = L_Top_X_coord / 2

            # Adds left page to output
            L_page.trimBox.lowerLeft = (0, 0)
            L_page.trimBox.upperRight = (L_middle_X_coord, L_Top_Y_coord)
            L_page.cropBox.lowerLeft = (0, 0)
            L_page.cropBox.upperRight = (L_middle_X_coord, L_Top_Y_coord)
            output.addPage(L_page)

            # Create right page
            R_page = input2.getPage(i)

            # Scales the page to A3
            R_page.scaleTo(420,297)

            # Save the coordinates of the PDF corners
            R_LowerLeft = R_page.cropBox.getLowerLeft()
            R_LowerRight = R_page.cropBox.getLowerRight()
            R_UpperLeft = R_page.cropBox.getUpperLeft()
            R_UpperRight = R_page.cropBox.getUpperRight()

            # Breaks coordinates into integers
            # and creates the middle X coord
            R_Top_X_coord = R_UpperRight[0]
            R_Bot_X_coord = R_LowerLeft[0]
            R_Top_Y_coord = R_UpperRight[1]
            R_Bot_Y_coord = R_LowerLeft[1] 
            R_middle_X_coord = R_Top_X_coord / 2

            # Adds right page to output
            R_page.trimBox.lowerLeft = (R_middle_X_coord, R_Bot_Y_coord)
            R_page.trimBox.upperRight = (R_Top_X_coord, R_Top_Y_coord)
            R_page.cropBox.lowerLeft = (R_middle_X_coord, R_Bot_Y_coord)
            R_page.cropBox.upperRight = (R_Top_X_coord, R_Top_Y_coord)
            output.addPage(R_page)

        with open(OUTPUT, "wb") as out_f:
            output.write(out_f)
    
    print("Your PDF has been cropped in the middle. You can find it at this location: " + OUTPUT)

