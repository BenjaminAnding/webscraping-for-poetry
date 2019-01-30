from bs4 import BeautifulSoup
import urllib
import os
import sys


baseurl = 'https://www.bartleby.com'
response = urllib.urlopen('https://www.bartleby.com/101/index1a.html')
raw_html = response.read()
html = BeautifulSoup(raw_html, 'lxml')
for i, a in enumerate(html.select('a')):
	#print(i, a.text)
	i = a
authors =[]
poems = []
urls = []
for i, table in enumerate(html.select('table')):
	if i==6:
		for td in table.select('td[rowspan]'):
			for i in range(int(td['rowspan'])):
				authors.append(td.text)
		for a in table.select('a[href]'):
			poems.append(a.text)
			urls.append(baseurl+a['href'])

#print(authors)
#print(poems)
print(len(authors), len(poems))
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

for author in authors:
	try:
		os.mkdir("authors/"+author)
	except:
		print("File exists")

for i in range(len(authors)):
	poem = fetch(urls[i])
	with open("authors/"+authors[i]+"/"+poems[i].encode('ascii','ignore'), 'wb') as poemfile:
		poemfile.write(poem[0].encode('ascii','ignore'))
