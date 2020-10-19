#!/usr/bin/env python3
#The top line is used for calling the script from bash

import PyPDF2 #Imports a module that works wonders on PDF's 

pdfIn = open('Original.pdf', 'rb') # exchange the 'original.pdf' with a name of your file 
pdfReader = PyPDF2.PdfFileReader(pdfIn)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages): #This block of code is applied to all pages in the PDF
    page = pdfReader.getPage(pageNum)
    page.rotateClockwise(-90) #This is where you tell the script how it should rotate the file. -90 turns the pages 90 degrees counterclockwise. 90 turns the PDF 90 degrees clockwise
    pdfWriter.addPage(page)

pdfOut = open('output.pdf', 'wb') #This defines pdfOut as whatever you may have called it
pdfWriter.write(pdfOut) #Writes the turned PDF to pdfOut
pdfOut.close() #Closes the PDF-files
pdfIn.close()
