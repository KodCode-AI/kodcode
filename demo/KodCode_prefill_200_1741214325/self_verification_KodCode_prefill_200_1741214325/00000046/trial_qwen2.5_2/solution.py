def is_palindrome_number(number: int) -> bool:
    """
    Checks if the given number is a palindrome number.
    
    Args:
    number (int): The number to check
    
    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    if number < 0:
        return False
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    return original_number == reversed_number