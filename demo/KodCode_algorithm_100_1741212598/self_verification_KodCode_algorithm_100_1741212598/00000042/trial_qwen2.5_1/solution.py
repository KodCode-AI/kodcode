def is_palindrome(n: int) -> bool:
    """
    Checks if the given number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def sum_reverse(n: int) -> int:
    """
    Returns the sum of the given number and its reverse.
    """
    return n + int(str(n)[::-1])

def count_lychrel(limit: int) -> int:
    """
    Counts the number of Lychrel numbers below limit.
    """
    lychrel_count = 0
    for num in range(1, limit):
        n = num
        for _ in range(50):
            n = sum_reverse(n)
            if is_palindrome(n):
                break
        else:
            lychrel_count += 1
    return lychrel_count