import os


movies = [
    {
        "title": "Spider-Man: No Way Home",
        "director": "Jon Watts",
        "year": 2021,
        "genre": "Action, Adventure, Fantasy",
    },
    {
        "title": "La La Land",
        "director": "Damien Chazelle",
        "year": 2016,
        "genre": "Comedy, Drama, Music",
    },
    {
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010,
        "genre": "Action, Adventure, Sci-Fi",
    },
    {
        "title": "Parasite",
        "director": "Bong Joon Ho",
        "year": 2019,
        "genre": "Comedy, Drama, Thriller",
    },
    {
        "title": "Interstellar",
        "director": "Christopher Nolan",
        "year": 2014,
        "genre": "Adventure, Drama, Sci-Fi",
    },
    {
        "title": "Joker",
        "director": "Todd Phillips",
        "year": 2019,
        "genre": "Crime, Drama, Thriller",
    },
    {
        "title": "The Dark Knight Rises",
        "director": "Christopher Nolan",
        "year": 2012,
        "genre": "Action, Adventure",
    },
    {
        "title": "Mad Max: Fury Road",
        "director": "George Miller",
        "year": 2015,
        "genre": "Action, Adventure, Sci-Fi",
    },
    {
        "title": "Avengers: Endgame",
        "director": "Anthony Russo, Joe Russo",
        "year": 2019,
        "genre": "Action, Adventure, Drama",
    },
    {
        "title": "Dune",
        "director": "Denis Villeneuve",
        "year": 2021,
        "genre": "Adventure, Drama, Sci-Fi",
    },
]


file_path = os.path.join(os.path.dirname(__file__), "movies.txt")


def save_to_file():
    with open(file_path, "w") as file:
        for movie in movies:
            file.write(
                f"{movie['title']}|{movie['director']}|{movie['year']}|{movie['genre']}\n"
            )


def load_from_file():
    global movies
    try:
        with open(file_path, "r") as file:
            movies = []
            for line in file:
                title, director, year, genre = line.strip().split("|")
                try:
                    year = int(year)
                except ValueError:
                    year = year
                movies.append(
                    {"title": title, "director": director, "year": year, "genre": genre}
                )
    except FileNotFoundError:
        pass


def get_all():
    res = ""
    if movies:
        for movie in movies:
            res += f"{movie_to_str(movie)}\n"
        return res.rstrip()
    return "No movies found"


def get(title):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            return movie_to_str(movie)
    return "No movie found with this title"


def get_by_director(director):
    return [movie for movie in movies if movie["director"].lower() == director.lower()]


def get_by_year(year):
    return [movie for movie in movies if movie["year"] == year]


def get_by_genre(genre):
    return [movie for movie in movies if genre.lower() in movie["genre"].lower()]


def add(**movie):
    movies.append(movie)
    save_to_file()


def movie_to_str(movie):
    return f"title: '{movie['title']}', director: '{movie['director']}', year: {movie['year']}, genre: '{movie['genre']}'"


load_from_file()
