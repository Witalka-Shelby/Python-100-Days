import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date_input = "2006-06-17"
song_year = date_input.split("-")[0]

config = dotenv_values(".env")
spotify_id = config['SPOTIFY_ID']
spotify_secret = config['SPOTIFY_SECRET']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_id,
                                               client_secret=spotify_secret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-public"))


user_id = sp.current_user()["id"]
user_playlists = sp.current_user_playlists()["items"]
playlist_list = []
uri_songs = []
create_playlist_name = "Billboard_100_witalka"
playlist_id = ""

#create playlist if not created
for playlist in user_playlists:
    playlist_list.append(playlist["name"])
    if playlist["name"] == create_playlist_name:
        playlist_id = playlist["uri"]


if create_playlist_name not in playlist_list:
    sp.user_playlist_create("witalka", "Billboard_100_witalka")


url = f"https://www.billboard.com/charts/hot-100/{date_input}/"

with open("./day 46/billboard.html") as website:
    website_html = website.read()

soup = BeautifulSoup(website_html, "html.parser")
songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

for song in songs:
    singer_name = song.select_one(selector="ul li ul li span").text.strip().split()
    song_name = song.select_one(selector="ul li ul li h3").text.strip()

    search = sp.search(f"track: {song_name} year: {song_year}")["tracks"]["items"]
    try:
        for song in search:
            search_artist = song["artists"][0]["name"]
            if search_artist in singer_name:
                uri_songs.append(song["uri"])
                # sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=search_id,  position=None)
                # sp.playlist_add_items(playlist_id=playlist_id, items=uri_songs)
                break
    except IndexError:
        print("Song no available")

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=uri_songs,  position=None)