import sys
import re

from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_basin_links(treeflowURL):
    """getSubdirectories"""
    soup = make_soup(treeflowURL)
    sub = soup.find("li", "sub")
    basin_links = [li.a["href"] for li in sub.findAll("li")]
    return basin_links

def get_reconstruction_links(basinURL):
    """getSubdirectories"""
    soup = make_soup(basinURL)
    reconstructionLinks = [area["href"] for area in soup.findAll("area")]
    if not reconstructionLinks:
        print basinURL + "is non-parsable"
    return reconstructionLinks

def manipulate_links(reconLinks):
    """utils"""
    newLinks = []
    for recon in reconLinks:
        for b in BAD:
            if [i for i in b if i in BAD]:
                print i
    return newLinks

def grepImageLinks(file):
    """grepSrc parse.py"""
    imLinks = []
    fh = open(file)
    for line in fh:
        line = line.rstrip()
        x = re.findall('src="([^"]*)"', line)
        if [i for i in x if i in DONT_WANT]:
            x.remove(i)
        elif len(x) > 0:
            imLinks.append(x)
    return imLinks

def extractRecon(basin):
    """utils"""
    sep = '/'
    link = basin[21:]
    newBasin = link.split(sep, 1)[0]
    return newBasin

def curlFile(url, name):
    """parse.py"""
    file = '/tmp/' + url
    print "curling to " + name
    try:
        response = urlopen(url)
        fh = open(file, "w")
        fh.write(response.read())
        fh.close()
    except:
        print url
        raise

def index_containing_substr(theList, substr):
    """utils"""
    for i, s in enumerate(theList):
        if substr in s:
            print i
            return i
    return -1

def main(args=sys.argv):
    try:
        if any("http" in arg for arg in args):
            url = args[index_containing_substr(args, "http")]
            print url
            basins = get_basin_links(url)
            for basin in basins:
                print '*** BASIN: ' + basin
                # e.g.: upco
                reconAlone = extractRecon(basin)
                # unfiltered links. e.g., ../basin.html
                recons = get_reconstruction_links(basin)
                # links without basin subdirectory e.g., treeflow.info/blah.html
                # instead of treeflow.info/upco/blah.html
                newList = manipulate_links(recons)
                count = 0
                imageLinks = []
                for item in newList:
                    newItem = item[:24] + '/' + reconAlone + item[24:]
                    file = '/tmp/' + reconAlone + str(count)
                    url = newItem
                    try:
                        response = urlopen(url)
                        # open the file for writing
                        fh = open (file, "w")
                        fh.write(response.read())
                        fh.close()
                        images = grepImageLinks(file)
                        imageLinks.append(images)
                        count += 1
                    except:
                        print '*** INCORRECT URL:' + url
        else:
            print "args = " + str(args).strip()
    except:
        print "args = " + str(args).strip()
        raise
        return 0
