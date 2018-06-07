from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pathlib import Path
import requests

count = 1
page = 1

while count <= 300:

    frontUrl = "https://www.olx.com.br/moveis/sofas-e-poltronas?o=" + str(page)
    frontPage = BeautifulSoup(urlopen(Request(frontUrl, headers={'User-Agent': 'Mozilla/5.0'})), "lxml")

    for link in (frontPage.find_all("a", {"class":"OLXad-list-link"})):
        productPage = BeautifulSoup(urlopen(Request(link["href"], headers={'User-Agent': 'Mozilla/5.0'})), "lxml")
        listaImagens = productPage.find_all("div", {"class":"box-image"})
        listaImagens.pop(0)
        for div in listaImagens:
            img = div.a
            directory = str(Path.home()) + "/ImagesCrawled/OLX/Sofa/"
            Path(directory).mkdir(parents=True, exist_ok=True)
            with open(directory + str(count) + ".jpg", 'wb') as outfile:
                outfile.write(requests.get(img["href"]).content)
                print(str(count) + ".jpg")
            count += 1

        page += 1
