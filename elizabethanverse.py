from bs4 import BeautifulSoup
import urllib
import os
import sys
import re


baseurl = 'https://www.bartleby.com'
response = urllib.urlopen('https://www.bartleby.com/331/')
raw_html = response.read()
html = BeautifulSoup(raw_html, 'lxml')
#for i, a in enumerate(html.select('table')):
#	print(i, a)
#	print('\n\n\n\n\n\n\n\n')
authors = []
authors1 = []
poems = []
urls = []


for i, table in enumerate(html.select('table')):
	if i==8:
		for td in table.select('td[rowspan]'):
			for i in range(int(td['rowspan'])):
				authors.append(td.text)
		for a in table.select('a[href]'):
			authors.append(a.findParents('td')[0].text)
			poems.append(a.text)
			urls.append(baseurl+a['href'])

for author in authors:
	author = re.sub(r'.*Anonymous*','Anonymous', author.encode('ascii','ignore'))
	author = re.sub(r'.*by\s','', author.encode('ascii','ignore'))
	authors1.append(author)

#print(authors1)
#print(poems)
print(len(authors1), len(poems))
#print urls

def fetch(url):
	response = urllib.urlopen(url)
	raw_html = response.read()
	html = BeautifulSoup(raw_html, 'html.parser')
	poem = []
	for i, table in enumerate(html.select('table')):
		if i==7:
			for td in table.select('td'):
				poem.append(td.text)
	return poem

for author in authors1:
	try:
		os.mkdir("authors/"+author)
	except:
		print("File exists")

for i in range(len(authors)):
	poem = fetch(urls[i])
	with open("authors/"+authors1[i]+"/"+poems[i].encode('ascii','ignore'), 'wb') as poemfile:
		poemfile.write(poem[0].encode('ascii','ignore'))

