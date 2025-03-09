from math import isqrt, sqrt

def sieve_of_eratosthenes(limit: int) -> list[bool]:
    """Generate a list of boolean values where the index represents
       whether the number is prime (True) or not (False)."""
    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def semidivisible_sum(limit: int) -> int:
    """Compute the sum of all semidivisible numbers not exceeding the given limit."""
    primes = sieve_of_eratosthenes(isqrt(limit) + 1)
    semidivisible_sum = 0
    
    for n in range(4, limit + 1):
        lps, ups = None, None
        for p in range(isqrt(n), 1, -1):
            if primes[p]:
                lps = p
                break
        for p in range(isqrt(n), limit + 1):
            if primes[p]:
                ups = p
                break
        
        if lps and n % lps == 0:
            semidivisible_sum += n
        elif ups and n % ups == 0:
            semidivisible_sum += n
        else:
            semidivisible_sum += n
    
    return semidivisible_sum