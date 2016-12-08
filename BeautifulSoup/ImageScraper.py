import requests

import random

import urllib.request

import validators 

from bs4 import BeautifulSoup

# url = "http://www.facets.la/"

req = urllib.request.urlopen(url)

soup = BeautifulSoup(req, "html.parser")


def image_downloader(url):
    # next goal is to generate a random name for the image to be downloaded
    # random no in range 1,1000 is generated with given upper and lower limits
    number = random.randrange(1, 1000)
    file_name = str(number) + ".jpg"

    # next one is to retreive the image from the scraped website
    if(validators.url(url)): # validators help to parse the url to get only valid ones
       print("Downloading....",url)
       urllib.request.urlretrieve(url, file_name)

for each_link in soup.find_all('img'):
	image_downloader(each_link.get('src'))
