def decimal_to_binary(number):
    if number == 0:
        return '0'
    binary_digits = []
    while number > 0:
        remainder = number % 2
        binary_digits.append(remainder)
        number = number // 2
    binary_digits.reverse()
    return ''.join(map(str, binary_digits))