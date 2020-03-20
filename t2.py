import requests
from bs4 import BeautifulSoup

url = "https://www.akc.org/dog-breeds/airedale-terrier/"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
span = soup.findAll("span", {"class": "attribute-list__description"})
print(span[5].text)
