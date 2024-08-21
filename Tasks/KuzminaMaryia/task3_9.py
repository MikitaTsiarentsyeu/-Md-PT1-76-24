def revers1(variable):
    result = ""
    for i in range(len(variable) -1, -1, -1):
        result += variable[i]
    return result

my_list_input = revers1(input("Enter text: "))


print(my_list_input)