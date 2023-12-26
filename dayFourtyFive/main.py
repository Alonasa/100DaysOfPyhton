import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://dev.to/t/news")
page = response.text

content = BeautifulSoup(page, "html.parser")
elements = content.find_all(name="div", class_="crayons-story__body")
authors = (content.find_all(name="a", class_="crayons-story__secondary"))
# .getText().strip())
posting_dates = content.find_all(name="time")
titles = content.find_all(name="h2", class_="crayons-story__title")
hashtags = content.find_all(name="a", class_="crayons-tag")
for hashtag in hashtags:
    text = hashtag.getText()

for el in posting_dates:
    posted = el['datetime']
# print(element)
# soup = BeautifulSoup(content, "lxml")
