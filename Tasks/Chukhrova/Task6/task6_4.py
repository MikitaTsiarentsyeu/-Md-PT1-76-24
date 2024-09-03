"""
4. Write a recursive function to calculate the power of a given number.
"""

def power_number(number:int, power:int) -> int:
    if not power:
        return 1
    elif power > 0:
        return number * power_number(number, power-1)
    else:
        return 1/power_number(number, -power)


print(power_number(2,5))
print(power_number(2,0))
print(power_number(2,-2))