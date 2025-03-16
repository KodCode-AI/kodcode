import math

def is_prime(num):
    if not isinstance(num, int):
        return False
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = math.sqrt(num)
    for i in range(3, int(max_divisor) + 1, 2):
        if num % i == 0:
            return False
    return True