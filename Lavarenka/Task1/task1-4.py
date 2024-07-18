"""
4.Write a program that converts some amount of money from USD to BYN, ask a user for the amount,
store the ratio inside the program itself.
"""

# for more accurate calculations you can use the module Decimal
dollar = 3.27  # 1$ == 3,27 byn

sum_byn = int(input('Enter dollar amount: ')) * dollar

print(f"Your summ: {sum_byn} byn")
