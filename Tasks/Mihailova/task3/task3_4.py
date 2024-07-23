user_input = input("Введите числа: ")
numbers = list(map(int, user_input.split()))
if len(numbers) < 2:
    print("Список должен содержать как минимум два числа.")
else:
   numbers.sort()
   second_largest = numbers[-2]
    
print("Второе по величине число:", second_largest)
