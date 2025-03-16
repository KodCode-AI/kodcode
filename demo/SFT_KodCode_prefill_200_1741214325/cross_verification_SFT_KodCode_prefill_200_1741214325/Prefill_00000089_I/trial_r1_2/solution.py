def factorial(n):
    # Check if the input is a valid integer or a whole number float
    if isinstance(n, int):
        pass
    elif isinstance(n, float) and n.is_integer():
        n = int(n)
    else:
        return None
    
    # Handle negative numbers
    if n < 0:
        return None
    
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result