"""
You need to write a program that has two modules: a back-end one and a console front-end one.
The program should allow the user to store and browse information about either musical albums or movies (or any other digital entity).
The back-end module should store the data on disk using any applicable format.

Each item should have the following parameters:
title: The title of the album or movie.
artist or director: The artist or director of the album or movie.
year: The year the album or movie was released.
genre: The genre of the album or movie.

The console front-end module should allow the user to perform the following actions:
Add a new album or movie to the collection.
List all albums or movies in the collection.
Search for an album or movie by title, artist/director, year, or genre.
Quit the program.

Вам необходимо написать программу, которая имеет два модуля: внутренний и консольный интерфейс.
Программа должна позволять пользователю хранить и просматривать информацию о музыкальных альбомах или фильмах (или любой другой цифровой сущности).
Бэкенд-модуль должен хранить данные на диске в любом применимом формате.

Каждый элемент должен иметь следующие параметры:
title: Название альбома или фильма.
artist or director: Артист или режиссер альбома или фильма.
year: Год выпуска альбома или фильма.
genre: Жанр альбома или фильма.

Консольный интерфейсный модуль должен позволять пользователю выполнять следующие действия:
Добавлять новый альбом или фильм в коллекцию.
Выводить список всех альбомов или фильмов в коллекции.
Искать альбом или фильм по названию, исполнителю/режиссеру, году или жанру.
Выйти из программы.
"""


from movies import ui_movies

print(ui_movies.main_menu())











