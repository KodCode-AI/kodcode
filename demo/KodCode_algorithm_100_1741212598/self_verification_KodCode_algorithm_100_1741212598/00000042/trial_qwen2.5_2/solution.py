def is_palindrome(n: int) -> bool:
    """
    Check if a number is a palindrome.
    """
    return str(n) == str(n)[::-1]

def sum_reverse(n: int) -> int:
    """
    Return the sum of a number and its reverse.
    """
    return n + int(str(n)[::-1])

def count_lychrel(limit: int) -> int:
    """
    Return the count of Lychrel numbers below the given limit.
    """
    lychrel_count = 0
    for num in range(1, limit):
        for _ in range(50):
            num = sum_reverse(num)
            if is_palindrome(num):
                break
        else:
            lychrel_count += 1
    return lychrel_count