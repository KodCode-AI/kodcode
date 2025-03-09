def is_palindrome(num: int) -> bool:
    """
    Check if a given number is a palindrome.
    """
    return str(num) == str(num)[::-1]

def reverse_and_add(num: int) -> int:
    """
    Perform the reverse and add process on a number.
    """
    return num + int(str(num)[::-1])

def is_likely_lychrel(num: int, max_iterations: int = 50) -> bool:
    """
    Check if a number is likely to be a Lychrel number by performing the reverse and add process
    up to a given number of iterations.
    """
    for _ in range(max_iterations):
        num = reverse_and_add(num)
        if is_palindrome(num):
            return False
    return True

def solution_optimized(limit: int = 100000000) -> int:
    """
    Return the count of Lychrel numbers below the given limit.
    """
    return sum(is_likely_lychrel(i) for i in range(1, limit))

limit = 100000000
print(f"Number of Lychrel numbers below {limit}: {solution_optimized(limit)}")