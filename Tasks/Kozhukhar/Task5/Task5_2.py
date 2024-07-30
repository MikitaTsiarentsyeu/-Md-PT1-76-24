def reverse_str_in_list(user_list: list) -> list:
    """Return str in List reverse if str, if not then don't reverse item"""
    reverse_list = []
    for item in user_list:
        if isinstance(item, str):
            reverse_list.append(item[::-1])
        else:
            reverse_list.append(item)
    return reverse_list


user_list = [546, 68525, "sdfsdf"]  # reverse only if string format
print(reverse_str_in_list(user_list))
user_list = ["123456", "98765", "abcdef"]
print(reverse_str_in_list(user_list))
