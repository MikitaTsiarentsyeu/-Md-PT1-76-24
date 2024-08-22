def count_vowels(input_str):
    """Count vowels"""
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for symbol in input_str:
        if symbol in vowels:
            count += 1
    return count


user_input = input("Enter string: ")

print("Number of vowels in the string: ", count_vowels(user_input))
