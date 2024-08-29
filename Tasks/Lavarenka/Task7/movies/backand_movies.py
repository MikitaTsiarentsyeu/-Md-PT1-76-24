import json


def load_json():
    """
    Loads the json file and returns it as a dictionary.
    """
    try:
        with open('movies/db_movies.json') as file:
            data = json.load(file)
            return data
    except:
        return None


def list_movies():
    """
    Returns a list of movies, if there are no movies, offers to add
    """
    data = load_json()
    if not data:
        print(f'There are no movies in this collection, if you want to add, write YES')
        add_m = input()
        if add_m == 'YES':
            return add_movies()
    else:
        for movie in data:
            # we go through the dictionary with a genre check
            for key, value in movie.items():
                if type(value) == list:
                    print(f'{key}: {", ".join(value)}')  # genre
                else:
                    print(f'{key}: {value}')
            print()


def add_movies():
    """
    Adds a movie with date checking
    """
    movie_name = input('Movie Name: ')
    movie_director = input('Movie Director: ')
    while True:
        try:
            movie_year = int(input('Movie Year (Please indicate the year of the film in numbers, > 1900 and < 2028): '))
            if 1900 < movie_year <= 2028:
                movie_year = str(movie_year)
                break
            else:
                print('Invalid value, Try again')
        except ValueError:
            print('Please enter a valid year.')
    movie_genre = input('Movie Genre (separated by a space): ').split(' ')
    res = {'Movie Title': movie_name, 'Movie Director': movie_director, 'Movie Year': movie_year, 'Genre': movie_genre}
    data = load_json()
    if data == None:
        data = []  # If the list is empty, then create a new one
    data.append(res)  # we add the dictionary to the list and then convert it to json
    with open('movies/db_movies.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print(f'Movie added:\n'
              f'Movie Title: {movie_name}\n'
              f'Movie Director: {movie_director}\n'
              f'Movie Year: {movie_year}\n'
              f'Genre: {",".join(movie_genre)}\n')


def search_movies():
    """
    case-insensitive search by title, author, date or genre
    if there are no movies, offers to add
    genres are searched only if you write the word in full
    """
    data = load_json()
    if not data:
        print(f'There are no movies in this collection, if you want to add, write YES')
        add_m = input()
        if add_m == 'YES':
            return add_movies()
    else:
        search_movie = input('Search Movie: ').lower()
        flag = False
        for movie in data:
            for key, value in movie.items():
                if isinstance(value, str):
                    value = value.lower()
                if isinstance(value, list):
                    value = map(str.lower, value)
                if search_movie in value:
                    if flag == False:
                        # will output 1 time if it finds more than one movie
                        print('Movies found according to your request:')
                        print()
                    flag = True  # if there is a movie

                    for key, value in movie.items():
                        if type(value) == list:
                            print(f'{key}: {", ".join(value)}')
                        else:
                            print(f'{key}: {value}')
                    print()
    if flag == False:
        print(f'Movie "{search_movie}" was found')
