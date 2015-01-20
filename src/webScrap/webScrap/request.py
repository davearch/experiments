import sys
import re
import os
import urlparse
import Queue

from bs4 import BeautifulSoup
from urllib2 import urlopen
from random import randint

import webScrap
from urlorder import URLOrder
from webScrap import utils

class Request(object):

    def __init__(self, URLOrder, webScrap):
        self.queue = Queue.Queue()
        self.queue.put(URLOrder)
        self.collection = []
        self.webScrap = webScrap

    def iterateQueue(self):
        while True:
            order = self.queue.get()
            do_work(order)
            self.queue.task_done()

    def do_work(order):
        raise NotImplementedError #override this in subclasses

class httpRequest(Request):
    def __init__(self, URLOrder, webScrap):
        super(httpRequest, self).__init__(URLOrder, webScrap)

    def do_work(self, order):
        try:
            soup = makeSoup(order.url)
            p = parseRequest(order, self.webScrap, soup)
            self.collection.append(p.parsedLinks)
        except ValueError:
            print "Value Error on Soup parse"
            print "manually grepping html..."
            html = makeHTML(order.url)
            p = parseRequest(order, self.webScrap, html)
            self.collection.append(p.parsedLinks)
        else:
            raise

    def makeHTML(url):
        try:
            tmp_file = self.tmp_dir + str(randint(randrange(1, 200)))
        except:
            raise
        response = urlopen(url)
        htmlFile = open(tmp_file, "w")
        htmlFile.write(response.read())
        htmlFile.close()
        return htmlFile

    def makeSoup(url):
        soup = urlopen(url).read()
        return BeautifulSoup(html, "lxml")

class parseRequest(Request):
    def __init__(self, URLOrder, webScrap, htmlSoup):
        super(parseRequest, self).__init__(URLOrder, webScrap)
        self.htmlSoup = htmlSoup

    def do_work(self, order):
        parseRouter(self.htmlSoup)

    def parseRouter(self, htmlSoup):
        if isinstance(htmlSoup, bs4.BeautifulSoup):
            parseSoup(htmlSoup)
        elif isinstance(htmlSoup, str):
            parseHTML(htmlSoup)
        else:
            raise ValueError('order not a soup or string')

    def parseSoup(self, htmlSoup):
        tag = self.URLOrder.tag
        sep = utils.seperate(tag)
        tagBase = utils.get_first(utils.seperate(tag))
        try:
            if self.URLOrder.classn:
                sub = [htmlSoup.find(tag, self.URLOrder.classn)]
            else:
                sub = [tag for tagBase in htmlSoup.findAll(tag)]
            if sub:
                removeUnwanted(sub)
                return sub
            else:
                raise ValueError("soup not parsable")
        except:
            raise

    def parseHTML(self, htmlSoup):
        imLinks = []
        for line in htmlSoup:
            line = line.rstrip()
            x = re.findall('src="([^"]*)"', line)
            removeUnwanted(x)
            if len(x) > 0:
                imLinks.append(x)
        return imLinks

    def removeUnwanted(self, listOfLinks):
        for item in self.URLOrder.ignore:
            try:
                listOfLinks.remove(item)
            except ValueError:
                pass
            except AttributeError:
                pass
            
