def is_perfect_number(n):
    """
    Returns True if n is a perfect number, False otherwise.
    A perfect number is a positive integer that is equal to the sum of its proper divisors,
    excluding the number itself. For example, 6 is a perfect number because 1 + 2 + 3 = 6.
    """
    if n < 1:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n