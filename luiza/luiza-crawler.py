from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pathlib import Path
import requests

count = 1
innerCount = 1
limitePorProduto = 4
page = 1
root = "https://www.magazineluiza.com.br/"

while count <= 300:

    frontUrl = "https://www.magazineluiza.com.br/sofas/moveis-e-decoracao/s/mo/msof/" + str(page) + "/"
    frontPage = BeautifulSoup(urlopen(Request(frontUrl, headers={'User-Agent': 'Mozilla/5.0'})), "lxml")
    for link in (frontPage.find_all("a", {"class":"product-li"})):
        productPage = BeautifulSoup(urlopen(Request(link["href"], headers={'User-Agent': 'Mozilla/5.0'})), "lxml")

        for img in (productPage.find_all("img", {"class":"js-carousels-main-item-img"})):
            if innerCount == limitePorProduto:
                innerCount = 1
            directory = str(Path.home()) + "/CrawledImages/Magazine Luiza/Sofa/"
            Path(directory).mkdir(parents=True, exist_ok=True)
            with open(directory + str(count) + ".jpg", 'wb') as outfile:
                outfile.write(requests.get(img["src"]).content)
                print(str(count) + ".jpg")
            count += 1
            innerCount += 1
            if innerCount == limitePorProduto:
                break

    page += 1
