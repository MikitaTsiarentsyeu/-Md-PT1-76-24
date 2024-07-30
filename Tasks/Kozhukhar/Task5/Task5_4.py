def count_letters(user_string: str) -> str:
    """Count Upper and Lower letters"""
    upper_count = 0
    low_count = 0
    if isinstance(user_string, str):
        for item in user_string:
            if item.isupper():
                upper_count += 1
            elif item.islower():
                low_count += 1
    return f"{upper_count} upper letters , {low_count} lower letters"


user_string = "AAA3aaaaa5987&)"
print(count_letters(user_string))
