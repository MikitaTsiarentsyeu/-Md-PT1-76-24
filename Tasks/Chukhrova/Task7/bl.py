import json


CATS_BD = "cats.json"
cats_attr = ["name", "breed", "age", "size"]


def get_all():
    try:
        with open(CATS_BD, 'r', encoding='utf-8') as f:
            cats_from_json = json.load(f)
            all_cats = ""
            for cat in cats_from_json:
                if cat["age"] == "null":
                    cat["age"] = "-"
                all_cats = f'{all_cats} {cat_to_str(cat)}\n'
            return all_cats.rstrip()
    except FileNotFoundError:
        return ""
    

def get(breed):
    try:
        with open(CATS_BD, 'r', encoding='utf-8') as f:
            cats_from_json = json.load(f)
            for cat in cats_from_json:
                if cat["breed"].lower() == breed.lower():
                    if cat["age"] == "null":
                        cat["age"] = "-"
                    return cat_to_str(cat)
    except FileNotFoundError:
        return ""
    else:
        return ""
    

def add(**cat):
    try:
        with open(CATS_BD, 'r', encoding='utf-8') as f:
            l = json.load(f)
    except FileNotFoundError:
        l = []
    if not cat["age"].isdigit():
        cat["age"] = "null"
    l.append(cat)
    with open(CATS_BD, 'w', encoding='utf-8') as f:
        json.dump(l, f)


def cat_to_str(cat):
    res = ""
    for key in cat:
        res = f"{res} {key}:'{cat[key]}'"
    return res.lstrip()