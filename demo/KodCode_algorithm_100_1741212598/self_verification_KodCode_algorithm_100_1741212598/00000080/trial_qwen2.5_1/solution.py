def is_automorphic_number(number: int) -> bool:
    """
    Returns True if the number is an automorphic number, otherwise False.
    An automorphic number is a number whose square ends in the same digits as the number itself.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    if number < 0:
        return False
    
    num_str = str(number)
    square_str = str(number ** 2)
    return square_str.endswith(num_str)