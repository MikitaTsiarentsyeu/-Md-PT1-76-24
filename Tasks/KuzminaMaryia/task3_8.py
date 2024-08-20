num_r = input("Введите список чисел через пробел: ")
num = list(map(int, num_r.split()))
summ = len(num)
num_rr = sum(int(e) for e in num_r.split())

x = int(num_rr / summ)

print(x)