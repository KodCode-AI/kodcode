def is_automorphic_number(number: int) -> bool:
    """
    Returns True if the number is an automorphic number, otherwise False.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    if number < 0:
        return False
    
    str_number = str(number)
    str_square = str(number ** 2)
    
    return str_square.endswith(str_number)