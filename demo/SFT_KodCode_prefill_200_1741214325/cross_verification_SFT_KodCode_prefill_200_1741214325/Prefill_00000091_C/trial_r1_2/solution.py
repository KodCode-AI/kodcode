from typing import List

def find_primes_in_range(start: int, end: int) -> List[int]:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes