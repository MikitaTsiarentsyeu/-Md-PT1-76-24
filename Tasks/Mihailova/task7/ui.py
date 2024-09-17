import bl  

def get_all():
    print(bl.get_all())

def get():
    name = input("Enter album name:\n")
    print(bl.get(name))

def add():
    album = {}
    for attr in bl.albums_attrs:
        album[attr] = input(f'Enter album {attr}: ')
    bl.add(**album)
    print("Album added successfully.")

def search():
    keyword = input("Enter search keyword (title, artist, year, or genre):\n")
    print(bl.search(keyword))

def main_menu():
    while True:
        action = input("""Choose a number of action:
          1. Get list of albums
          2. Search by name, artist, year, or genre
          3. Add new album
          4. Exit\n""")
        if action == "1":
            get_all()
        elif action == "2":
            search()
        elif action == "3":
            add()
        elif action == "4":
            print("Exiting the program.")
            exit()
        else:
            print("Please choose a valid action number.")

main_menu()
