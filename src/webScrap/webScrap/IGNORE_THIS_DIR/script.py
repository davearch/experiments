import webScrap

if name == '__main__':
    base      = webScrap(BASE_URL, DEF_DIR)
    baseOrder = URLOrder(BASE_URL, "a[href]", ".menu")
    httpreque = HTTPRequest(baseOrder, base)
    firstMenu = httpreque.getLinks()
    nOrder    = URLOrder(firstMenu, "area[href]")
    nhttprequ = HTTPRequest(nOrder, base)
    subpages  = nhttprequ.getLinks()
    dontwant  = [""]
    imgOrder  = URLOrder(subpages, "img[src]", dontwant)
    newhttpre = HTTPRequest(imgOrder, base)
    imgLinks  = newhttpre.getLinks()
    base.curlLinks()
    base.tarDirectory()
