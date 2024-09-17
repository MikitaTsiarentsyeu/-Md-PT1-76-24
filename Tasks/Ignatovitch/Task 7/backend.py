import json
import os

class Collection:
    def __init__(self, filename='collection.json'):
        self.filename = filename
        self.load()

    def load(self):
        """Load the collection from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.items = json.load(file)
        else:
            self.items = []

    def save(self):
        """Save the collection to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.items, file, indent=4)

    def add_item(self, title, artist_or_director, year, genre):
        """Add a new item to the collection."""
        item = {
            'title': title,
            'artist_or_director': artist_or_director,
            'year': year,
            'genre': genre
        }
        self.items.append(item)
        self.save()

    def list_items(self):
        """List all items in the collection."""
        return self.items

    def search_items(self, **kwargs):
        """Search for items based on various parameters."""
        results = self.items
        for key, value in kwargs.items():
            results = [item for item in results if str(item.get(key)).lower() == str(value).lower()]
        return results