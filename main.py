from SpotifyMp3 import SpotifyMp3
import tkinter


path = "./"
url = "https://open.spotify.com/playlist/37i9dQZF1DX4eRPd9frC1m"
spotifyMp3 = SpotifyMp3(url, path)
try:
    print("Started")
    spotifyMp3.start()
except Exception as e:
    print(e)
    spotifyMp3.closeBrowser()

