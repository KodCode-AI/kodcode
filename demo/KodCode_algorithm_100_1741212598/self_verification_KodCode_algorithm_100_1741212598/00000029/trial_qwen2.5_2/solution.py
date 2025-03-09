def is_prime(num: int) -> bool:
    """
    Helper function to check if a number is prime.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def check_primes_with_property(limit: int) -> int:
    """
    Counts the number of prime numbers below a given limit that satisfy the property.
    """
    def property_check(p: int) -> bool:
        n = 1
        while n**3 < (n**3 + n**2 * p):
            if (n**3 + n**2 * p)**(1/3) == int((n**3 + n**2 * p)**(1/3)):
                return True
            n += 1
        return False
    
    count = 0
    for p in range(2, limit):
        if is_prime(p) and property_check(p):
            count += 1
    return count