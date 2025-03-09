from math import sqrt, ceil

def semidivisible_sum(limit: int) -> int:
    def lps(n):
        # Find the largest prime less than or equal to the square root of n
        root = int(sqrt(n))
        for i in range(root, 1, -1):
            if all(i % p != 0 for p in range(2, int(sqrt(i)) + 1)):
                return i
        return 1  # if no prime found, return 1, this will never happen for n >= 4

    def ups(n):
        # Find the smallest prime greater than or equal to the square root of n
        root = ceil(sqrt(n))
        while True:
            if all(root % p != 0 for p in range(2, int(sqrt(root)) + 1)):
                return root
            root += 1

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        return all(n % i != 0 for i in range(3, int(sqrt(n)) + 1, 2))

    def find_primes(limit):
        primes = []
        checked = [False] * (limit + 1)
        for i in range(2, limit + 1):
            if not checked[i]:
                if is_prime(i):
                    primes.append(i)
                for j in range(i, limit + 1, i):
                    checked[j] = True
        return primes

    primes = find_primes(int(sqrt(limit)) + 1)
    semidivisible_sum = 0

    for n in range(4, limit + 1):
        lps_val = lps(n)
        ups_val = ups(n)
        if (n % lps_val == 0 and n % ups_val != 0) or (n % lps_val != 0 and n % ups_val == 0):
            semidivisible_sum += n

    return semidivisible_sum