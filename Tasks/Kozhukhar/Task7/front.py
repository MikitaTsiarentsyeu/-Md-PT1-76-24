from bl import MusicFilms


def main():
    base = MusicFilms()

    while True:
        print("\nChoose an action:")
        print("1. Add a new album or movie")
        print("2. List all albums or movies")
        print("3. Find an album or movie")
        print("4. Exit the program")

        choice = input("Enter the action number: ")

        if choice == "1":
            title = input("Enter the title: ")
            artist_or_director = input("Enter the artist or director: ")
            year = input("Enter the year: ")
            genre = input("Enter the genre: ")
            base.add_data(title, artist_or_director, year, genre)
            print("Successfully added.")

        elif choice == "2":
            media_list = base.list_media()
            for media in media_list:
                print(
                    f"Title: {media['title'].capitalize()}, Artist or Director: {media['artist_or_director'].upper()}, "
                    f"Year: {media['year']}, Genre: {media['genre'].capitalize()}"
                )

        elif choice == "3":
            title = input("Enter the title (leave empty to skip): ")
            artist_or_director = input(
                "Enter the artist or director (leave empty to skip): "
            )
            year = input("Enter the year (leave empty to skip): ")
            genre = input("Enter the genre (leave empty to skip): ")

            search_params = {
                "title": title or None,
                "artist_or_director": artist_or_director or None,
                "year": year or None,
                "genre": genre or None,
            }

            results = base.find_media(**search_params)
            for media in results:
                print(
                    f"Title: {media['title'].capitalize()}, Artist or Director: {media['artist_or_director'].upper()}, "
                    f"Year: {media['year']}, Genre: {media['genre'].capitalize()}"
                )

        elif choice == "4":
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
