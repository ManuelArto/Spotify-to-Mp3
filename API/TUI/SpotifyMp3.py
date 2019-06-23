# API Credentials
from API.API import SP_client_id_key, SP_client_secret_key, YT_DEVELOPER_KEY
# for Spotify API
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
# for YT API
import googleapiclient.discovery
# for download from YT
from pytube import YouTube
import os


class SpotifyMp3:

    def __init__(self, url, path):
        self.playlist_id = url.split("list/")[1]
        self.path = path + "/"
        # Spotify API config
        client_id = SP_client_id_key           # INSERT YOUR CREDENTIAL HERE
        client_secret = SP_client_secret_key
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        # Youtube API config
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = YT_DEVELOPER_KEY        # INSERT YOUR API_KEY HERE
        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

    def start(self):
        self.get_titles()
        self.get_links()
        self.download_from_yt()

    def get_titles(self):
        print("getting titles")
        sp = self.sp
        result = sp.user_playlist_tracks(user="", playlist_id=self.playlist_id)
        tracks = []
        for track in result["items"]:
            string = track["track"]["name"] + " _ "
            for artist in track["track"]["artists"]:
                string += artist["name"] + " "
            tracks.append(string[0:-1])
        self.tracks = tracks

    def get_links(self):
        print("getting links")
        links = []
        for track in self.tracks:
            request = self.youtube.search().list(part="snippet", maxResults=1, q=track)
            response = request.execute()
            for items in response["items"]:
                links.append("https://www.youtube.com/watch?v=" + items["id"]["videoId"])
        self.links = links

    def download_from_yt(self):
        print("downloading")
        os.mkdir(self.path)
        for link in self.links:
            yt = YouTube(link)
            stream = yt.streams.last()
            stream.download(output_path=self.path)
            os.rename(self.path + stream.default_filename,
                      self.path + str(stream.default_filename).strip(".webm") + ".mp3")
