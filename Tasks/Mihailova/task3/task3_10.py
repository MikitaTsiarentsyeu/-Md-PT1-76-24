#10. Write a program that takes a list of numbers as input and returns the largest prime number in the list.
user_input = input("Введите числа: ")
numbers = list(map(int, user_input.split()))

max_prime = None  

for num in numbers:  
    if num > 1: 
        is_prime = True 
        if num == 2: 
            is_prime = True
        elif num % 2 == 0:  
            is_prime = False  
        else:
            for i in range(3, int(num**0.5) + 1, 2):  
                if num % i == 0:  
                    is_prime = False
                    break  
        if is_prime:  
           max_prime = num  
print(max_prime)  