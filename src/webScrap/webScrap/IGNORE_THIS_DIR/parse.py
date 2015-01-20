import sys
import re

from bs4 import BeautifulSoup
from urllib2 import urlopen

class Parse(object):

    foundLinks      = []
    imgSrcs         = []
    DownLoadedFiles = []
    
    def __init__(self, urls):
        self.urls = urls

    def getSubdirectories(urls):
        """Return a list of links from the page(s)."""
        pass

    def make_soup(url):
        """Return Soup Object containing parsable HTML."""
        html = urlopen(url).read()
        return BeautifulSoup(html, "lxml")
