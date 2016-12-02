import requests

from bs4 import BeautifulSoup

url = "http://www.gsmarena.com/"

req = requests.get(url)

print(req.status_code)

soup = BeautifulSoup(req.content, "html.parser")


lists = soup.find_all('div', class_="brandmenu-v2 light l-box clearfix")

print(type(lists))
for list in lists:
    print(type(list.contents[3]))
