def count_occur(s, char):
    if len(s) == 0:
        return 0
    if s[0] == char:
        return 1 + count_occur(s[1:], char)
    else:
        return count_occur(s[1:], char)

def main():
    s = input("Введите строку: ")
    char = input("Введите символ для подсчета: ")

    if len(char) != 1:
        print("Пожалуйста, введите только один символ.")
        return

    count = count_occur(s, char)

    print(f"Количество вхождений символа '{char}' в строке: {count}")

main()