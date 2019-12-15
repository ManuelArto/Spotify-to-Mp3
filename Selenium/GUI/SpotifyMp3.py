from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import youtube_dl
import os


class SpotifyMp3:

    def __init__(self, url, path):
        options = Options()
        options.headless = True
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options, executable_path="./chromedriver.exe")
        self.path = path
        self.url = url

    def closeBrowser(self):
        self.driver.quit()

    def get_titles(self):
        print("getting titles")
        driver = self.driver
        driver.get(self.url)
        titles = WebDriverWait(driver, 5).until(
                     EC.visibility_of_all_elements_located((By.CLASS_NAME, "tracklist-name")))
        artists = driver.find_elements_by_class_name("TrackListRow__artists")
        self.path += str(driver.title) + "/"
        self.songs = []
        for song, artist in zip(titles, artists):
            self.songs.append(song.text + " " + artist.text + "\n")
        return self.songs

    def get_links(self):
        print("getting links")
        driver = self.driver
        links = []
        for song in self.songs:
            try:
                driver.get("http://www.youtube.com/results?search_query=" + song)
                link = WebDriverWait(driver, 5).until(
                       EC.visibility_of_all_elements_located((By.ID, "video-title")))[0].get_attribute("href")
                links.append(link + "\n")
            except Exception as e:
                print(song + " at number " + str(self.songs.index(song)) + " not found. ERROR:")
                print(e)
        return links

    def download_from_yt(self, link):
        try:
            self.closeBrowser()
            download_options = {
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.mp3',
                'nocheckcertificate': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            if not os.path.exists("../"+self.path):
                os.mkdir(self.path)
                os.chdir(self.path)
            with youtube_dl.YoutubeDL(download_options) as dl:
                dl.download([link])
        except Exception as e:
            print(e)
