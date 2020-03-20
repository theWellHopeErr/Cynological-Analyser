import requests
from bs4 import BeautifulSoup


def scrapper(url):
    key = ""
    value = ""
    dataScrapped = False
    attributes = dict()

    resp = requests.get(url)
    if resp.status_code == 200:
        print("Successfully opened the web page")

        soup = BeautifulSoup(resp.text, 'html.parser')

        breed = soup.find("h1", {"class": "page-header__title"}).text.strip()
        attributes["breed"] = breed

        desc = soup.find("div", {"class": "breed-hero__footer"}).text.strip()
        attributes["desc"] = desc

        attributes['url'] = url

        lists = soup.find("ul", {"class": "attribute-list"})
        for list_item in lists.findAll("li"):
            for span in list_item.findAll("span"):
                if span.has_attr('class') and span['class'][0] == 'attribute-list__description':
                    value = span.text
                    dataScrapped = True
                elif span.has_attr('class') and span['class'][0] == 'attribute-list__term':
                    key = span.text
                    dataScrapped = True
                else:
                    dataScrapped = False
            if dataScrapped:
                attributes[key[:-1]] = value

        span = soup.findAll("span", {"class": "attribute-list__description"})
        attributes["Group"] = span[5].text
        
        print("************************************************************")
        print("Data scrapped from {}".format(url))
        for k, v in attributes.items():
            print("{}:{}".format(k, v))
        print("************************************************************")
        return attributes
    else:
        print("Error: Cannot load page")
