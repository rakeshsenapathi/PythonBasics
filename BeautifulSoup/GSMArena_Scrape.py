# Scraping home page of GSMArena to find the list of all phone brands

import requests

from bs4 import BeautifulSoup

url = "http://www.gsmarena.com/" #base url

req = requests.get(url)

# status_code=200 represents OK
if(req.status_code != 200):
	print(req.status_code)

soup = BeautifulSoup(req.content, "html.parser")

lists = soup.find('div', class_="brandmenu-v2 light l-box clearfix")

phone_list = lists.find_all('li')

for each_phone in phone_list:
	print(each_phone.text)





