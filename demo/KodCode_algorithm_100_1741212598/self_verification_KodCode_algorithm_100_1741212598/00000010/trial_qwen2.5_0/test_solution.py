from solution import *

`python
from solution import solution_optimized, is_palindrome, reverse_and_add, is_likely_lychrel

def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(123) is False
    assert is_palindrome(1221) is True
    assert is_palindrome(12321) is True

def test_reverse_and_add():
    assert reverse_and_add(349) == 349 + 943 == 1292
    assert reverse_and_add(47) == 47 + 74 == 121
    assert reverse_and_add(123) == 123 + 321 == 444

def test_is_likely_lychrel():
    assert is_likely_lychrel(56) is True
    assert is_likely_lychrel(196, max_iterations=1500) is True  # Known Lychrel number
    assert is_likely_lychrel(47, max_iterations=1500) is False  # Known non-Lychrel number
    assert is_likely_lychrel(295, max_iterations=1500) is True  # Another known Lychrel number

def test_solution_optimized():
    # Test with a smaller limit for faster verification
    assert solution_optimized(2000) == 249

# Output the result for the large limit (10^8)
print(f"Number of Lychrel numbers below 10^8: {solution_optimized(100000000)}")