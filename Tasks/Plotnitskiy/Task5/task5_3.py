def filter_strings(list_of_strings):
    return [s for s in list_of_strings if len(s) > 5]


print(filter_strings(["Python", "is", "a", "high-level", "programming", "language"]))
