def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

result = power(2, 3) 
print(result) 

result_negative = power(2, -3)  
print(result_negative)  