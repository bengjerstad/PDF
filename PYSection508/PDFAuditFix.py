from pdfrw import PdfObject, PdfReader, PdfWriter
import os

defaultlang = 'en-US'

#read all files in the folder called 'files'
files = os.listdir('files')
for file in files:
	print(file)
	fixlist = []
	trailer = PdfReader('files\\'+file)
	print("Lang: ",trailer.Root.Lang)
	if trailer.Root.Lang == None:
		fixlist.append('Lang')
	print("Title: ",trailer.Info.Title)
	if trailer.Info.Title == None:
		fixlist.append('Title')
	print(trailer.Root.MarkInfo)
	if trailer.Root.MarkInfo == None:
		fixlist.append('MarkInfo')
	print('')
	print('Found issues with these:')
	print(fixlist)
	tofix = input('Do you want to fix all of these issues? y or n')
	if tofix == 'y' or tofix == 'Y':
		print('Fixing this:')
		for fix in fixlist:
			print(fix)
			if fix == 'Lang':
				trailer.Root.Lang = defaultlang
			if fix == 'Title':
				totitle = input('Do you want the title to be: '+file.split(".")[0]) 
				if totitle == 'y' or totitle == 'Y':
					title = file.split(".")[0]
				else:
					title = input('What does the title need to be?') 
				trailer.Info.Title = title
			if fix == 'MarkInfo':
				trailer.Root.MarkInfo = PdfObject('<</Marked true>>')
		#commit the changes
		PdfWriter('out\\'+file, trailer=trailer).write()
		
	tofix = input('Do you want to fix anything else in this file? y or n')
	
