import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://dev.to/t/news")
page = response.text

content = BeautifulSoup(page, "html.parser")
element = content.find(name="div", class_="crayons-story__indention")
print(element)
# soup = BeautifulSoup(content, "lxml")
