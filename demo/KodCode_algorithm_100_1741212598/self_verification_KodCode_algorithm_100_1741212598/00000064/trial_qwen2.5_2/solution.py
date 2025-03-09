import math

def enhanced_factorial(number: float) -> str:
    """
    Returns the factorial of the given number as a string.
    For integer inputs, performs exact computation.
    For floating-point inputs, uses Stirling's approximation.
    """
    if number == 0:
        return "1"
    elif number.is_integer():
        num = int(number)
        result = 1
        for i in range(1, num + 1):
            result *= i
        return str(result)
    else:
        # Stirling's approximation: n! ≈ sqrt(2 * pi * n) * (n / e) ** n
        n = number
        approximation = math.sqrt(2 * math.pi * n) * (n / math.e) ** n
        return f"{approximation:.3f}"