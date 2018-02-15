import urllib.request # for working with urls
from bs4 import BeautifulSoup # imports module for parsing html

class Scraper:
    def __init__ (self,site): # will take website provided as parameter
        self.site=site

    def scrape(self):
        r=urllib.request.urlopen(self.site) # requests to sit and returns response w/ html and other data
        html=r.read() # provides html from response object
        parser="html.parser" # somehow parses the html
        sp=BeautifulSoup(html,parser) # ""

        for tag in sp.find_all("a"): # will cause function to find all <a></a> tags with URLs between
            url=tag.get("href") # href variable between <a> and </a> contains url
            if url is None:
                continue
            if "html" in url:
                print("\n"+url)

