def list_5():
    listd = input("Введите строки, разделённые запятыми: ").split(',')
    
    long = [i.strip() for i in listd if len(i.strip()) > 5]

    return long

result = list_5()
print("Строки длиной более 5 символов:", result)


#  ОR


def filter_list(spisok):
    long = [line for line in spisok if len(line) > 5]
    
    return long

long_line = ["Write", "function", "that", "takes", "strings"]
result2 = filter_list(long_line)

print("Строки длиной более 5 символов:", result2)