#5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
#get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
#get_ranges([4,7,10])  -> "4, 7, 10"
#get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
def get_ranges(numbers):
    if not numbers:
        return ""
    
    ranges = []
    start = numbers[0]
    end = numbers[0]
    
    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}-{end}")
            start = num
            end = num
    
    if start == end:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}-{end}")
    
    return ", ".join(ranges)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  
print(get_ranges([4, 7, 10]))                 
print(get_ranges([2, 3, 8, 9]))               
