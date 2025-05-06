from dotenv import load_dotenv
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
import requests
import os
import spotipy

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id=os.getenv("SPOTIFY_USERID")
redirect_uri="https://example.com"
spotify_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"
scope = "playlist-modify-private user-read-private playlist-read-private"

users_date = input("Which date do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
date_obj = datetime.strptime(users_date,"%Y-%m-%d")
this_year = datetime.today().year
year = date_obj.year
name = input("What would you like to call the playlist?:\n")
description = input("What description would you like to add?:\n")
loop_events = int(this_year)-int(year)

token = spotipy.oauth2.SpotifyOAuth(client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri,scope=scope)
sp = spotipy.Spotify(auth_manager=token)

spotify_data = {
    "name":name,
    "description":description,
    "public":False
}

spotify_header = {
    "Authorization":f"Bearer {token.get_access_token()['access_token']}",
    'Content-Type':'application/json'
}

response = requests.post(url=spotify_endpoint,json=spotify_data,headers=spotify_header)
playlist_id = response.json()['id']

add_items_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

song_uris=[]
best_songs=[]
best_years=[]
for i in range(0,loop_events+1):

    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

    response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}-{date_obj.month}-{date_obj.day}",
                            headers=header)
    soup = BeautifulSoup(response.text,"html.parser")
    song_title = soup.select_one("li ul li h3")
    best_songs.append(song_title.get_text().strip())
    best_years.append(year)
    year+= 1

for i in range(0,len(best_songs)):
    result = sp.search(q=f'track:{best_songs[i]} year:{best_years[i]}',type='track')

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{best_songs[i]} doesn't exist in Spotify. Skipped")

request_body = {
    "uris":song_uris,
    "position":0
}

response = requests.post(add_items_endpoint,json=request_body,headers=spotify_header)
print("Completed")
