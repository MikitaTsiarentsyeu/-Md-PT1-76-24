def count_abc():
    line = input("Введите строку: ")
    
    smool = sum(1 for sub in line if sub.islower())
    big = sum(1 for sub in line if sub.isupper())
    
    return smool, big

lower, upper = count_abc()
print(f"Количество строчных букв: {lower}, количество прописных букв: {upper}")

#OR

def count_cba(line):
    smool2 = sum(1 for sub in line if sub.islower())
    big2 = sum(1 for sub in line if sub.isupper())
    
    return smool2, big2

result = count_cba("Write a function that takEs two integers as Arguments and reTurns their sum.")
lower2, upper2 = result
print(f"Количество строчных букв: {lower2}, количество прописных букв: {upper2}")