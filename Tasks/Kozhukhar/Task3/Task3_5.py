def fivelong(strings):
    """Return list only with 5 long strings"""
    return [s for s in strings if len(s) > 5]


input_strings = input("Enter the lines separated by commas: ").split(",")

input_strings = [s.strip() for s in input_strings]  # delete spaces

print("Lines longer than 5 characters:", fivelong(input_strings))
