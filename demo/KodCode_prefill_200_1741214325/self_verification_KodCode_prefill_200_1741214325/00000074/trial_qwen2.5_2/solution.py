def is_perfect_square(num: int) -> bool:
    """
    Checks if the given number is a perfect square.
    
    Args:
    num (int): The number to check
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    if num < 0:
        return False
    root = int(num ** 0.5)
    return root * root == num