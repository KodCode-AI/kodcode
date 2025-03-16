def decimal_to_binary(n):
    if n == 0:
        return '0'
    bits = []
    while n > 0:
        remainder = n % 2
        bits.append(str(remainder))
        n = n // 2
    bits.reverse()
    return ''.join(bits)