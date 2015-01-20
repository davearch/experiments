import sys
import re
import os

from bs4 import BeautifulSoup
from urllib2 import urlopen

import utils

DEF_DIR = os.environ.get(
    'WEBSCRAP_DEFAULT_DIR',
    os.path.expanduser('/tmp/webScrapTmp')
)

class webScrap(object):
    def __init__(self, url, dlLocation=DEF_DIR):
        self.url = url
        self.dlLocation = dlLocation

    def tarOrder(directory):
        """compress directory into a tar file"""
        pass

    def dlLinks(dlList):
        """recursively download links"""
        pass

    def __getattr__(self, item):
        return self[item]
