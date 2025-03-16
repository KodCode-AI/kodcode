def is_perfect_number(n):
    """
    Checks if a given number is a perfect number.
    
    A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    if n <= 1:
        return False  # By definition, perfect numbers are greater than 1
    
    total = 1  # Start with 1, since 1 is a proper divisor for all numbers > 1
    sqrt_n = int(n ** 0.5)  # Calculate square root once

    # Check for divisors up to the square root of n
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            total += i  # Add the divisor i
            other_divisor = n // i
            if other_divisor != i:  # Avoid adding duplicate when i and other_divisor are the same
                total += other_divisor

    return total == n

# Example usage:
print(is_perfect_number(6))   # Output: True
print(is_perfect_number(28))  # Output: True
print(is_perfect_number(12))  # Output: False