import sys
import re
import os
import Queue

from bs4 import BeautifulSoup
from urllib2 import urlopen

from .webScrap import URLOrder
from .webScrap import webScrap

class httpRequest(object):

    linksQueue = Queue.Queue()

    def __init__(self, URLOrder):
        linksQueue.put(URLOrder)
        self.linksCollected = []

    def makeSoup(URLOrder):
        html = urlopen(url).read()
        return BeautifulSoup(html, "lxml")

    def requestHTML(URLOrder):
        pass

    def isSoupValid(soup):
        return True

    def iterateQueue():
        pass
