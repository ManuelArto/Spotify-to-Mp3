from SpotifyMp3 import SpotifyMp3

spotifyMp3 = ()
try:
    url = input("Inserisci l'URL della playlist di spotify\n")
    # path = input("Inserisci il nome della cartella di download\n")
    spotifyMp3 = SpotifyMp3(url, "")
    print("Started")
    spotifyMp3.start()
except Exception as e:
    print(e)
