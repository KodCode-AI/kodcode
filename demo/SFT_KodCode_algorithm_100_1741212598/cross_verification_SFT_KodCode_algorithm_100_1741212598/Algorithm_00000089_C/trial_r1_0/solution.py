def find_next_prime(value: int) -> int:
    """Return the smallest prime number greater than the given value."""
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    n = value + 1
    while True:
        if is_prime(n):
            return n
        n += 1