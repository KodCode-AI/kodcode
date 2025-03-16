def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return '0'
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(remainder)
        n = n // 2
    binary_digits.reverse()
    return ''.join(map(str, binary_digits))