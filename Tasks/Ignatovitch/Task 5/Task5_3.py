def my_string(strings):
    if len(strings) == 0:
        return []
    if len(strings[0]) > 5:
        return [strings[0]] + my_string(strings[1:])
    else:
        return my_string(strings[1:])

print(my_string (["hello", "world", "granny", "Belarus", "result"]))