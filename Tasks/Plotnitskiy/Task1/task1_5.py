import random  # импортирую модуль random для генерации случайного числа

left = int(input("Please enter the left border of the range: "))
right = int(input("Please enter the right border of the range: "))
random_number = random.randint(
    left, right
)  # генерируем случайное число в введенном диапазоне с помощью метода .randint (но только целое число и только с использованием функции int, если хочу генерировать случайные нецелые числа, то тогда нужно использовать метод random.uniform и функцию float)
print("The random number in the given range is: ", random_number)
