def get_ranges(my_list):
    ranges = []
    start = end = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] != end + 1:
            ranges.append((start, end))
            start = end = my_list[i]
        else:
            end = my_list[i]
    ranges.append((start, end))
    result = []
    for start, end in ranges:
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")
    return ", ".join(result)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))