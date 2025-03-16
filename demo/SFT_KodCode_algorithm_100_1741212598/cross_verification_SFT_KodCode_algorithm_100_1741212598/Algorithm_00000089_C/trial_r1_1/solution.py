def find_next_prime(value: int) -> int:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    n = value + 1
    if n <= 2:
        return 2
    elif n == 2:
        return 2
    elif n % 2 == 0:
        n += 1

    while True:
        if is_prime(n):
            return n
        n += 2