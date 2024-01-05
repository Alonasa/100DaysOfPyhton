from datetime import datetime

import requests
import spotipy
from bs4 import BeautifulSoup
from requests import request
from spotipy import SpotifyClientCredentials

CLIENT_ID = "af95b8b6e51245d3bbde7942c54d3ffd"
CLIENT_SECRET = "c9b1660a8386475cbda88586a4c5998e"
SPOTIFY_REDIRECT_URI = "https://localhost:8888/callback"
ARTIST_URI = "spotify:artist:2WX2uTcsvV5OnS0inACecP"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))
birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

results = spotify.artist_albums(birdy_uri, album_type='album')
print(results["items"][0])

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
