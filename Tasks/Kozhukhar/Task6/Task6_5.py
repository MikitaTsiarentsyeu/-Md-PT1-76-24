def fibonacci(n: int) -> int:
    """Recursive function to find the Nth number in the Fibonacci sequence."""

    if n == 1:
        return 0
    elif n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the Nth position in the Fibonacci sequence: "))

print(f"The answer is {fibonacci(n)}")
