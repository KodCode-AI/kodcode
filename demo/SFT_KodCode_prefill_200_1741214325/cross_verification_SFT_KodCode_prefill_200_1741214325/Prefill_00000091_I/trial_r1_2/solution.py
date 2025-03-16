def get_primes_in_range(start, end):
    if end < 2:
        return []
    sieve = [True] * (end + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(end ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, end + 1, i):
                sieve[j] = False
    primes = [i for i in range(start, end + 1) if sieve[i]]
    return primes