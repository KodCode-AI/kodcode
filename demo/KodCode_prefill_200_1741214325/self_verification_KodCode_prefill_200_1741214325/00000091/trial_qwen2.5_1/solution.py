def find_primes_in_range(start, end):
    """
    Returns a list of all prime numbers within the given range [start, end].
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes