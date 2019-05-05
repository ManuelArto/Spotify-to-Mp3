from TUI.SpotifyMp3 import SpotifyMp3

path = "./"
url = ""
try:
    url = input("Inserisci l'URL della playlist di spotify\n")
    spotifyMp3 = SpotifyMp3(url, path)
    print("Started")
    spotifyMp3.start()
except Exception as e:
    print(e)
    spotifyMp3.closeBrowser()

