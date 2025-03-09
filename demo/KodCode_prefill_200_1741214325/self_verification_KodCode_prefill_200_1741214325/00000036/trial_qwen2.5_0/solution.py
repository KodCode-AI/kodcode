def print_primes(start: int, end: int) -> None:
    """
    This function prints all prime numbers in a given range from 'start' (inclusive) to 'end' (inclusive).

    Parameters:
    start (int): Start of the range (inclusive).
    end (int): End of the range (inclusive).

    Returns:
    None
    """

    def is_prime(num: int) -> bool:
        """Check if a given number is prime."""
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(start, end + 1):
        if is_prime(num):
            print(num)