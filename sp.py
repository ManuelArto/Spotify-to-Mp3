from API import client_id_key, client_secret_key
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json


class SpotifyApi:

    def __init__(self):
        client_id = client_id_key           # INSERT YOUR CREDENTIAL HERE
        client_secret = client_secret_key
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get_playlist_tracks(self, playlist_id):
        sp = self.sp
        result = sp.user_playlist_tracks(user="", playlist_id=playlist_id)
        tracks = []
        for track in result["items"]:
            string = track["track"]["name"] + " _ "
            for artist in track["track"]["artists"]:
                string += artist["name"] + " "
            tracks.append(string[0:-1])
        print(json.dumps(tracks, indent=3))
        return tracks


spotifyApi = SpotifyApi()
tracks = spotifyApi.get_playlist_tracks(playlist_id="37i9dQZF1DX6wfQutivYYr")