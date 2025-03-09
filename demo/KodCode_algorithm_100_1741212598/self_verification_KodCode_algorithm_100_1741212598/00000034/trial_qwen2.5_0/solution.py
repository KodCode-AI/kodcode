def check_opposite_signs(num1, num2):
    """
    Determines if two integers have opposite signs using bitwise operations.
    """
    return (num1 ^ num2) < 0