from bs4 import BeautifulSoup
import os, sys
if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen


baseurl = 'https://www.bartleby.com'
response = urlopen('https://www.bartleby.com/265/index1.html')
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
			if "T. S. Eliot" in td.text:
				authors.append(td.text)
			else:
				if "Gordon Bottomley" in td.text or "Rupert Brooke" in td.text or "Witter Bynner" in td.text or "Adelaide Crapsey" in td.text or "John Gould Fletcher" in td.text or "Wilfrid Wilson Gibson" in td.text or "Horace Holley" in td.text or "Orrick Johns" in td.text or "Amy Lowell" in td.text or "Edgar Lee Masters" in td.text or "Constance Lindsay Skinner" in td.text or "Sara Teasdale" in td.text or "Allen Upward" in td.text:
					for i in range(int(td['rowspan'])-1):
						authors.append(td.text)
				else:
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

