from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


data_user = input("Which year & date that you want to travel to ?, Input date in YYYY-MM-DD format.")

URL = "https://www.billboard.com/charts/hot-100/" + data_user + "/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')

song_titles = soup.select('div>ul>li>ul>li>h3')
artist_names = soup.select('div>ul>li>ul>li>span.a-no-trucate.a-font-primary-s')

list_of_songs = [songs.get_text().strip() for songs in song_titles]
print(list_of_songs)

list_of_artist_names = [artist.get_text().strip() for artist in artist_names]
print(list_of_artist_names)

CLIENT_ID = "222600408154410fb5df8e7fc8c8caaf"
CLIENT_SECRET = "d7e8c2d7fee24977ad15ad16a9f06331"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="31zjghz2mrv6w76i3xkecs6nwphq",
    )
)
# Here's a short explanation of each parameter used with SpotifyOAuth:
#
# scope: Defines permissions the app needs (e.g., modifying private playlists).
# redirect_uri: URL Spotify redirects to after authentication.
# client_id and client_secret: Identifiers for your app to connect with Spotify's API.
# show_dialog: If True, forces Spotify’s login dialog to appear each time for authentication.
# cache_path: Path to store the token for session persistence.
# username: Spotify username of the account to modify playlists.

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = data_user.split("-")[0]  #2012-06-30

for song, artist_name in zip(list_of_songs, list_of_artist_names):
    result = sp.search(q=f"track:{song} year:{year} artist:{artist_name}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{data_user} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)