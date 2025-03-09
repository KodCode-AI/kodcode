def print_primes(n):
    """
    Prints all prime numbers up to a given number n.
    """
    if n < 2:
        return
    
    sieve = [True] * (n + 1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for i in range(x*x, n + 1, x):
                sieve[i] = False
    
    for x in range(2, n + 1):
        if sieve[x]:
            print(x, end=' ')