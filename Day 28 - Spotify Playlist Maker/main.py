from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

#Your Spotify Credentials
spotify_clientid = your id
spotify_clientsecret = your secret key


date = input("From what time you want to get songs?(YYYY-MM-DD) ")
# Searching the billboard of given date.
URL = "https://www.billboard.com/charts/hot-100/"+date

# Scraping BillBoard
response = requests.get(URL)
bibly_songs = response.text
soup = BeautifulSoup(bibly_songs, "html.parser")
songs = [song.getText().strip() for song in soup.select("li #title-of-a-story")]
# print(songs)

artists = [artist.getText().strip() for artist in soup.select("li .a-truncate-ellipsis-2line")]
# print(artists)

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_clientid,
                                               client_secret=spotify_clientsecret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))
user_id = sp.current_user()["id"]


songs_uri = []
# Searching spotify songs by title and artist name
for i in range(len(songs)):
    results = sp.search(q=f"track:{songs[i]} artist:{artists[i]}", limit=1, type="track")
    # print(results)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"{songs[i]} doesn't exist on spotify. Skipped")

#print(songs_uri)
# Creating a New playlist in spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} BillBoard 100", public=False)
# adding songs in that playlist
sp.playlist_add_items(playlist_id=playlist['id'], items=songs_uri)


