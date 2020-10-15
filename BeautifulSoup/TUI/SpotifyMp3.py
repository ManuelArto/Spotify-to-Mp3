import requests
import json
from bs4 import BeautifulSoup
import os


class SpotifyMp3:
	def __init__(self, url, path):
		try:
			os.mkdir("./files")
		except Exception as e:
			pass
		self.path = path
		self.url = url

	def start(self):
		self.get_titles()
		self.get_links()
		self.download_from_yt()

	def get_titles(self):
		print("getting titles")
		try:
			r = requests.get(self.url)
			html_parser = BeautifulSoup(r.text, "html.parser")
			if self.path == "":
				self.path = str(html_parser.title.string)
			tracks_json = "{" + html_parser.find_all("script")[10].string.strip(
				"\n\t\t\t\tSpotify = {};\n\t\t\t\tSpotify.Entity = ").strip(';\n\t\t\t').replace("\'", " ") + "}"  # could change
			tracks_json = json.loads(tracks_json)
			if self.path == "":
				self.path = str(html_parser.title.string)
			with open("./files/songs.txt", "w+") as file:
				for track in tracks_json["tracks"]["items"]:
					if "album" in self.url:
						file.write(
							f"{track['name']} {track['artists'][0]['name']}\n")
					else:
						file.write(
							f"{track['track']['name']} {track['track']['artists'][0]['name']}\n")
		except Exception as e:
			print("Error: ", e)

	def get_links(self):
		print("getting links")
		file = open("./files/songs.txt", "r")
		songs = [song.strip("\n") for song in file.readlines()]
		attempts = {}
		with open("./files/links.txt", "w+") as file:
			index = 0
			while index < len(songs):
				song = songs[index]
				try:
					r = requests.get(
						"http://www.youtube.com/results?search_query=" + song)
					html_parser = BeautifulSoup(r.text, "html.parser")
					script = html_parser.find(name="body").find_all(name="script")[1].string.replace('\n    window["ytInitialData"] = ', '').replace(
						""";\n    window["ytInitialPlayerResponse"] = null;\n    if (window.ytcsi) {window.ytcsi.tick("pdr", null, \'\');}\n  """, '')
					script_json = json.loads(script)
					file.write("https://www.youtube.com" + script_json["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"]
							   [0]["itemSectionRenderer"]["contents"][0]["videoRenderer"]["navigationEndpoint"]["commandMetadata"]["webCommandMetadata"]["url"] + "\n")
				except Exception as e:
					if song not in attempts.keys():
						# 5 attempts for download a song (can be changed)
						attempts[song] = 5
						print(
							f"'{song}' at number {str(index)} ERROR: {e}")
					if attempts[song] != 0:
						index -= 1
						attempts[song] -= 1
						print(f"RETRY n:{5 - attempts[song]}")
					else:
						file.write("\n")
				index += 1

	def download_from_yt(self):
		try:
			print("downloading")
			file = open("./files/links.txt", "r")
			links = [link.strip("\n") for link in file.readlines()]
			if self.path == "":
				self.path = "songs"
			try:
				os.mkdir(self.path)
			except Exception as e:
				print(f"Folder {self.path} exists")
			os.chdir(self.path)

			# youtube-dl cli
			for link in links:
				os.system(f"youtube-dl -x --audio-format mp3 {link}")

			# youtube_dl library
			# import youtube_dl
			# download_options = {
			# 	"format": "bestaudio/best",
			# 	"postprocessors": [
			# 		{
			# 			"key": "FFmpegExtractAudio",
			# 			"preferredcodec": "m4a",
			# 			"preferredquality": "192",
			# 		}
			# 	],
			# 	"postprocessor_args": ["-ar", "16000"],
			# 	"prefer_ffmpeg": True,
			# 	"keepvideo": True,
			# }
			# with youtube_dl.YoutubeDL(download_options) as dl:
			# 	dl.download(links)
		except Exception as e:
			print(e)
