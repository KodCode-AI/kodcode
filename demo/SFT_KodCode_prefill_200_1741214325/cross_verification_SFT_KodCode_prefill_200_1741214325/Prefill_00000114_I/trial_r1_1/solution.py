def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if n % divisor == 0:
            return False
    return True