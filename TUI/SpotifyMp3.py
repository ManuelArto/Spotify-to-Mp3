from builtins import print

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pytube import YouTube
import os


class SpotifyMp3:

    def __init__(self, url, path):
        options = Options()
        options.headless = True
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)
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
        driver.get(self.url)
        titles = WebDriverWait(driver, 5).until(
                     EC.visibility_of_all_elements_located((By.CLASS_NAME, "tracklist-name")))
        artists = driver.find_elements_by_class_name("TrackListRow__artists")
        self.path += str(driver.title) + "/"
        file = open("./files/songs.txt", 'w+')
        for song, artist in zip(titles, artists):
            file.write(song.text + " " + artist.text + "\n")
        file.close()

    def get_links(self):
        print("getting links")
        driver = self.driver
        file = open("./files/songs.txt", 'r')
        songs = file.readlines()
        file = open("./files/links.txt", 'w+')
        for song in songs:
            try:
                driver.get("http://www.youtube.com/results?search_query=" + song)
                link = WebDriverWait(driver, 5).until(
                       EC.visibility_of_all_elements_located((By.ID, "video-title")))[0].get_attribute("href")
                file.write(link + "\n")
            except Exception as e:
                print(song + " at number " + str(songs.index(song)) + " not found. ERROR:")
                print(e)
        file.close()
        self.closeBrowser()

    def download_from_yt(self):
        print("downloading")
        os.mkdir(self.path)
        file = open("./files/links.txt", 'r')
        links = file.readlines()
        for link in links:
            yt = YouTube(link)
            stream = yt.streams.last()
            stream.download(output_path=self.path)
            os.rename(self.path + stream.default_filename,
                      self.path + str(stream.default_filename).strip(".webm") + ".mp3")
