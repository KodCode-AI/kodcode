def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def digit_sum(num):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(num))

def count_prime_digit_sum(n):
    """
    Return the count of numbers in [1, n] whose digit sum is a prime number.
    """
    count = 0
    for x in range(1, n + 1):
        if is_prime(digit_sum(x)):
            count += 1
    return count