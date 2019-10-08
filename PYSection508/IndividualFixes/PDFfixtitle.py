from pdfrw import PdfReader, PdfWriter
import os

title = 'Product Sheet'

files = os.listdir('files')
for file in files:
	trailer = PdfReader('files\\'+file)
	trailer.Info.Title = title
	PdfWriter('out\\'+file, trailer=trailer).write()
