import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

class SpotifyInterface:

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, scope: str) -> None:
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope=scope))

    def get_user_id(self) -> str:
        return self.sp.current_user()['id']
    
    def find_song_URI(self, name: str, yyyy: str):
        query_string = f"track: {name} year: {yyyy}"
        response = self.sp.search(query_string, limit=1, type='track')
        time.sleep(0.5)
        
        try:
            return response['tracks']['items'][0]['uri']
        except IndexError:
            return None

    def create_playlist(self, name: str, public: bool):
        user = self.get_user_id()
        try:
            response = self.sp.user_playlist_create(user, name=name, public=public)
            return response['id']
        except KeyError:
            return None

    def add_playlist_songs(self, playlist_id: str, songs: list):
        try:
            response = self.sp.playlist_add_items(playlist_id, songs)
            return response['snapshot_id']
        except KeyError:
            return None