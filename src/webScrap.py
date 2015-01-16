from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
import re
import sys

BASE_URL = "http://www.treeflow.info"
BAD      = ['#', '../']
BASINS   = ['upco',   'loco', 
            'riogr',  'ark', 
            'platte', 'upmo', 
            'cali',   'pnw', 
            'grba',   'midatl']

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_basin_links(treeflowURL):
    soup = make_soup(treeflowURL)
    sub = soup.find("li", "sub")
    basin_links = [li.a["href"] for li in sub.findAll("li")]
    return basin_links

def get_reconstruction_links(basinURL):
    soup = make_soup(basinURL)
    reconstructionLinks = [area["href"] for area in soup.findAll("area")]
#    print reconstructionLinks
    return reconstructionLinks

def manipulate_links(reconLinks):
    bad = ['#', '../', 'upco', 'loco', 'riogr',
           'ark', 'platte', 'upmo', 'cali', 'pnw',
           'grba', 'midatl']
    newLinks = []
    for recon in reconLinks:
#        if any(x in recon for x in bad):
#            print recon.split(x,1)
        for b in bad:
#            if b in  recon:
#                newb = recon.split(b,1)
#                print newb[1]
            if [i for i in b if i in bad]:
                print ''
#    if '#' in reconLinks:
#        reconLinks.remove('#')
#    for recon in reconLinks:
#        if '../' in recon:
#            recon = recon[3:]
#        recon = BASE_URL + '/' + recon
#        newLinks.append(recon)
    return newLinks

### cant get to work
#def download_images(reconLink):
#    try:
#        soup = make_soup(reconLink)
#        for div in soup.find_all('div'):
#            print div
#    except:
#        print 'INCORRECT URL:' + reconLink + '\n'
###

def grepImageLinks(file):
    imLinks = []
    dontWant = ['http://treeflow.info/images/wwa_logo.jpg', 
                'http://treeflow.info/images/University-of-Colorado.jpg', 
                'http://treeflow.info/images/climas.png', 
                'http://treeflow.info/images/arizonalogo.gif']
    fh = open(file)
    for line in fh:
        line = line.rstrip()
        x = re.findall('src="([^"]*)"', line)
        if [i for i in x if i in dontWant]:
            x.remove(i)
        elif len(x) > 0:
            imLinks.append(x)
    return imLinks
###

def extractRecon(basin):
    sep = '/'
    link = basin[21:]
    newBasin = link.split(sep, 1)[0]
    return newBasin


if __name__ == '__main__':
    basins = get_basin_links(BASE_URL)
    for basin in basins:
        print '*** BASIN: ' + basin
        # e.g.: upco
        reconAlone = extractRecon(basin)
        # unfiltered links. e.g., ../basin.html
        recons = get_reconstruction_links(basin)
        for recon in recons:
            print recon
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
#            imgs = download_images(newItem)
