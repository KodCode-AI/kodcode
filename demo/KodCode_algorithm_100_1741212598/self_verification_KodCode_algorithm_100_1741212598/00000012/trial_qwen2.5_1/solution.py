def simpson_integration(function, a: float, b: float, precision: int) -> float:
    """
    Approximates the definite integral of a function over the interval [a, b]
    using Simpson's method.
    """
    if not (0 <= a <= b <= 1000) or not (1 <= precision <= 10):
        raise ValueError("Invalid input: a, b must be in [0, 1000], and precision must be in [1, 10].")
    
    n = 1000  # Fixed number of steps for Simpson's method
    h = (b - a) / n
    result = function(a) + function(b)
    
    for i in range(1, n, 2):
        xi = a + i * h
        result += 4 * function(xi)
    
    for i in range(2, n-1, 2):
        xi = a + i * h
        result += 2 * function(xi)
    
    result *= h / 3
    return round(result, precision)