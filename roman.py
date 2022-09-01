
def decrement_value(symbol):
    base_symbol = symbol[-1]
    base_value = convert_to_roman_symbol(base_symbol)

    decrement_value = 0
    increment_value = 0
    for s in symbol[:-1]:
        if s is not base_symbol:
            value = int(convert_to_roman_symbol(s))
            decrement_value += value
        else:
            value = int(convert_to_roman_symbol(s))
            increment_value += value

    symbol_value = (base_value + increment_value) - decrement_value
    return symbol_value

def increment_value(symbol):
    base_value = convert_to_roman_symbol(symbol[0])

    increment_value = 0
    for s in symbol[1:]:
        value = int(convert_to_roman_symbol(s))
        increment_value += value

    symbol_value = base_value + increment_value
    return symbol_value

def convert_to_roman_symbol(symbol):
    dictionary = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }

    big_symbol = len(symbol) > 1
    if big_symbol:

        first_value = convert_to_roman_symbol(symbol[0])
        last_value = convert_to_roman_symbol(symbol[-1])
        decrement = last_value > first_value

        if decrement:
            symbol_value = decrement_value(symbol)

        if not decrement:
            symbol_value = increment_value(symbol)

    if not big_symbol:
        symbol_value = dictionary.get(symbol)

    if symbol_value is None:
        raise ValueError("Invalid symbol")    

    return symbol_value