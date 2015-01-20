import sys
import re
import os

from bs4 import BeautifulSoup
from urllib2 import urlopen

class URLOrder(object):

    def __init__(self, url, tags, classn=None, ignore=None):
        self.url    = url
        self.tags   = tags
        self.classn = classn
        if ignore is None:
            ignore = []
        self.ignore = ignore

    def isValidURL(url):
        return True

    def __getattr__(self, item):
        return self[item]

    
