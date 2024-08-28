"""
3. Write a recursive function to count the number of occurrences of a given character in a string.
"""

# 1
def count_character_find(my_string:str, character:str, count=0) -> int:
    idx = my_string.find(character)
    if idx == -1:
        return count
    count += 1
    return count_character_find(my_string[idx+1:], character, count)

# 2
def count_character(my_string:str, character:str, count=0) -> int:
    if not my_string:
        return count
    count += my_string[0] == character
    return count_character(my_string[1:], character, count)

print(count_character_find("I love cats, dogs and wild cats", 'a'))
print(count_character("I love cats, dogs and wild cats", 'a'))