## Write a recursive function to calculate the power of a given number.
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)

print(power(2, 8))