def print_primes(n):
    """
    Prints all prime numbers up to a given number n.
    """
    if n < 2:
        return  # No primes less than 2
    
    # Print 2 separately since it's the only even prime number
    if n >= 2:
        print(2)
    
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to not prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Print all prime numbers
    for p in range(3, n+1, 2):
        if prime[p]:
            print(p)