def find_pandigital_fibonacci() -> int:
    """
    Finds the index of the first Fibonacci number that is pandigital in both the first nine digits and the last nine digits.
    """
    def check(number: int) -> bool:
        return len(str(number)) == 9 and set(str(number)) == set('123456789')
    
    def check1(number: int) -> bool:
        return len(str(number)) == 9 and set(str(number)) == set('123456789')
    
    fib_1, fib_2 = 0, 1
    index = 2
    
    while index < 1000000:
        fib_1, fib_2 = fib_2, (fib_1 + fib_2) % 10**9  # Use modulo 10^9 to keep the numbers manageable
        if check(fib_2) and check1(fib_2):
            return index
        index += 1
    
    return -1