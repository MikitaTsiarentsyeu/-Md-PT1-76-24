def t_or_f (num):
    if num <= 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0: return False
    return True

def large(num_c):
    max_ = None
    for num in num_c:
        if t_or_f(num):
                if max_ is None or num > max_: max_ = num
    return max_

list_input = input("Enter list numbers: ")
num_c = list(map(int, list_input.split()))
res = large(num_c)

print(res)