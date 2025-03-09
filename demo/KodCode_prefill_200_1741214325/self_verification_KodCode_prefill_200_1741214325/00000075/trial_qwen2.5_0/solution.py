def is_perfect_number(number):
    """
    Returns True if the given number is a perfect number, False otherwise.
    A perfect number is a positive integer that is equal to the sum of its proper divisors.
    """
    if number <= 1:
        return False
    divisors_sum = sum([i for i in range(1, number) if number % i == 0])
    return divisors_sum == number