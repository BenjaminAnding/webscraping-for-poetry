from bs4 import BeautifulSoup
import os, sys
if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen


baseurl = 'https://www.bartleby.com'
response = urlopen('https://www.bartleby.com/273/index1.html')
raw_html = response.read()
html = BeautifulSoup(raw_html, 'lxml')
#for i, table in enumerate(html.select('table')):
#	print(i, table)
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
	response = urlopen(url)
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
	with open("authors/"+authors[i]+"/"+poems[i], 'wb') as poemfile:
            poemfile.write(poem[0].encode('ascii','ignore'))

