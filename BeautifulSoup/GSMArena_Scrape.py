# Scraping home page of GSMArena to find the list of all phone brands

import requests

import webbrowser

import sys

from bs4 import BeautifulSoup

url = "http://www.gsmarena.com/"  # base url

req = requests.get(url)

# status_code=200 represents OK
if(req.status_code != 200):
    print(req.status_code)

soup = BeautifulSoup(req.content, "html.parser")

lists = soup.find('div', class_="brandmenu-v2 light l-box clearfix")

brand_list = lists.find_all('li')
links = lists.find_all('a')

name = input("Enter Mobile brand: ")
for each_link in links:
    if(name == (each_link.text)):
        print("Brand exists....")
        print("Opening url....")
        try:
            webbrowser.open(url + each_link.get('href'))
            sys.exit()
        except Exception as e:
            raise e
    else:
    	continue

print("Brand doesnt exist")
