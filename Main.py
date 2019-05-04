from View import View
from SpotifyMp3 import SpotifyMp3


def start(url):

    path = "./"
    spotifyMp3 = SpotifyMp3(url, path)
    try:
        print(url)
        # songs = spotifyMp3.get_titles()
        # write on songs
        # links = spotifyMp3.get_links()
    except Exception as e:
        print(e)
        spotifyMp3.closeBrowser()


view = View(start=start)
