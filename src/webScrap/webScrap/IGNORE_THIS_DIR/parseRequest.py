import sys
import re
import os
import Queue

from bs4 import BeautifulSoup
from urllib2 import urlopen

from .webScrap import webScrap
from .webScrap import URLOrder
from .webScrap import httpRequest

class ParseRequest(object):

    parseQueue = Queue.Queue()

    def __init__(self, URLOrder):
        parseQueue.put(URLOrder)

    def parseRouter(URLOrder):
        pass

    def parseSoup(URLOrder):
        pass

    def parseHTML(URLOrder):
        pass

    def iterateQueue():
        pass
