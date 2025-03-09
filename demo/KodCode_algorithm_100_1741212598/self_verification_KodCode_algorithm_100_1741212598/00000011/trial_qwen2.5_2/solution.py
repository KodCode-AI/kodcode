from typing import Tuple

def fx(x: float, a: float) -> float:
    """
    The function whose root we are trying to find.
    """
    return x**2 - a

def fx_derivative(x: float) -> float:
    """
    The derivative of the function fx.
    """
    return 2 * x

def square_root_approximate(
    a: float, 
    initial_guess: float = 2.0, 
    max_iter: int = 9999, 
    tolerance: float = 1e-14
) -> Tuple[float, int, bool]:
    """
    Approximate the square root of a number using Newton's method.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if a == 0:
        return 0.0, 0, True
    
    x_prev = initial_guess
    x_curr = x_prev - fx(x_prev, a) / fx_derivative(x_prev)
    iterations = 1
    
    while abs(x_curr - x_prev) > tolerance and iterations < max_iter:
        x_prev = x_curr
        x_curr = x_prev - fx(x_prev, a) / fx_derivative(x_prev)
        iterations += 1
    
    return x_curr, iterations, abs(x_curr - x_prev) <= tolerance