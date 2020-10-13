from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time


class SpotifyMp3:
	def __init__(self, url, path):
		try:
			os.mkdir("./files")
		except Exception as e:
			pass
		options = Options()
		options.headless = True
		prefs = {"profile.managed_default_content_settings.images": 2}
		options.add_experimental_option("prefs", prefs)
		self.driver = webdriver.Chrome(
			options=options, executable_path="/home/manuel/Downloads/chromedriver"
		)
		self.path = path
		self.url = url

	def closeBrowser(self):
		self.driver.quit()

	def start(self):
		self.get_titles()
		self.get_links()
		self.download_from_yt()

	def get_titles(self):
		print("getting titles")
		driver = self.driver
		try:
			driver.get(self.url)
			time.sleep(7)
			titles = driver.find_elements_by_class_name("da0bc4060bb1bdb4abb8e402916af32e-scss")
			artists = driver.find_elements_by_class_name("_966e29b71d2654743538480947a479b3-scss")
			self.path += str(driver.title) if self.path != "" else "" + "/"
			with open("./files/songs.txt", "w+") as file:
				for song, artist in zip(titles, artists):
					file.write(f"{song.text} {artist.text}\n")
		except Exception as e:
			print(e)

	def get_links(self):
		print("getting links")
		driver = self.driver
		file = open("./files/songs.txt", "r")
		songs = file.readlines()
		file = open("./files/links.txt", "w+")
		for song in songs:
			try:
				driver.get("http://www.youtube.com/results?search_query=" + song)
				link = (
					WebDriverWait(driver, 5)
					.until(
						EC.visibility_of_all_elements_located((By.ID, "video-title"))
					)[0]
					.get_attribute("href")
				)
				file.write(link + "\n")
			except Exception as e:
				print(song.strip("\n") + " at number " + str(songs.index(song)) + " not found. ERROR: ", end="")
				print(e)
		file.close()
		self.closeBrowser()

	def download_from_yt(self):
		try:
			self.closeBrowser()
			print("downloading")
			file = open("./files/links.txt", "r")
			links = file.readlines()
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
