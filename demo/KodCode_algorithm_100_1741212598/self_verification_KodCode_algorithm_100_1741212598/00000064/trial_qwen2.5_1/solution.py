from math import gamma
from decimal import Decimal, getcontext

def enhanced_factorial(number: float) -> str:
    """
    Computes the factorial of the given number. For integer inputs, it returns the exact factorial as a string.
    For floating-point inputs, it uses Stirling's approximation to approximate the factorial and rounds to 3 decimal places.
    """
    # Set up Decimal context for handling large numbers
    getcontext().prec = 50
    
    # Convert to Decimal for precision
    number = Decimal(number)
    
    if number == 0:
        return "1"
    elif number.is_integer():
        # Compute exact factorial for integer inputs
        result = 1
        for i in range(1, int(number) + 1):
            result *= i
        return str(result)
    else:
        # Use Stirling's approximation for non-integer inputs
        return str(round(gamma(number + 1), 3))