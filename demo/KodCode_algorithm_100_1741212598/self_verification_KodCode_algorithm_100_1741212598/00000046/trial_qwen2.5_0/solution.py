def efficient_prime_factors(n):
    """
    Returns a list of prime factors of n in ascending order.
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def liouville_lambda(n):
    """
    Returns 1 if the number of prime factors (counting multiplicity) is even,
    -1 if it is odd.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    factors = efficient_prime_factors(n)
    return -1 if len(factors) % 2 != 0 else 1