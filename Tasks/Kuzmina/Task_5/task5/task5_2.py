def my_func(spisochek: list) -> list:
    retus = []
    for lis in spisochek:
        if isinstance(lis, str):
            retus.append(lis[::-1])
        else:
            retus.append(lis)
    return retus


spisochek = ['Write', 'function', 'takes', 'list', 'strings', 'argument']
print(my_func(spisochek))


#  ОR


def alter_revers():
    
    retusovka = input("Введите строки, разделённые запятыми: ").split(',')
    
    ticl = [g.strip()[::-1] for g in retusovka]
    
    return ticl

d = alter_revers()

print("Перевёрнутые строки:", d)