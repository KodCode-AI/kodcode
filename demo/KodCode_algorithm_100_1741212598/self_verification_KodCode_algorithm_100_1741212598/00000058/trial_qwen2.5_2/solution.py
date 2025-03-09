import math

def semidivisible_sum(limit: int) -> int:
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    sum_semidivisible = 0
    for n in range(4, limit + 1):
        sqrt_n = math.isqrt(n)
        lps = sqrt_n
        while not is_prime(lps):
            lps -= 1
        ups = sqrt_n
        while not is_prime(ups):
            ups += 1
        if lps != ups and (n % lps == 0 or n % ups == 0):
            sum_semidivisible += n
    return sum_semidivisible