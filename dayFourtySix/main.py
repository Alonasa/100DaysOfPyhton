from datetime import datetime

import requests
from bs4 import BeautifulSoup
from requests import request

base_url = "https://www.billboard.com/charts/hot-100"

date = input("Write date to check music chart in format YYYY-MM-DD ").strip()

get_songs = requests.get(url=f"{base_url}/{date}")
page = get_songs.text

elements = BeautifulSoup(page, "html.parser")

song_title = elements.select("li ul li h3")
song_titles_list = [song.getText().strip() for song in song_title]
song_author = elements.select("li ul li span")
song_authors_list = [song.getText().strip() for song in song_author]
print(song_authors_list)

# song_author = elements.find_all(name="span", class_="c-label")
# songs = [song.getText() for song in song_titles]
# authors = [author.getText() for author in song_author]
#
# for element in songs, authors:
#     print(f"{element}\n")
