rate = 3.2
usd = float(input("Please enter the amount in USD: "))


def convert(usd, rate):
    """Converts USD to BYN"""
    return usd * rate


print(f"{usd} USD is equal to {convert(usd, rate):.2f} BYN")
