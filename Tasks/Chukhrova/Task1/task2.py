import math

'''
  Write a program that calculates the area of a circle given its radius, 
  ask a user for the radius.
'''


try:
    radius = float(input('Please, input radius: '))
    if radius > 0:
        area = round(math.pi * radius**2, 6)
        print(f'Area of a circle: {area}')
    else:
        print("Radius should be a positive number")
except ValueError:
    print('Not a number, please retry')