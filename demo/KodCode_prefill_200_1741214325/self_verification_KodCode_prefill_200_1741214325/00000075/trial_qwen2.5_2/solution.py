def is_perfect_number(num: int) -> bool:
    """
    Checks if the given number is a perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper divisors,
    excluding the number itself.
    """
    if num < 1:
        return False
    divisors_sum = 1  # 1 is a divisor for all positive integers
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:  # add the quotient only if it's different from i
                divisors_sum += num // i
    return divisors_sum == num