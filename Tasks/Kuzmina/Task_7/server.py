import json
import os

class Collection:
    def __init__(self, filename='collection.json'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        else:
            self.data = []

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_item(self, title, artist_or_director, year, genre):
        item = {
            "title": title,
            "artist_or_director": artist_or_director,
            "year": year,
            "genre": genre
        }
        self.data.append(item)
        self.save_data()

    def list_items(self):
        return self.data

    def find_items(self, search_term):
        results = []
        for item in self.data:
            if (search_term.lower() in item["title"].lower() or
                search_term.lower() in item["artist_or_director"].lower() or
                search_term.lower() in str(item["year"]) or
                search_term.lower() in item["genre"].lower()):
                results.append(item)
        return results