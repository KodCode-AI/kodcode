from solution import *

import pytest

def test_solution_for_two_digits():
    assert solution(2) == 90

def test_solution_for_three_digits():
    assert solution(3) == 100

def test_simple_cases():
    assert solution(2) == 90
    assert solution(3) == 100

def test_non_trivial_cases():
    # Testing that only the correct digit cancelling fractions are included
    # and their denominators are correctly processed.
    assert are_digit_cancelling_fraction(49, 98) is True
    assert are_digit_cancelling_fraction(30, 50) is False  # This is trivial
    assert are_digit_cancelling_fraction(40, 80) is True  # This is trivial
    assert are_digit_cancelling_fraction(16, 64) is True
    assert are_digit_cancelling_fraction(26, 65) is True

def test_invalid_cases():
    assert are_digit_cancelling_fraction(0, 0) is False
    assert are_digit_cancelling_fraction(4, 2) is False  # This simplifies to incorrect fraction