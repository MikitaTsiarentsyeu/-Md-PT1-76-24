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
"""

from movies import ui_movies

print(ui_movies.main_menu())











