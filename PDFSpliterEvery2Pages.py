from PyPDF2 import PdfFileWriter, PdfFileReader
import os

input=[]

files = os.listdir('infiles')
for file in files:
	input = PdfFileReader(open("infiles/"+file, "rb"))
	for idx,x in enumerate(input.pages):
		if (idx % 2) == 0:
			output = PdfFileWriter()
			output.addPage(input.getPage(idx))

		else:
			output.addPage(input.getPage(idx))
			outputStream = open("outfiles/"+file.split(".")[0]+" ("+str(idx+1)+").pdf","wb")
			output.write(outputStream)