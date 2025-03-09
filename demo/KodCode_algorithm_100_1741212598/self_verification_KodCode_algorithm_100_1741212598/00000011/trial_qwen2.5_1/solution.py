from typing import Tuple

def fx(x: float, a: float) -> float:
    return x**2 - a

def fx_derivative(x: float) -> float:
    return 2 * x

def square_root_approximate(
    a: float, 
    initial_guess: float = 2.0, 
    max_iter: int = 9999, 
    tolerance: float = 1e-14
) -> Tuple[float, int, bool]:
    """
    Approximate the square root of a number using Newton's method.
    
    Args:
    a (float): The number to find the square root of.
    initial_guess (float): The initial guess for the square root. Default is 2.0.
    max_iter (int): The maximum number of iterations to perform. Default is 9999.
    tolerance (float): The tolerance level for the approximation. Default is 1e-14.
    
    Returns:
    Tuple[float, int, bool]: 
        - The approximated square root.
        - The number of iterations performed.
        - A boolean indicating if the approximation converged within the tolerance.
    
    Raises:
    ValueError: If the input number is negative.
    """
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    
    x = initial_guess
    for i in range(max_iter):
        fx_val = fx(x, a)
        if abs(fx_val) < tolerance:
            return (x, i+1, True)
        
        df_dx = fx_derivative(x)
        x_new = x - fx_val / df_dx
        
        if abs(x_new - x) < tolerance:
            return (x_new, i+1, True)
        
        x = x_new
    
    return (x, max_iter, False)