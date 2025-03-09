def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    """
    Return the prime factors of n.
    """
    factors = []
    # Check for number of 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for other primes
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

def liouville_lambda(n):
    """
    Returns the Liouville Lambda value for a given integer or a list of integers.
    """
    if not isinstance(n, list):
        n = [n]
    results = []
    for num in n:
        factors = prime_factors(num)
        factor_count = len(factors)
        prime_factors_dict = {factor: factors.count(factor) for factor in set(factors)}
        is_even = all(count % 2 == 0 for count in prime_factors_dict.values())
        if is_even:
            results.append(1)
        else:
            results.append(-1)
    return results if n != [n] else results[0]