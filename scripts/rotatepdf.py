#!/usr/bin/env python3

import PyPDF2

pdfIn = open('Gade-udstillingsanalyse2006.pdf', 'rb') # exchange the 'original.pdf' with a name of your file 
pdfReader = PyPDF2.PdfFileReader(pdfIn)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    page = pdfReader.getPage(pageNum)
    page.rotateClockwise(90)
    pdfWriter.addPage(page)

pdfOut = open('Gade-udstillingsanalyse2006rotated.pdf', 'wb')
pdfWriter.write(pdfOut)
pdfOut.close()
pdfIn.close()