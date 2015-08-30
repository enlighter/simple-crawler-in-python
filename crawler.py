### This project is built for compatibilty with Python 3.4 (tested and built using python 3.4.3) ###
from baby_steps.extractLinks import get_all_links
import requests


def normalize_link(link):
    bare = link.replace("https://", "http://")

    return bare


def crawl_web(seed_page):
    tocrawl = [seed_page]
    crawled = []
    # debug:
    #print("Initialized : tocrawl = ", tocrawl, "\ncrawled = ", crawled, "\n\n")

    while tocrawl:
        dest = tocrawl.pop(0)
        # popping from the end (tocrawl.pop() or tocrawl.pop(-1) )
        # implements DFS
        # here we're going for a BFS implementation
        dest = normalize_link(dest)
        # debug:
        #print("Next : tocrawl = ", tocrawl, "\ncrawled = ", crawled)
        #print("Will we process ", dest, " : ", (dest not in crawled), "\n\n")
        if dest not in crawled:
            current_page = requests.get(dest)
            links_extracted = get_all_links(current_page.content.decode('UTF-8'))
            tocrawl.extend(links_extracted)
            crawled.append(dest)
            # debug:
            #print("Next : tocrawl = ", tocrawl, "\ncrawled = ", crawled, "\n\n")
        else:
            continue

    return crawled

### test
#print(bare_link("https://www.udacity.com/cs101x/kicking.html"))
