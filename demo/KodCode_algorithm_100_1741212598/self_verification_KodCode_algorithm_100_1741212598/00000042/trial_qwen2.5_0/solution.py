def is_palindrome(n: int) -> bool:
    """
    Check if a given number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def sum_reverse(n: int) -> int:
    """
    Return the sum of a number and its reverse.
    """
    return n + int(str(n)[::-1])

def count_lychrel(limit: int) -> int:
    """
    Count the number of Lychrel numbers below the given limit.
    A Lychrel number is a number that does not form a palindrome through
    the reverse and add process within 50 iterations.
    """
    def is_likely_lychrel(n: int) -> bool:
        for _ in range(50):
            n = sum_reverse(n)
            if is_palindrome(n):
                return False
        return True

    lychrel_count = 0
    for i in range(1, limit):
        if is_likely_lychrel(i):
            lychrel_count += 1
    return lychrel_count