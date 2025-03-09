def prime_factors(n):
    """Return the list of prime factors of n."""
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

def liouville_lambda(value):
    """
    Returns the Liouville Lambda value for a given integer or a list of integers.
    """
    if not isinstance(value, list):
        value = [value]  # Wrap single value in a list for consistency

    results = []
    for val in value:
        if val <= 0:
            results.append(0)  # Return 0 for non-positive values
        else:
            factors = prime_factors(val)
            unique_factors = set(factors)
            if len(unique_factors) % 2 == 0:
                results.append(1)
            else:
                results.append(-1)
    return results if len(value) > 1 else results[0]