def length_string(user_list: list) -> list:
    """Return List with length string greater than 5"""
    new_list = []
    for item in user_list:
        if isinstance(item, str):
            if len(item) > 5:
                new_list.append(item)
    return new_list


user_list = [546, 6852578, "sdfsdf"]  # result without not string fotmat
print(length_string(user_list))
user_list = ["12345", "98765324234", "abcdefsdfsdf"]
print(length_string(user_list))
