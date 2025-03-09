def is_palindrome(n: int) -> bool:
    """
    Checks if the given number is a palindrome.
    """
    s = str(n)
    return s == s[::-1]

def reverse_and_add(n: int) -> int:
    """
    Returns the result of reverse and add process for the given number.
    """
    s = str(n)
    return n + int(s[::-1])

def is_likely_lychrel(n: int) -> bool:
    """
    Checks if the number is a Lychrel number by performing reverse and add process up to 50 times.
    """
    for _ in range(50):
        n = reverse_and_add(n)
        if is_palindrome(n):
            return False
    return True

def solution_optimized(limit: int) -> int:
    """
    Counts the number of Lychrel numbers below the given limit.
    """
    count = 0
    for num in range(1, limit):
        if is_likely_lychrel(num):
            count += 1
    return count

# Example usage
limit = 100000000
print(f"{solution_optimized(limit) = }")