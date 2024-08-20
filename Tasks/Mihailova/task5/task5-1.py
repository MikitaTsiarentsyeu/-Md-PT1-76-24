#1. Write a function that takes two integers as arguments and returns their sum.


while True:
    user_input = input("Введите 2 числа: ")
    numbers = user_input.split()

    if len(numbers) != 2:
        print("Ошибка: необходимо ввести ровно два числа.")
        continue
    
    try:
        a, b = map(int, numbers)
        break  
    except ValueError:
        print("Ошибка: оба значения должны быть числами.")

def int_sum(a, b):
    return a + b

result = int_sum(a, b)
print(result)
