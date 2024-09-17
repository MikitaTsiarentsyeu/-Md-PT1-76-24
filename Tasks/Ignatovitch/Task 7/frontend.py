from backend import Collection

def main():
    collection = Collection()
    
    while True:
        print("\nMenu:")
        print("1. Add a new album or movie")
        print("2. List all albums or movies")
        print("3. Search for an album or movie")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            title = input("Enter title: ")
            artist_or_director = input("Enter artist or director: ")
            year = input("Enter year: ")
            genre = input("Enter genre: ")
            collection.add_item(title, artist_or_director, year, genre)
            print("Item added successfully!")

        elif choice == '2':
            items = collection.list_items()
            if items:
                for idx, item in enumerate(items, start=1):
                    print(f"{idx}. Title: {item['title']}, Artist/Director: {item['artist_or_director']}, Year: {item['year']}, Genre: {item['genre']}")
            else:
                print("No items found.")

        elif choice == '3':
            search_type = input("Search by (title/artist_or_director/year/genre): ").strip()
            search_value = input(f"Enter {search_type}: ")
            results = collection.search_items(**{search_type: search_value})
            if results:
                for idx, item in enumerate(results, start=1):
                    print(f"{idx}. Title: {item['title']}, Artist/Director: {item['artist_or_director']}, Year: {item['year']}, Genre: {item['genre']}")
            else:
                print("No items found.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()