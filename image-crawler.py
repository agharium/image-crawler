from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pathlib import Path
import requests

count = 1
limit = 48
offset = 0
root = "https://www.americanas.com.br"

while count <= 300:

    frontUrl = "https://www.americanas.com.br/categoria/moveis/sofa?limite=" + str(limit) + "&offset=" + str(offset)
    frontPage = BeautifulSoup(urlopen(Request(frontUrl, headers={'User-Agent': 'Mozilla/5.0'})), "lxml")

    for link in (frontPage.find_all("a", {"class":"card-product-url"})):
        productPage = BeautifulSoup(urlopen(Request(root + link["href"], headers={'User-Agent': 'Mozilla/5.0'})), "lxml")
        for div in (productPage.find_all("div", {"class":"gallery-product swiper-wrapper"})):
            img = div.figure.a.img
            directory = str(Path.home()) + "/ImagesCrawled/Sofa/"
            Path(directory).mkdir(parents=True, exist_ok=True)
            with open(directory + str(count) + ".jpg", 'wb') as outfile:
                outfile.write(requests.get(img["src"]).content)
                print(str(count) + ".jpg")
            count += 1

    offset = limit
    limit += 48
