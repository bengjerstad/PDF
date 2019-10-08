from pdfrw import PdfObject, PdfReader, PdfWriter
import os

files = os.listdir('files')
for file in files:
	trailer = PdfReader('files\\'+file)
	#trailer.Root.MarkInfo.Marked = 'true'
	#trailer.Root.MarkInfo = PdfObject({'/Marked': 'true'})
	trailer.Root.MarkInfo = PdfObject('<</Marked true>>')
	PdfWriter('out\\'+file, trailer=trailer).write()
