from .backand_movies import list_movies, add_movies, search_movies


def get_all():
    """
    we call the function to view all movies
    """
    return list_movies()


def get():
    """
    call the movie search function
    """
    return search_movies()


def add():
    """
    call the function to add a movie
    """
    return add_movies()


def main_menu():
    """
    application menu
    """
    while True:
        action = input("""Choose an action number:
Get all movies: | Find a movie: | Add a movie: | Exit:
       1        |       2       |       3      |   4
                \n """)
        print(f"You have chosen number: {action}")
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
