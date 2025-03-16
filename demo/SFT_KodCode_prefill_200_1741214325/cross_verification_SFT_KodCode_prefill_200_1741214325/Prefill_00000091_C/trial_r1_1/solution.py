import math
from typing import List

def find_primes_in_range(start: int, end: int) -> List[int]:
    primes = []
    for n in range(start, end + 1):
        if n < 2:
            continue
        is_prime = True
        sqrt_n = math.isqrt(n)
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes