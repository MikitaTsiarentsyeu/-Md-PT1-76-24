"""
    5. Write a function that takes an ordered list of numbers without duplicates
    and returns a string with ranges for those numbers, check the example below:
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
    get_ranges([4,7,10])  -> "4, 7, 10"
    get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

    5. Напишите функцию, которая принимает упорядоченный список чисел
    без дубликатов и возвращает строку с диапазонами для этих чисел, проверьте пример ниже:
"""


def get_ranges(numbers):
    res = [numbers[0]]
    my_list = []
    for number in range(1, len(numbers)):
        if numbers[number] - numbers[number - 1] == 1:
            res.append(numbers[number])
            if number == len(numbers) - 1:
                res.append(numbers[number])
                my_list.append(f'{res[0]}-{res[-1]}') if len(res) > 1 else my_list.append(f'{res[0]}')
        else:
            my_list.append(f'{res[0]}-{res[-1]}') if len(res) > 1 else my_list.append(f'{res[0]}')
            res = []
            res.append(numbers[number])
            if number == len(numbers) - 1:
                my_list.append(f'{res[0]}')
    return f'"{", ".join(my_list)}"'


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print()
print(get_ranges([2, 3, 8, 9]))
print()
print(get_ranges([4, 7, 10, 11, 12, 34, 35, 36]))
