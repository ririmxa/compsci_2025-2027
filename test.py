playlist = []
history = []

def add_song():
    song_title = input("Enter the song title: ")
    song_year = input("Enter the song year: ")
    playlist.append([song_title, song_year])
    print(f"Added [{song_title}, {song_year}]")

def play_next():
    if not playlist:
        print("Playlist is empty.")
    else:
        song = playlist.pop(0)
        history.insert(0, song)
        print (f"Now playing: {song[0]}")

def view_song_year():
    if not history:
        print("No song is playing.")
    else:
        song = history[0]
        print(f"Song was released in: {song[1]}")

def play_previous():
    if not history:
        print("No history available.")
    else:
        song = history.pop(0)
        playlist.insert(0, song)
        print(f"Rewinding to: {song}")

def view_status():
    print("---Status---")
    print("History (most recent first): ")
    for s in history:
        print(f"[{s[0]}], [{s[1]}]")
    
    print("Queue (waiting to be played): ")
    for s in playlist:
        print(f"[{s[0]}], [{s[1]}]")

while True:
    print("~Menu~")
    print("1. Add Song")
    print("2. Play Next")
    print("3. View Song Year")
    print("4. Play Previous")
    print("5. View Status (History & Queue)")
    print("6. Exit")

    choice = input("What would you like to do?: ")
    if choice == "1":
        add_song()
    elif choice == "2":
        play_next()
    elif choice == "3":
        view_song_year()
    elif choice == "4":
        play_previous()
    elif choice == "5":
        view_status()
    elif choice == "6":
        print("---Exiting Music Player---")
        break
    else:
        print("Invalid Input")
