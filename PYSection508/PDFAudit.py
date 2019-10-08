from pdfrw import PdfReader, PdfWriter
import os

defaultlang = '(en-US)'

#read all files in the folder called 'files'
files = os.listdir('files')
for file in files:
	print(file)
	trailer = PdfReader('files\\'+file)
	print("Lang: ",trailer.Root.Lang)
	print("Title: ",trailer.Info.Title)
	print("MarkInfo: ",trailer.Root.MarkInfo)
	print("")
