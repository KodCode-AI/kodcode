def is_palindrome(number: int) -> bool:
    """
    Check if a number is a palindrome.
    """
    return str(number) == str(number)[::-1]

def reverse_number(number: int) -> int:
    """
    Reverse the digits of a number.
    """
    return int(str(number)[::-1])

def is_likely_lychrel(number: int, max_iterations: int = 50) -> bool:
    """
    Check if a number is a Lychrel number by performing the reverse and add process.
    """
    for _ in range(max_iterations):
        number += reverse_number(number)
        if is_palindrome(number):
            return False
    return True

def solution_optimized(limit: int) -> int:
    """
    Returns the count of Lychrel numbers below the given limit.
    """
    count = 0
    for num in range(1, limit):
        if is_likely_lychrel(num):
            count += 1
    return count