import bl


def get_all():
    res = bl.get_all()
    print(res)


def get():
    title = input("Enter movie title:\n")
    res = bl.get(title)
    print(res)


def get_by_director():
    director = input("Enter director name:\n")
    movies = bl.get_by_director(director)
    if movies:
        for movie in movies:
            print(bl.movie_to_str(movie))
    else:
        print("No movies found by this director")


def get_by_year():
    year = int(input("Enter movie year:\n"))
    movies = bl.get_by_year(year)
    if movies:
        for movie in movies:
            print(bl.movie_to_str(movie))
    else:
        print("No movies found from this year")


def get_by_genre():
    genre = input("Enter movie genre:\n")
    movies = bl.get_by_genre(genre)
    if movies:
        for movie in movies:
            print(bl.movie_to_str(movie))
    else:
        print("No movies found in this genre")


def add():
    movie = {}
    movie["title"] = input("Enter movie title: ")
    movie["director"] = input("Enter movie director: ")
    year = input("Enter movie year: ")
    try:
        movie["year"] = int(year)
    except ValueError:
        movie["year"] = year
    movie["genre"] = input("Enter movie genre: ")
    bl.add(**movie)


def main_menu():
    while True:
        action = input(
            """Choose an action number:
            1. List all movies
            2. Get a movie by title
            3. Get movies by director
            4. Get movies by year
            5. Get movies by genre
            6. Add new movie
            7. Exit\n"""
        )

        if action == "1":
            get_all()
        elif action == "2":
            get()
        elif action == "3":
            get_by_director()
        elif action == "4":
            get_by_year()
        elif action == "5":
            get_by_genre()
        elif action == "6":
            add()
        elif action == "7":
            exit()
        else:
            print("Please choose from the action numbers only")


main_menu()
