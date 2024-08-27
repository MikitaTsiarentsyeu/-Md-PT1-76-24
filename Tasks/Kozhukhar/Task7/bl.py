import json
import os


class MusicFilms:
    def __init__(self, file_path="music_films_base.json"):
        self.file_path = file_path
        self.data = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.data = json.load(file)
        else:
            self.data = []

    def save_data(self):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_data(self, title, artist_or_director, year, genre):
        self.data.append(
            {
                "title": title,
                "artist_or_director": artist_or_director,
                "year": year,
                "genre": genre,
            }
        )
        self.save_data()

    def list_media(self):
        return self.data

    def find_media(self, **kwargs):
        results = []
        for media in self.data:
            if all(
                media[key].lower() == value.lower()
                for key, value in kwargs.items()
                if value
            ):
                results.append(media)
        return results
