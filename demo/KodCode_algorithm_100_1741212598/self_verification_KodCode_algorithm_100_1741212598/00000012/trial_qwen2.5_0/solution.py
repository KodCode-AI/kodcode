def simpson_integration(function, a: float, b: float, precision: int) -> float:
    """
    Approximates the integral of function f(x) over the interval [a, b] using Simpson's rule.

    Args:
    function: A callable function that takes a float and returns a float.
    a: The lower limit of integration.
    b: The upper limit of integration.
    precision: The desired precision of the result.

    Returns:
    The approximated value of the integral of f(x) over [a, b].
    """
    if not (0 <= a <= b <= 1000 and 1 <= precision <= 10):
        raise ValueError("Invalid input values. Ensure 0 <= a <= b <= 1000 and 1 <= precision <= 10.")

    n = 1000  # Fixed number of steps in the Simpson's rule
    h = (b - a) / n
    integral = (function(a) + function(b)) / 6.0
    for i in range(1, n, 2):
        x = a + i * h
        integral += function(x) / 3.0
    for i in range(2, n-1, 2):
        x = a + i * h
        integral += 2.0 * function(x) / 3.0

    return round(integral * h, precision)