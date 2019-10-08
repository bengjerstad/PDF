from PyPDF2 import PdfFileWriter, PdfFileReader
import os

input=[]
splitpages = 4

files = os.listdir('infiles')
for file in files:
	input = PdfFileReader(open("infiles/"+file, "rb"))
	for idx,x in enumerate(input.pages):
		mod = idx % splitpages
		#print(idx,mod)
		if mod == 0:
			output = PdfFileWriter()
			output.addPage(input.getPage(idx))
		else:
			output.addPage(input.getPage(idx))
		if mod == splitpages - 1:
			outputStream = open("outfiles/"+file.split(".")[0]+" ("+str(idx+1)+").pdf","wb")
			output.write(outputStream)
			
