def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_sum(n):
    """Calculate the sum of the digits of n."""
    return sum(int(digit) for digit in str(n))

def count_prime_digit_sums(n):
    """
    Count the number of integers x in the range [1, n] such that the sum of the digits of x is a prime number.
    """
    return sum(is_prime(digit_sum(x)) for x in range(1, n + 1))