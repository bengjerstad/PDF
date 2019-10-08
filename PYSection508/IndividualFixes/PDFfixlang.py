from pdfrw import PdfReader, PdfWriter
import os

files = os.listdir('files')
for file in files:
	trailer = PdfReader('files\\'+file)
	#print(trailer.Root.Lang)
	trailer.Root.Lang = '(en-US\)'
	PdfWriter('out\\'+file, trailer=trailer).write()
