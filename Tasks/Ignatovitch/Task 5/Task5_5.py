def get_ranges(numbers):
    if len(numbers) == 0:
        return ""
    
    start = numbers[0]
    i = 0
    
    while i + 1 < len(numbers) and numbers[i + 1] == numbers[i] + 1:
        i += 1
    
    end = numbers[i]

    if start == end:
        range_str = f"{start}"
    else:
        range_str = f"{start}-{end}"
    
    rest = get_ranges(numbers[i + 1:])
    
    if rest:
        return range_str + ", " + rest
    else:
        return range_str

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10])) 
print(get_ranges([4, 7, 10]))                
print(get_ranges([2, 3, 8, 9])) 