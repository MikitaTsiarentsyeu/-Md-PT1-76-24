import json


def load_json():
    try:
        with open('movies/db_movies.json') as file:
            data = json.load(file)
            return data
    except:
        return None



def list_movies():
    data = load_json()
    if not data:
        print(f'There are no movies in this collection, if you want to add, write YES')
        add_m = input()
        if add_m == 'YES':
            return add_movies()
    else:
        for movie in data:
            for key, value in movie.items():
                if type(value) == list:
                    print(f'{key}: {", ".join(value)}')
                else:
                    print(f'{key}: {value}')
            print()


def add_movies():
    movie_name = input('Movie Name: ')
    movie_director = input('Movie Director: ')
    while True:
        try:
            movie_year = int(input('Movie Year (Please indicate the year of the film in numbers, > 1900): '))
            if 1900 < movie_year < 2026:
                movie_year = str(movie_year)
                break
            else:
                print('Try again')
        except ValueError:
            print('Please enter a valid year.')
    movie_genre = input('Movie Genre: ').split(' ')
    res = {'Movie Title': movie_name, 'Movie Director': movie_director, 'Movie Year': movie_year, 'Genre': movie_genre}
    data = load_json()
    if data == None:
        data = []
    data.append(res)
    with open('movies/db_movies.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

        print('Movie added')


def search_movies():
    search_movie = input('Search Movie: ').lower()
    data = load_json()
    flag = False
    for movie in data:
        for key, value in movie.items():
            if isinstance(value, str):
                value = value.lower()
            if search_movie in value:
                print('Movies found according to your request:')
                flag = True
                for key, value in movie.items():
                    if type(value) == list:
                        print(f'{key}: {", ".join(value)}')
                    else:
                        print(f'{key}: {value}')
                print()
    if flag == False:
        print(f'Movie "{search_movie}" was found')
