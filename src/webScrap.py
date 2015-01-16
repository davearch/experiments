from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep

BASE_URL = "http://www.treeflow.info"

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
    newLinks = []
    if '#' in reconLinks:
        reconLinks.remove('#')
    for recon in reconLinks:
        if '../' in recon:
            recon = recon[3:]
        recon = BASE_URL + '/' + recon
        newLinks.append(recon)
    return newLinks

def download_images(reconLink):
    soup = make_soup(reconLink)
    trs  = soup.find('td', {"class":"rightcolumn"})
    print trs
    images = [img["src"] for img in trs.findAll("img")]
    print images
#    images = [img["src"] for img in trs.findAll("img")]
#    print images
#    return images

if __name__ == '__main__':
    treeflow = ("http://www.treeflow.info")
    
    basins = get_basin_links(treeflow)
    basinMiddle = []
    for basin in basins:
        sep = '/'
        link = basin[21:]
        newBasin = link.split(sep, 1)[0]
        basinMiddle.append(newBasin)
        recons = get_reconstruction_links(basin)
        newList = manipulate_links(recons)
        for item in newList:
            newItem = item[:24] + '/' + newBasin + item[24:]
            imgs = download_images(newItem)

#        for item in newList:
#            print item
#            imgs = download_images(item)
