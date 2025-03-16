def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(remainder)
        n = n // 2
    binary_digits.reverse()
    return ''.join(str(digit) for digit in binary_digits)