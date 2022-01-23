import requests
from bs4 import BeautifulSoup

link = "https://www.emiratespostshop.ae"

html_text = requests.get(link).text
soup = BeautifulSoup(html_text, 'html.parser')
  
divTag = soup.find_all("div", {"class": "product"})

stamps = []

for tag in divTag:
    tdTags = tag.find_all("div", {"class": "product-title"})
    ssTags = tag.find("div", {"class": "sold"})
    aaTags = tag.find("div", {"class": "available"})   
    for tag in tdTags:
      stamps.append (tag.text + " : " + str(ssTags.text) + " || " + str(aaTags.text))

print (stamps[0])
print (stamps[1])
print (stamps[2])
print (stamps[3])
