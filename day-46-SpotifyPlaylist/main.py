import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
SPOTIPY_CLIENT_ID = "6a74a37a4f9f45c0821e76b0638846ce"
SPOTIPY_CLIENT_SECRET = "d054d6cfbcd64aa0a357b2c7a34c1a20"

# get the Spotify OAuth
obj_spotipy = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri="http://localhost:8080/",
        scope="playlist-modify-private",
        cache_path="token.txt",
        username="陳重光"
    )
)
user_id = obj_spotipy.current_user()["id"]
print(user_id)

# get the day from user input
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:  \n")
year = date.split("-")[0]

# send the request to the website and get the html code
response = requests.get(URL + date + "/");
soup = BeautifulSoup(response.text, "html.parser")

# get the top 100 song title
song_uris = []
title_list = soup.select("li h3", id="title-of-a-story", limit=100)
for title in title_list:
    song_name = title.get_text().strip()
    result = obj_spotipy.search(q=f"track:{song_name} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        # print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song_name} doesn't exist in Spotify. Skipped.")

# create the spotify playlist
playlist = obj_spotipy.user_playlist_create(user=user_id, name=f"{date} Billboard 100 from Python", public=False)
print(playlist)

# add the songs into the new playlist
obj_spotipy.playlist_add_items(playlist_id=playlist["id"], items=song_uris)





