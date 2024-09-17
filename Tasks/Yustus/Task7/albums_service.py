import json
import os

def load_json():
    if os.path.exists('database/albums.json'):
        with open('database/albums.json', 'r') as file:
            albums = json.load(file)
        return albums
    else:
        return []

def list_albums():
    albums = load_json()
    if albums:
        for album in albums:
            print(f"Title: {album['title']}, Director: {album['artist']}, Year: {album['year']}, Genre: {', '.join(album['genre'])}")
    else:
        print("No albums found. Would you like to add an album? (y/n)")
        choice = input().lower()
        if choice == 'y':
            add_album()

def add_album():
    albums = load_json()
    title = input("Enter the album title: ")
    artist = input("Enter the artist's name: ")
    year = input("Enter the release year: ")
    genre = input("Enter the genre(s) separated by commas: ").split(',')
    genre = [g.strip() for g in genre]

    new_album = {
        "title": title,
        "director": artist,
        "year": year,
        "genre": genre
    }

    albums.append(new_album)
    with open('albums.json', 'w') as file:
        json.dump(albums, file, indent=4)

    print("Album added successfully!")

def get_album_by_title(title):
    albums = load_json()
    for album in albums:
        if album['title'].lower() == title.lower():
            return album
    return None

def get_albums_by_artist(artist):
    albums = load_json()
    return [album for album in albums if album['artist'].lower() == artist.lower()]

def get_albums_by_year(year):
        albums = load_json()
        return [album for album in albums if album['year'] == year]

def get_albums_by_genre(albums, genre):
    albums = load_json()
    return [album for album in albums if genre.lower() in [g.lower() for g in album['genre']]]

def album_to_str(album):
    print(f"Title: {album['title']}, Director: {album['artist']}, Year: {album['year']}, Genre: {', '.join(album['genre'])}")
