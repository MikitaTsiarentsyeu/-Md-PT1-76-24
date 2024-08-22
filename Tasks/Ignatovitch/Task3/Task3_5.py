user_input = input("Enter a list of strings separated by spaces: ").split()

result = []

for string in user_input:
    if len(string) > 5:
        result.append(string)
        print("Strings with length greater than 5 characters:", result)
    else:
        print("There are no words with length greater than 5 characters")

