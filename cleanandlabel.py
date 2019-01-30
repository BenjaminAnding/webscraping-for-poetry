import os, sys, glob, re, string

files = glob.iglob('./authors/*')
iterator = 0
for file in files:
	with open('labels.txt', 'ab') as labels:
		labels.write(file.replace('./authors/', '')+':'+str(iterator)+'\n')
	subfiles = glob.iglob(file+'/*')
	for subfile in subfiles:
		with open(file+'/combined.txt', 'ab') as combined:
			with open(subfile, 'r') as readfile:
				originalarray = readfile.readlines()
				translatearray = [] 
				for line in originalarray:
					translatearray.append(line.translate(None, string.punctuation).translate(None, '0123456789').lower())
				for line in translatearray:
					combined.write(line)
			print("done with "+subfile)
	print("done with "+file)
	with open(file+'/label.txt', 'wb') as label:
		label.write(str(iterator))
	iterator+=1
