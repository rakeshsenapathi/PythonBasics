from bs4 import BeautifulSoup

import urllib.request as urlRequest

url = "http://www.hdwallpapers.in/"

# headers = {'User-Agent': 'Mozilla/5.0'}

req = urlRequest.Request(url)

html_content = urlRequest.urlopen(req)

soup = BeautifulSoup(html_content.read(),"html.parser") 

wallpapers = soup.find_all('div',class_="thumbbg")

print(soup.prettify)

