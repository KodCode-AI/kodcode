def print_primes(n):
    """
    Prints all prime numbers up to n.
    """
    if n < 2:
        return  # No primes less than 2
    
    for possiblePrime in range(2, n + 1):
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            print(possiblePrime)