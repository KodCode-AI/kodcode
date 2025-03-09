def is_palindrome_number(number: int) -> bool:
    """
    Checks if the given number is a palindrome.
    
    A number is a palindrome if it reads the same backward as forward.
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