def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

def main():
    base = float(input("Введите основание: "))
    exponent = int(input("Введите степень: "))

    result = power(base, exponent)

    print(f"{base} в степени {exponent} равно {result}")

main()