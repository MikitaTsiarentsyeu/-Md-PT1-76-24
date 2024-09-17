import math

albums = [
    {"title": "Nevermind", "artist": "Nirvana", "year": 1991, "genre": "rock"},
    {"title": "Forever King", "artist": "50 Cent", "year": 2009, "genre": "rap"},
    {"title": "Speak Now", "artist": "Taylor Swift", "year": 2020, "genre": "pop"},
]
albums_attrs = list(albums[0].keys())

def get_all():
    res = ""
    if albums:
        for p in albums:
            res += f"{album_to_str(p)}\n"
        return res
    return "No albums in the collection."

def get(name):
    for p in albums:
        if p["title"].lower() == name.lower():
            return album_to_str(p)
    return "Album not found."

def add(**album):
    albums.append(album)

def album_to_str(album):
    res = ""
    for key in album:
        res += f"{key.capitalize()}: {album[key]}  "
    return res.strip()

def search(keyword):
    keyword = keyword.lower()
    results = [album_to_str(p) for p in albums if keyword in p["title"].lower() or keyword in p["artist"].lower() or keyword in str(p["year"]) or keyword in p["genre"].lower()]
    return "\n".join(results) if results else "No matching albums found."

def album_from_str(**kwargs):
    album = {}
    for key in albums_attrs:
        if key == "year":
            try:
                album[key] = int(kwargs[key])
            except ValueError:
                album[key] = math.nan
        else:
            album[key] = kwargs[key]
    return album

