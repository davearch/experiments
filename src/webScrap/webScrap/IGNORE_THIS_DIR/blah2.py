import sys
import re
import os

from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep

DEFAULT_DIR = os.environ.get(
    'WEBSCRAP_DEFAULT_DIR',
    os.path.expanduser('/tmp/webScrapTmp')
)

class BaseWebScrap(object):

    subpages      = []
    img_srcs      = []
    name          = ""
    url           = ""

    def __getattr__(self, item):
        return self[item]

    def _get_location(self):
        raise NotImplementedError()

    @property
    def location(self):
        path = self._get_location()
        try:
            os.makedirs(os.path.dirname(location), mode=0o700)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        return location

class webScrap(BaseWebScrap):

    subpages = BASINS
    name     = 'treeflow'
    url      = BASE_URL
    
    def __init__(self, directory=DEFAULT_DIR):
        super(Config, self).__init__()
        self.directory = directory

    def _get_location(self):
        return os.path.join(self.directory, self.name + '.txt')

    def tar_images(self):
        pass
