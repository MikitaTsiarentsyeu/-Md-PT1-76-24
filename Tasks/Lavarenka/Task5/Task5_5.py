"""
    5. Write a function that takes an ordered list of numbers without duplicates
    and returns a string with ranges for those numbers, check the example below:
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
    get_ranges([4,7,10])  -> "4, 7, 10"
    get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
"""


def get_ranges(numbers: list) -> str:
    """
    A function that takes an ordered list of numbers without
    duplicates and returns a string with ranges for those numbers.
    """
    interim_list = [numbers[0]]  # we start from index 1, so in interim_list we write index 0
    res = []
    for number in range(1, len(numbers)):
        if numbers[number] - numbers[number - 1] != 1:
            # if the sequence is broken, we write it down in the res and start the sequence over again
            res.append(f'{interim_list[0]}-{interim_list[-1]}') if len(interim_list) > 1 else res.append(
                f'{interim_list[0]}')
            interim_list = []
        interim_list.append(numbers[number])

        if number == len(numbers) - 1:
            # catches the last number or sequence and writes it to the res
            res.append(f'{interim_list[0]}-{interim_list[-1]}') if len(interim_list) > 1 else res.append(
                f'{interim_list[0]}')
    return f'"{", ".join(res)}"'


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print()
print(get_ranges([2, 3, 8, 9]))
print()
print(get_ranges([4, 7, 10, 11, 12, 34, 35, 36]))
