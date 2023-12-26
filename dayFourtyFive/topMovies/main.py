import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
page = response.text

movie_title = "listicleItem_listicle-item__title__BfenH"

elements = BeautifulSoup(page, "html.parser")
reversed_titles = elements.find_all(name="h3", class_=movie_title)
titles = reversed_titles[::-1]
with open("movies_to_watch.txt", "w", encoding="utf-8") as file:
    for movie in titles:
        movie = movie.getText()
        file.write(f"{movie}\n")
