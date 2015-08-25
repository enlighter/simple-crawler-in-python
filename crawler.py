### This project is built for compatibilty with Python 3.4 (tested and built using python 3.4.3) ###
from baby_steps.extractLinks import get_all_links
import requests

def crawl_web(seed_page):
    tocrawl = []
    crawled = []
    tocrawl.append(seed_page)

    while tocrawl:
        dest = tocrawl.pop()
        if dest not in crawled:
            current_page = requests.get(dest)
            links_extracted = get_all_links(current_page.content.decode('UTF-8'))
            tocrawl.extend(links_extracted)
            crawled.append(dest)
        else:
            continue

    return crawled