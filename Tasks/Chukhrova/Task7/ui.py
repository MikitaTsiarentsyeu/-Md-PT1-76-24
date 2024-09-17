"""
You need to write a program that has two modules: a back-end one and a console front-end one.
The program should allow the user to store and browse information about either musical albums or movies (or any other digital entity).
The back-end module should store the data on disk using any applicable format.
"""
import bl


def get_all_cats():
    cats = bl.get_all()
    if cats:
        print(cats)
    else:
        print("Sorry, empty!")


def get_cat_by_breed():
    breed = input("Select breed: ")
    cat = bl.get(breed)
    if cat:
        print(cat)
    else:
        print("Sorry, empty!")


def add_new_cat():
    cat = {}
    for attr in bl.cats_attr:
        cat[attr] = input(f'Write {attr}: ')
    bl.add(**cat)


def menu():
    while True:
        try:
            user_choice = int(input("""\nPlease, select option:
1. Show all cats
2. Show cat by breed
3. Add a new cat
4. Exit
Your choice: """))
        except ValueError:
            print("Not a number...")
            continue
        if user_choice == 1:
            get_all_cats()
        elif user_choice == 2:
            get_cat_by_breed()
        elif user_choice == 3:
            add_new_cat()
        elif user_choice == 4:
            exit()
        else:
            print("We don't have such option, please retry...")

menu()