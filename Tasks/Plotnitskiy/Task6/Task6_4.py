def exponentiate(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / exponentiate(base, -exp)
    else:
        return base * exponentiate(base, exp - 1)


print(exponentiate(2, 3))
print(exponentiate(2, -1))
