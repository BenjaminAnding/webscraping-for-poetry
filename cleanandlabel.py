import os, sys, glob, re, string

files = glob.iglob('./authors/*')
iterator = 0
for file in files:
	with open('labels.txt', 'a') as labels:
		labels.write(file.replace('./authors/', '')+':'+str(iterator)+'\n')
	subfiles = glob.iglob(file+'/*')
	for subfile in subfiles:
		with open(file+'/combined.txt', 'a') as combined:
			with open(subfile, 'r') as readfile:
				originalarray = readfile.readlines()
				translatearray = [] 
				for line in originalarray:
					translatearray.append(line.translate(str.maketrans('','',string.punctuation)).translate(str.maketrans('','','1234567890')).lower())
				for line in translatearray:
					combined.write(line)
			print("done with "+subfile)
	print("done with "+file)
	with open(file+'/label.txt', 'w') as label:
		label.write(str(iterator))
	iterator+=1
