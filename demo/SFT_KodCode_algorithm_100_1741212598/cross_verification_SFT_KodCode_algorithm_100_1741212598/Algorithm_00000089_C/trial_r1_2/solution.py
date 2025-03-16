def find_next_prime(value: int) -> int:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    current = value + 1
    while True:
        if is_prime(current):
            return current
        current += 1