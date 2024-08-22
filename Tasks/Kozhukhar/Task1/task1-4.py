import decimal

rate = decimal.Decimal("3.20")


def convert(usd, rate):
    """Converts USD to BYN"""
    return usd * rate


try:
    usd = decimal.Decimal(input("Please enter the amount in USD: "))
    byn = convert(usd, rate)
    print(f"{usd} USD is equal to {byn:.2f} BYN")
except decimal.InvalidOperation:
    print("Invalid input. Please enter a valid number.")
