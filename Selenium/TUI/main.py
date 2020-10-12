from SpotifyMp3 import SpotifyMp3

spotifyMp3 = ()
try:
	url = input("Inserisci l'URL della playlist di spotify: ")
	path = input("Inserisci il nome della cartella di download (leave blank for spotify playlist title): ")
	spotifyMp3 = SpotifyMp3(url, path)
	print("[STARTING]")
	while True:
		choice = input("1. Save songs' title\n2. Save songs' link\n3. Download songs\n4. Break\nSelect: ")
		if choice == "1":
			spotifyMp3.get_titles()
		elif choice == "2":
			spotifyMp3.get_links()
		elif choice == "3":
			spotifyMp3.download_from_yt()
		elif choice == "4":
			break
		else:
			print("Select a valide choice")
except Exception as e:
	print(e)
