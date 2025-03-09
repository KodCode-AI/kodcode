def calculate_distinct_prime_factors(n: int) -> int:
    """
    Returns the number of distinct prime factors of n.
    """
    if n <= 1:
        return 0
    
    distinct_factors = set()
    # Check divisibility by 2
    if n % 2 == 0:
        distinct_factors.add(2)
        while n % 2 == 0:
            n //= 2
    
    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            distinct_factors.add(i)
            while n % i == 0:
                n //= i
    
    # If n is a prime number and greater than 2
    if n > 2:
        distinct_factors.add(n)
    
    return len(distinct_factors)