def find_min_ratio():
    """
    Finds the value of n (1 < n < 10^7) for which the Euler's Totient function (φ(n)) is a permutation of n
    and the ratio n/φ(n) is minimized.
    """
    def euler_phi(n):
        """
        Calculates the Euler's Totient function φ(n).
        """
        result = n  # Initialize result as n
        p = 2
        # Consider all prime factors
        while p * p <= n:
            # Check if p is a prime factor.
            if n % p == 0:
                # If yes, then update n and result
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result

    # A hash map to store the ratio and the corresponding n
    phi_cache = {}
    min_ratio = float('inf')
    min_n = 0

    for n in range(2, 10**7):
        phi_n = euler_phi(n)
        ratio = n / phi_n
        # Check if n and phi(n) are permutations
        if sorted(str(n)) == sorted(str(phi_n)):
            if ratio < min_ratio:
                min_ratio = ratio
                min_n = n
                phi_cache[min_n] = min_ratio

    return min_n