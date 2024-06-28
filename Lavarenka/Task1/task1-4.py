"""
4.Write a program that converts some amount of money from USD to BYN, ask a user for the amount,
store the ratio inside the program itself.
"""

# 4. Напишите программу, конвертирующую некоторую сумму денег из долларов США в белорусские рубли,
# запросите у пользователя сумму,
# сохраните соотношение внутри самой программы.

dollar = 3.27  # 1$ == 3,27 byn

sum_byn = int(input('Enter dollar amount: ')) * dollar

print(sum_byn)


