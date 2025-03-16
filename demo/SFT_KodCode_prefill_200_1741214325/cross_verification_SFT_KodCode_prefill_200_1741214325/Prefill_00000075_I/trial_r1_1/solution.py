import math

def is_perfect_number(n):
    if n <= 1:
        return False
    sum_div = 1  # 1 is a proper divisor for n > 1
    sqrt_n = int(math.sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            # Check if the divisor is not the number itself
            if i != n:
                sum_div += i
            counterpart = n // i
            # Check counterpart is different from i and not equal to n
            if counterpart != i and counterpart != n:
                sum_div += counterpart
    return sum_div == n