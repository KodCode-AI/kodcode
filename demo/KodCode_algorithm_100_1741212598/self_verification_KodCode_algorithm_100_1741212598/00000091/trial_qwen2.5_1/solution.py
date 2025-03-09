def calculate_distinct_prime_factors(n: int) -> int:
    """
    Returns the number of distinct prime factors of the given number n.
    """
    count = 0
    i = 2
    # Check for each number from 2 to the square root of n
    while i * i <= n:
        # If i is a prime factor
        if n % i == 0:
            count += 1
            # Divide n by this prime factor and check for the next
            while n % i == 0:
                n //= i
        i += 1
    # If n is a prime number greater than 2
    if n > 1:
        count += 1
    return count