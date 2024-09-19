def palindrome_rec():
    s = input("Введите строку: ")
    
    s = ''.join(s.split()).lower()
    
    def palindrome_rec(sub_str):
        if len(sub_str) <= 1:
            return True
        if sub_str[0] != sub_str[-1]:
            return False
        return palindrome_rec(sub_str[1:-1])

    if palindrome_rec(s):
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")

palindrome_rec()