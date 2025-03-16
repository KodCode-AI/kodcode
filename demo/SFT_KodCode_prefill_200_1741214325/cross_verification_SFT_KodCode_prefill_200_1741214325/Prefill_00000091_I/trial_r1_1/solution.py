def find_primes_in_range(start, end):
    def is_prime(number):
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    primes = []
    lower = min(start, end)
    upper = max(start, end)
    for num in range(lower, upper + 1):
        if is_prime(num):
            primes.append(num)
    return primes