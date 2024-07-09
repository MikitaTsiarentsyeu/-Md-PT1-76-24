"""
1.Write a program that converts Celsius to Fahrenheit,
  ask a user for the Celsius value.
"""

# N1:
c = int(input())
f = ((c * 9) / 5) + 32
print(f'{c} degrees Celsius is equal to {f} degrees Fahrenheit')

# N2:
c = input()

while True:
    if c.isdigit():
        # checks whether the string consists only of numeric characters
        f = ((int(c) * 9) / 5) + 32
        print(f'{f} F')
        break
    else:
        print('Enter the number')
        c = input()
        continue
