## Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
def get_ranges(numbers):
    ranges = []
    start = None
    prev = None
    for num in numbers:
        if start is None:
            start = num
            prev = num
        elif num == prev + 1:
            prev = num
        else:
            if start == prev:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{prev}")
            start = num
            prev = num
    if start is not None:
        if start == prev:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}-{prev}")
    return ", ".join(ranges)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  # Output: 0-4, 7-8, 10
print(get_ranges([4, 7, 10]))  # Output: 4, 7, 10
print(get_ranges([2, 3, 8, 9]))  # Output: 2-3, 8-9
