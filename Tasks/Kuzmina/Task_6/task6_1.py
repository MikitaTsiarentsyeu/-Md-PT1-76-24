def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    
    
user_input = input("Введите строку для обращения: ")
reversed_string = reverse_string(user_input)
print("Обращённая строка:", reversed_string)