import sys
import re
import urlparse

import webScrap
import urlorder
from treeflow import BASE_URL, BAD, BASINS, DONT_WANT

def seperate(string):
    """Seperate strings"""
    stringList = re.findall("\[(.*?)\]", string)
    #print stringList
    return stringList

def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

def index_containing_substr(theList, substr):
    for i, s in enumerate(theList):
        if substr in s:
            return i
    return -1

def main(args=sys.argv[1:]):
    from request import httpRequest
    base = webScrap.webScrap(BASE_URL)
    baseOrder = urlorder.URLOrder(BASE_URL, "a[href]", ".menu")
    httpreque = httpRequest(baseOrder, base)
    firstMenu = httpreque.getLinks()
