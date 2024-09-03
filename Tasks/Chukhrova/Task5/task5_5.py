"""
5. Write a function that takes an ordered list of numbers without duplicates and 
returns a string with ranges for those numbers, check the example below:
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
"""


def get_ranges(l:list):
    ranges = []
    start = l[0]
    end = l[0]
    for idx in range(1, len(l)):
        if end+1 == l[idx]:
            end = l[idx]
        else:
            ranges.append(str(start) + ("" if start == end else f"-{end}"))
            start = end = l[idx]
    ranges.append(str(start) + ("" if start == end else f"-{end}"))
    return ", ".join(ranges)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))