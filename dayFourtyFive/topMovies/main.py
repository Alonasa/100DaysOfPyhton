import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
page = response.text

movie_title = "listicleItem_listicle-item__title__BfenH"

elements = BeautifulSoup(page, "html.parser")
all_titles = elements.find_all(name="h3", class_=movie_title)
print(all_titles)
