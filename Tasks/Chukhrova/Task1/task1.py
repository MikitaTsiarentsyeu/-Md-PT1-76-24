''' 
  Write a program that converts Celsius to Fahrenheit, 
  ask a user for the Celsius value. 
'''


try:
    celsius = float(input('Please, input Celsius value: '))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f'Fahrenheit value: {fahrenheit}')
except ValueError:
    print('Not a number, please retry')