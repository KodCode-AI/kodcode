def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]