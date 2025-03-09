def is_automorphic_number(number: int) -> bool:
    """
    Checks if the given number is an automorphic number.
    An automorphic number is a number whose square ends in the same digits as the number itself.
    """
    if not isinstance(number, int):
        raise TypeError
    
    if number < 0:
        return False
    
    square_str = str(number ** 2)
    number_str = str(number)
    
    return square_str.endswith(number_str)