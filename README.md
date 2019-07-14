# Spotify-To_Mp3
This is an app developed in python that let you to download in mp3 format all the songs in a playlist on spotify.

You have to insert the URL of a public playlist(like: https://open.spotify.com/playlist/37i9dQZF1DX4eRPd9frC1m) of 
spotify and then the app will download all the songs in a folder named by the title of the playlist.


There are **two** version of the app:

## Selenium
    That one use the library Selenium and the "chromedriver.exe" to manage the browser and find all the names of songs and
    the relative youtube's links, then all of them will be downloaded with the library youtube_dl

## API
    That one use two API library, one for YT and the other for Spotify, to find the names of the songs and the relative 
    youtube's links, then all of them will be downloaded with the library youtube_dl

#
If you want to run or edit the project you need to install those libraries:

1. Selenium: https://selenium-python.readthedocs.io/
2. Youtube_dl: https://ytdl-org.github.io/youtube-dl/index.html

APIs:
1. Spotipy: https://spotipy.readthedocs.io/en/latest/
2. Youtube API: https://developers.google.com/youtube/v3/quickstart/python

For the APIs credentials follow the instructions on the link above and then you will be able to insert them in the app
