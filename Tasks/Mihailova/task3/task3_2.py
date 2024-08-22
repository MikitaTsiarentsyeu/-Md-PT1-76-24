user_input = input("Введите числа:")
numbers = user_input.split()
even_numbers = 0
for num in numbers:
    num = int(num)
    if num % 2 == 0:
        even_numbers += num


print(even_numbers)
    