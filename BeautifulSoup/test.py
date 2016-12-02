from bs4 import BeautifulSoup

import urllib.request as urlRequest

url = "http://www.hdwallpapers.in"

# headers = {'User-Agent': 'Mozilla/5.0'}

req = urlRequest.Request(url)

html_content = urlRequest.urlopen(req)

soup = BeautifulSoup(html_content.read(), "html.parser")

links = soup.find_all('a')

file = open("wallpaper_links.txt","w")

""" # to extract all the urls through anchor tags 
for link in links:
	print ("<a href= '%s' > %s </a>"%(link.get("href"),link.text)) """

image_links = soup.find_all('div', class_="thumb")

for image_link in image_links:
	for each_it in image_link:
		print("Writing:",each_it.text)
		file.write(url+each_it.get("href")+"\n")

file.close()
