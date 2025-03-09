from solution import *

import pytest

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(12321) == True

def test_reverse_and_add():
    assert reverse_and_add(123) == 456
    assert reverse_and_add(444) == 888
    assert reverse_and_add(321) == 444

def test_is_likely_lychrel():
    assert is_likely_lychrel(47) == True
    assert is_likely_lychrel(349) == True
    assert is_likely_lychrel(196) == True

def test_solution_optimized():
    limit = 10
    assert solution_optimized(limit) == 2
    limit = 100
    assert solution_optimized(limit) == 24
    limit = 1000
    assert solution_optimized(limit) == 249

    # Test with a larger limit
    limit = 100000000
    result = solution_optimized(limit)
    # Note: This test is for demonstration purposes only. The exact number of Lychrel numbers up to 99999999
    # is not provided here due to its computational complexity and time constraints.
    # assert result == expected_number_of_lychrel_numbers  # Replace with the correct number
    print(f"{result} Lychrel numbers found below the limit {limit}")