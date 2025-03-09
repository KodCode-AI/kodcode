def simpson_integration(function, a: float, b: float, precision: int) -> float:
    """
    Returns the approximate definite integral of a function f(x) over the interval [a, b] using Simpson's method.
    """
    if not (0 <= a <= b <= 1000) or not (1 <= precision <= 10):
        raise ValueError("Invalid input. Ensure a, b are within [0, 1000] and precision is within [1, 10].")
    
    n = 1000  # Number of steps
    h = (b - a) / n
    s = function(a) + function(b)
    
    for i in range(1, n, 2):
        s += 4 * function(a + i * h)
    
    for i in range(2, n-1, 2):
        s += 2 * function(a + i * h)
    
    result = s * h / 3
    return round(result, precision)