import math
from math import gamma

def enhanced_factorial(number: float) -> str:
    """
    Returns the factorial of a number as a string. For exact integers, it uses
    the factorial function. For floating-point numbers, it uses Stirling's
    approximation and rounds to 3 decimal places.
    """
    if number.is_integer():
        integer_part = int(number)
        result = math.factorial(integer_part)
        return str(result)
    else:
        stirling_approximation = math.sqrt(2 * math.pi / number) * (number / math.e)**number
        result = round(stirling_approximation, 3)
        return "{:.3f}".format(result)