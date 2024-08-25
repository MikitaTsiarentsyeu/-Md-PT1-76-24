import json
from .backand_movies import list_movies, add_movies, search_movies


# data = [
#     {'Movie Title': 'Elvis the Pig', 'Movie Director': 'Jason Mills', 'Movie Year': '2022', 'Genre': ['Foreign', 'Family']},
#     {'Movie Title': "The Djinn's Curse", 'Movie Director': 'Khong Khaek', 'Movie Year': '2023', 'Genre': ['Foreign', 'Horrors']},
#
#
#
# ]
#
# with open('db_movies.json', 'w') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)


def get_all():
    return list_movies()



def get():
    return search_movies()


def add():
    return add_movies()


def main_menu():
    while True:
        action = input("""Choose an action number:
Get all movies: | Find a movie: | Add a movie: | Exit:
       1        |       2       |       3      |   4
                \n """)
        print(f"You have chosen number {action}")
        if action == "1":
            get_all()
        elif action == "2":
            get()
        elif action == "3":
            add()
        elif action == "4":
            print("Thank you for using Lavarenka!")
            exit()
        else:
            print("please choose from the action numbers only\n")
