from sympy import sieve

def find_min_ratio():
    """
    Finds the value of n (1 < n < 10^7) for which the Euler's Totient function (φ(n))
    is a permutation of n and the ratio n/φ(n) is minimized.
    """
    min_ratio = float('inf')
    n_value = None
    
    for n in range(2, 10000000):
        phi_n = totient(n)
        if sorted(str(n)) == sorted(str(phi_n)):
            current_ratio = n / phi_n
            if current_ratio < min_ratio:
                min_ratio = current_ratio
                n_value = n
                
    return n_value

def totient(n):
    """
    Computes the Euler's Totient function for a given number n.
    """
    result = n
    i = 0
    while True:
        p = list(sieve.primerange(0, int(n**0.5) + 1))  # Get primes up to sqrt(n)
        p.append(n)
        p = set(p)  # To avoid duplicates and for quick lookup
        for prime in p:
            if prime > n:
                break
            if n % prime == 0:
                result -= result // prime
        if i > 0 and result < 2:
            break
        i += 1
    return result