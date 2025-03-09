def efficient_prime_factors(n):
    """Efficiently returns prime factors of n."""
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
    """Calculates the Liouville Lambda function value for n."""
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    
    factors = efficient_prime_factors(n)
    # Since duplicates are allowed in prime factors, we need to count unique factors and their powers.
    factor_counts = {factor: factors.count(factor) for factor in set(factors)}
    
    # Liouville Lambda is -1 if the number of prime factors with odd power is odd, 1 otherwise.
    lambda_val = 1
    for count in factor_counts.values():
        if count % 2 != 0:
            lambda_val *= -1
            
    return lambda_val