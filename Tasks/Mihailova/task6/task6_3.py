#3. def count_occurrences(string, char):

def count_occurrences(string, char):
    if not string:
        return 0
    
    if string[0] == char:
        return 1 + count_occurrences(string[1:], char)
    
    return count_occurrences(string[1:], char)


string = "Hello world!"
print(string)
char = input("Введите букву: ")
result = count_occurrences(string, char)
print(f"Символ '{char}' встречается в строке '{string}' {result} раз(а).")
