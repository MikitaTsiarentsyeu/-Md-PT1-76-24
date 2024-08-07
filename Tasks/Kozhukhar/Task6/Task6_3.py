def symbol_count(s: str, symbol: str) -> int:
    """Recursive function to count the number of occurrences of a given character in a string"""
    if not s:
        return 0
    count = 1 if s[0] == symbol else 0
    return count + symbol_count(s[1:], symbol)


string = "123456ffff123123"
counting_symbol = "1"
print(symbol_count(string, counting_symbol))
