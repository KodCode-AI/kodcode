def sum_of_n_natural_numbers(n):
    """
    This function calculates the sum of the first `n` natural numbers.
    
    Parameters:
    n (int): The number of natural numbers to sum.
    
    Returns:
    int: The sum of the first `n` natural numbers.
    """
    if not isinstance(n, int):
        return "Error: Input must be an integer."
    if n < 0:
        return "Error: Input must be a positive integer or zero."
    return n * (n + 1) // 2

# Example usage:
print(sum_natural_numbers(5))  # Output: 15