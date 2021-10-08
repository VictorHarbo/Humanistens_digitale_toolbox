#!/usr/bin/env python3
from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
from os import getcwd

cwd = getcwd()
input_dir = "Path/to/files/folder"
output_dir = "Path/to/output/folder"

value = input("Should the file be turned 90, 180 or 270 degress clockwise? ")
value = int(value)

for x in listdir(input_dir):
    if not x.endswith('.pdf'):
        continue
    pdf_in = open(input_dir + x, 'rb')
    pdf_reader = PdfFileReader(pdf_in)
    pdf_writer = PdfFileWriter()
    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(value)
        pdf_writer.addPage(page)
    pdf_out = open(output_dir + x, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()