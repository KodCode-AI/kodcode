def is_palindrome_number(number: int) -> bool:
    if number < 0:
        return False
    s = str(number)
    return s == s[::-1]