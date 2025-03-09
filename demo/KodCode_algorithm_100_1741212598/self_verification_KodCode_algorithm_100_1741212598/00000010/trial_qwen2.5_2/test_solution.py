from solution import *

``
from solution import is_palindrome, reverse_number, is_likely_lychrel, solution_optimized

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(1234321) == True
    assert is_palindrome(1234567) == False

def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(4567) == 7654
    assert reverse_number(9009) == 9009

def test_is_likely_lychrel():
    assert is_likely_lychrel(47) == True
    assert is_likely_lychrel(349) == True
    assert is_likely_lychrel(196) == True
    assert is_likely_lychrel(197) == True
    assert is_likely_lychrel(44) == False

def test_solution_optimized():
    limit = 10
    assert solution_optimized(limit) == 2  # 19, 55 are Lychrel numbers under 10

    limit = 100
    assert solution_optimized(limit) == 24  # Count of Lychrel numbers under 100

    limit = 1000
    assert solution_optimized(limit) == 249  # Count of Lychrel numbers under 1000

    limit = 10000
    assert solution_optimized(limit) == 2592  # Count of Lychrel numbers under 10000

    limit = 100000000
    assert solution_optimized(limit) == 24988  # Note: This count may vary based on the actual Lychrel numbers