import requests
from bs4 import BeautifulSoup

FORM_LINK = "https://forms.gle/5SzSdbMkdXPfMgQ66"
WEBSITE_LINK = "https://appbrewery.github.io/Zillow-Clone/"

data = requests.get(url=WEBSITE_LINK).text
elements = BeautifulSoup(data, "html.parser")

ADVERTISINGS = elements.find_all(attrs={"class": "ListItem-c11n-8-84-3-StyledListCardWrapper"})
LINKS = [item.a["href"] for item in ADVERTISINGS]
PRICES = [el.text.replace("+", "/").split("/")[0] for el in
          elements.find_all("span", {"data-test": "property-card-price"})]
ADDRESSES = [el.text.replace("|", ",").split(",", 1)[1].strip() for el in elements.find_all("address")]
print(PRICES)
print(LINKS)
print(ADDRESSES)
