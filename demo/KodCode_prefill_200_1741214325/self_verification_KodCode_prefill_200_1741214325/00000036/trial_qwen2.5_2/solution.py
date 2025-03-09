def print_primes(start: int, end: int):
    """
    Prints all prime numbers in the given range from start to end (inclusive).
    """
    if start > end or start < 2:
        raise ValueError("Invalid range: start should not be greater than end and start should be at least 2.")
    
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
            
def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True