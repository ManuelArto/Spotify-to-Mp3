from SpotifyMp3 import SpotifyMp3
from View import View
import threading


class Main:

	def __init__(self):
		View(start=self.start)

	def start(self, url, view):
		def callback():
			try:
				path = ""	# TODO: ask for path
				spotifyMp3 = SpotifyMp3(url, path)
				songs = spotifyMp3.get_titles()
				view.write_songs(songs)
				links = spotifyMp3.get_links()
				view.write_links(links)
				spotifyMp3.download_from_yt(view.write_download, songs)
				print("END")
			except Exception as e:
				print(e)
		t = threading.Thread(target=callback)
		t.start()


if __name__ == "__main__":
	Main()
