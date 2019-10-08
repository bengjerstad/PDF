from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import re

output = PdfFileWriter()
input=[]

def natural_key(string_):
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

files = os.listdir('infiles')
files.sort(key=natural_key)

for file in files:
	input = PdfFileReader(open("infiles/"+file, "rb"))
	for idx,x in enumerate(input.pages):
			output.addPage(input.getPage(idx))
			
outputStream = open("outfiles/"+files[0].split(".")[0]+".pdf", "wb")
output.write(outputStream)