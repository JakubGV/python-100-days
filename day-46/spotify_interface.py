import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

class SpotifyInterface:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope: str) -> None:
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope=scope))

    def find_song_URI(self, name: str, yyyy: str):
        query_string = f"track: {name} year: {yyyy}"
        response = self.sp.search(query_string, limit=1, type='track')
        time.sleep(0.5)
        
        try:
            return response['tracks']['items'][0]['uri']
        except IndexError:
            return None