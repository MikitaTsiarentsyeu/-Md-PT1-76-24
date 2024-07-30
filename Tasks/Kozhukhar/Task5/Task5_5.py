def output_numbers_result(user_list: list) -> str:
    """Return result such as get_ranges([2, 3, 8, 9])  -> "2-3, 8-9" """
    new_list = []
    new_string = ""
    first_count = user_list[0]
    last_count = user_list[0]
    for i in range(1, len(user_list)):
        if (user_list[i] - user_list[i - 1]) == 1:
            last_count = user_list[i]
        else:
            if first_count == last_count:
                new_list.append(f"{first_count}")
            else:
                new_list.append(f"{first_count} - {last_count}")
            first_count = user_list[i]
            last_count = user_list[i]
    if first_count == last_count:
        new_list.append(f"{first_count}")
    else:
        new_list.append(f"{first_count} - {last_count}")

    new_string = ", ".join(new_list)

    return new_string


user_list = [3, 4, 5, 6, 9, 11, 15, 16, 17, 18, 20, 23, 24, 25, 26, 100, 101, 200]
print(output_numbers_result(user_list))
