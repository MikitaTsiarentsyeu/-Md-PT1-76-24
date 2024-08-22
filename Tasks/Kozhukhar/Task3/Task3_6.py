def delete_vowels(input_str):
    """Delete vowels from the input string"""
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    new_str = ""
    for symbol in input_str:
        if symbol not in vowels:
            new_str += symbol
    return new_str


user_input = input("Enter string: ")

print("String without vowels: ", delete_vowels(user_input))
