def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

def count_prime_digit_sums(n):
    """
    Returns the count of numbers in the range [1, n] whose digits sum to a prime number.
    """
    prime_sum_count = 0
    for x in range(1, n + 1):
        if is_prime(digit_sum(x)):
            prime_sum_count += 1
    return prime_sum_count