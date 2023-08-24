from dotenv import load_dotenv
import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy

load_dotenv()

os.environ['CLIENT_ID'] = "<client id>"
os.environ['CLIENT_SECRET'] = "<client secret>"

clid = os.getenv("CLIENT_ID")
clscrt = os.getenv("CLIENT_SECRET")  

def get_user_top_tracks(token):
    sp = spotipy.Spotify(auth=token)
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='medium_term')  # 'short_term', 'medium_term', 'long_term'
    return top_tracks

def display_top_tracks(tracks):
    print("Nischal's Top Tracks:")
    for idx, track in enumerate(tracks['items']):
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_images = track['album']['images']

        print(f"{idx + 1}. {track['name']} by {artists}")
        print(f"   Album: {album_name}")
        if album_images:
            print(f"   Album Image URL: {album_images[0]['url']}")
        else:
            print("   Album Image URL not available")
        print("") 
def main():
    SPOTIPY_REDIRECT_URI = 'http://localhost:8080/callback'
    auth_manager = SpotifyOAuth(client_id=clid, client_secret=clscrt, redirect_uri=SPOTIPY_REDIRECT_URI, scope="user-top-read")
    token_info = auth_manager.get_cached_token()

    if not token_info:
        auth_url = auth_manager.get_authorize_url()
        print(f"Please visit this URL to authenticate: {auth_url}")

        auth_code = input("Enter the code from the URL: ")
        token_info = auth_manager.get_access_token(auth_code)

    access_token = token_info['access_token']
    top_tracks = get_user_top_tracks(access_token)
    display_top_tracks(top_tracks)

if __name__ == "__main__":
    main()
