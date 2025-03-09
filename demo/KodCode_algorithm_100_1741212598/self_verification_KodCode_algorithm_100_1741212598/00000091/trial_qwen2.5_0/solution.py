def calculate_distinct_prime_factors(n):
    """
    Returns the number of distinct prime factors of n.
    """
    if n < 2:
        return 0
    
    count = 0
    # Check for number of 2s that divide n
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
    
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        # While i divides n, count i and divide n
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    
    # This condition is to handle the case when n is a prime number
    # greater than 2
    if n > 2:
        count += 1
    
    return count