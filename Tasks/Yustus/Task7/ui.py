import albums_service as al

def get_all_albums():
    albums = al.list_albums()

def get_album_by_title():
    title = input("Enter album title: ")
    album = al.get_album_by_title(title)
    if album:
        print(al.album_to_str(album))
    else:
        print(f"No album found with title '{title}'")

def get_albums_by_artist():
    artist = input("Enter artist name: ")
    albums = al.get_albums_by_artist(artist)
    if albums:
        for album in albums:
            print(al.album_to_str(album))
    else:
        print(f"No albums found by artist '{artist}'")

def get_albums_by_year():
    year = int(input("Enter album year: "))
    albums = al.get_albums_by_year(year)
    if albums:
        for album in albums:
            print(al.album_to_str(album))
    else:
        print(f"No albums found from year {year}")

def get_albums_by_genre():
    genre = input("Enter album genre: ")
    albums = al.get_albums_by_genre(genre)
    if albums:
        for album in albums:
            print(al.album_to_str(album))
    else:
        print(f"No albums found in genre '{genre}'")

def add_album():
    al.add_album()

def main_menu():
    while True:
        action = input(
            """Choose an action:
            1. List all albums
            2. Get an album by title
            3. Get albums by artist
            4. Get albums by year
            5. Get albums by genre
            6. Add new album
            7. Exit
            """
        )

        if action == "1":
            get_all_albums()
        elif action == "2":
            get_album_by_title()
        elif action == "3":
            get_albums_by_artist()
        elif action == "4":
            get_albums_by_year()
        elif action == "5":
            get_albums_by_genre()
        elif action == "6":
            add_album()
        elif action == "7":
            print("Exiting...")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main_menu()
