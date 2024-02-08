import requests
from bs4 import BeautifulSoup

FORM_LINK = "https://forms.gle/5SzSdbMkdXPfMgQ66"
WEBSITE_LINK = "https://appbrewery.github.io/Zillow-Clone/"

data = requests.get(url=WEBSITE_LINK).text
elements = BeautifulSoup(data, "html.parser")

ADVERTISINGS = elements.find_all(attrs={"class": "StyledPropertyCardPhotoBody"})
LINKS = [item.a["href"] for item in ADVERTISINGS]
print(LINKS)
