### This project is built for compatibilty with Python 3.4 (tested and built using python 3.4.3) ###

from baby_steps.extractLinks import get_all_links
import requests

url = "https://www.udacity.com/cs101x/index.html"
response = requests.get(url)
links = get_all_links(response.content.decode('UTF-8'))
print(links)