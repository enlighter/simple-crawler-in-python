from baby_steps.extractLinks import get_all_links
import requests

url = "https://www.udacity.com/cs101x/index.html"
response = requests.get(url)
links = get_all_links(response.content.decode('UTF-8'))
print(links)