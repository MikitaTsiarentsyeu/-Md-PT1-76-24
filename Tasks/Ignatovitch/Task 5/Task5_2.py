def reversed_string (string):
    if len(string) == 0:
        return []
    else:
        return [s[::-1] for s in string]

print(reversed_string (["hello", "buy", "mummy"]))