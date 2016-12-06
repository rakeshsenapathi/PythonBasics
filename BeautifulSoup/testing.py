import urllib.request  

import webbrowser

import random

from bs4 import BeautifulSoup

def image_downloader(url):
    html_content = urllib.request.urlopen(url) #GETs http request object
    soup = BeautifulSoup(html_content,"html.parser") #html parser is used to extract the html_content

    # next goal is to generate a random name for the image to be downloaded
    number = random.randrange(1,1000) # random no in range 1,1000 is generated with given upper and lower limits
    file_name = str(number) + ".png"

    # next one is to retreive the image from the scraped website
    urllib.request.urlretrieve(url, file_name) 

image_downloader("https://static.xx.fbcdn.net/rsrc.php/v3/yx/r/pyNVUg5EM0j.png")
    






