from View import View
from SpotifyMp3 import SpotifyMp3


class Main:

    def __init__(self):
        View(start=self.start)

    def start(self, url, view):
        path = "./"
        spotifyMp3 = SpotifyMp3(url, path)
        try:
            print(url)
            songs = spotifyMp3.get_titles()
            view.write_songs(songs)
            # links = spotifyMp3.get_links()
            # view.write_links(links)
        except Exception as e:
            print(e)
            spotifyMp3.closeBrowser()


if __name__ == '__main__':
    Main()
