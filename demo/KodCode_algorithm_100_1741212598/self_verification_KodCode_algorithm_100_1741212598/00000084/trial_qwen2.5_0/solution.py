def prime_factors(n, primes):
    """
    Returns the prime factorization of n given a list of primes.
    """
    factors = []
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    if n > 1:
        factors.append(n)
    return factors

def phi(n, primes):
    """
    Returns Euler's Totient function value for n using prime factorization.
    """
    if n == 1:
        return 1
    factors = prime_factors(n, primes)
    unique_factors = sorted(set(factors))
    phi_n = n
    for prime in unique_factors:
        phi_n *= (1 - 1/prime)
    return int(phi_n)

def find_min_ratio():
    primes = sieve_of_eratosthenes(100000)
    best_n = None
    min_ratio = float('inf')
    for n in range(2, 10000000):
        # Check if phi(n) is a permutation of n
        if sorted(str(n)) == sorted(str(phi(n, primes))):
            current_ratio = n / phi(n, primes)
            if current_ratio < min_ratio:
                min_ratio = current_ratio
                best_n = n
    return best_n

def sieve_of_eratosthenes(limit):
    """
    Generates all prime numbers up to the limit using the Sieve of Eratosthenes.
    """
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num*num, limit + 1, num):
                sieve[multiple] = False
    return [num for num in range(2, limit) if sieve[num]]

def find_min_permutation_of_phi():
    return find_min_ratio()