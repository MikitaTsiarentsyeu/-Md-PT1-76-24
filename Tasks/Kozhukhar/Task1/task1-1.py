import decimal

cel = decimal.Decimal(input("Please enter degrees Celsius to convert to Fahrenheit: "))
# Works correctly if you enter a period rather than a comma for floating-point values


def cel_to_fahr(cel):
    """Convert Celsius to Fahrenheit"""
    return cel * 9 / 5 + 32


print(f"{cel} degrees Celsius is {cel_to_fahr(cel)} degrees Fahrenheit")
