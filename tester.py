### This project is built for compatibilty with Python 3.4 (tested and built using python 3.4.3) ###

from baby_steps.extractLinks import get_all_links
import requests
from crawler import crawl_web

def test_link_extraction():
    url = "https://www.udacity.com/cs101x/index.html"
    response = requests.get(url)
    print(response.content)
    links = get_all_links(response.content.decode('UTF-8'))
    print(links)

def test_requests():
    url = "https://blockchain.info/address/155VGwiUkDoMWmZYE5FuuuqkppS6tf5SNr"
    response = requests.get(url)
    print(response.content)

def test_crawler():
	crawled = crawl_web("https://www.udacity.com/cs101x/index.html")
	print(crawled)

#test_link_extraction()
#test_requests()
test_crawler()