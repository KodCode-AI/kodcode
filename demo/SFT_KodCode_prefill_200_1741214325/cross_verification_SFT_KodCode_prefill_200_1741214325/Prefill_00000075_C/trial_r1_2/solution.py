import math

def is_perfect_number(num: int) -> bool:
    """
    Checks if the given number is a perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper divisors,
    excluding the number itself.
    """
    if num <= 0:
        return False
    total = 0
    sqrt_num = int(math.sqrt(num))
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            # Add divisor i if it's not the number itself
            if i != num:
                total += i
            # Calculate the corresponding divisor
            j = num // i
            # Add divisor j if it's different from i and not the number itself
            if j != i and j != num:
                total += j
    return total == num