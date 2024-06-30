'''
  Write a program that converts some amount of money from USD to BYN, 
  ask a user for the amount, 
  store the ratio inside the program itself.
'''

try:
    usd = float(input('Please, input amount of money (USD): '))
    if usd > 0:
        RATIO = 3.27
        byn = round(RATIO * usd, 3)
        print(f'Amount of money (BYN): {byn}')
    else:
        print("Amount of money should be a positive number")
except ValueError:
    print('Not a number, please retry')
