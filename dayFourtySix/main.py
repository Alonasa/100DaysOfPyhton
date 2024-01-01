from datetime import datetime

import requests
from bs4 import BeautifulSoup
from requests import request

client_id = "af95b8b6e51245d3bbde7942c54d3ffd"
client_secret = "c9b1660a8386475cbda88586a4c5998e"

base_url = "https://www.billboard.com/charts/hot-100"

date = input("Write date to check music chart in format YYYY-MM-DD ").strip()

get_songs = requests.get(url=f"{base_url}/{date}")
page = get_songs.text

elements = BeautifulSoup(page, "html.parser")

song_title = elements.select("li ul li h3")
song_titles_list = [song.getText().strip() for song in song_title]
print(song_titles_list)

# song_author = elements.find_all(name="span", class_="c-label")
# songs = [song.getText() for song in song_titles]
# authors = [author.getText() for author in song_author]
#
# for element in songs, authors:
#     print(f"{element}\n")
