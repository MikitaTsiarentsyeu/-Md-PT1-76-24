def degree_of_number(number: int, degree: int) -> int:
    """Recursive function to calculate the degree_of_number of a given number."""

    if degree == 0:
        return 1
    return number * degree_of_number(number, degree - 1)


print(degree_of_number(5, 3))
