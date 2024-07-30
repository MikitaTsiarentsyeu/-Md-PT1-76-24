def sum_two_integer(term1: int, term2: int) -> int:
    """Sum of two integer. If both are not integer, then None"""
    if isinstance(term1, int) and isinstance(term2, int):
        return term1 + term2


# I also could get result as string format and work with exception but in my opinion integer as result more important

print(sum_two_integer(5, 5))
print(sum_two_integer(5, 5.5))
print(sum_two_integer(5, "A"))
print(sum_two_integer(5, 500))
