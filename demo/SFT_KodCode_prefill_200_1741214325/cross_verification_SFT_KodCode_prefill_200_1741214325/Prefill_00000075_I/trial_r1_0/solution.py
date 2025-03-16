def is_perfect_number(n):
    """
    This function checks if a given number is a perfect number.
    
    A perfect number is a positive integer that is equal to the sum of its proper divisors, 
    which are all positive divisors excluding itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    if n <= 1:
        return False  # perfect numbers are positive integers greater than 1

    sum_divisor = 1  # 1 is a proper divisor for all numbers except 1
    sqrt_n = int(n ** 0.5)

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_divisor += i
            other_divisor = n // i
            if other_divisor != i:  # avoid adding square root twice
                sum_divisor += other_divisor

    return sum_divisor == n

# Example usage:
print(is_perfect(6))   # Output: True
print(is_perfect(28))  # Output: True
print(is_perfect(12))  # Output: False