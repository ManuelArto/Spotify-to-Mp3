# SpotifyToMp3
SpotifyToMp3 is an app developed in python that let you to download in mp3 format all the songs in a playlist or album on spotify.

You have to insert the **URL** of a public playlist(like: https://open.spotify.com/playlist/37i9dQZF1DX4eRPd9frC1m) and then the app will download all the songs in a folder named like the playlist's title.

There are **three** version of the app, and for each one a **TUI** and **GUI**(could not working well) mode:

- ### BeautifulSoup (best one)
Using the **BeautifulSoup** library, doesn't require to do anything.

- ### Selenium
Using the **Selenium** library: you need to download the chromedriver module and change the **executable_path** in **SpotifyMp3**.py

Selenium Docs: https://selenium-python.readthedocs.io/

- ### API
Using two **API** libraries, one for YT and the other one for Spotify.
You need to setup the APIs for the two services and insert your credentials manually in **SpotifyMp3**.py

1. Spotipy Docs: https://spotipy.readthedocs.io/en/latest/
2. Youtube API Docs: https://developers.google.com/youtube/v3/quickstart/python
