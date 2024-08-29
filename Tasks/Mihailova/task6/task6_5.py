#5. Write a recursive function to find the Nth number in the Fibonacci sequence.

#0, 1, 1, 2, 3, 5, 8, 13, 21

#n = 6 => 5

def fibonacci(n):
    if n == 1:
        return 0  
    elif n == 2:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  

n = 9
print(fibonacci(n))  
