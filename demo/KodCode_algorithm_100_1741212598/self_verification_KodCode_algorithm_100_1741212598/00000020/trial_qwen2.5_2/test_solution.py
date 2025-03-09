from solution import *

from solution import solution, digit_cancelling_fractions

def test_solution_2():
    assert solution(2) == 100

def test_solution_3():
    result = digit_cancelling_fractions(3)
    # Manually calculate or know the product of denominators for digit-cancelling fractions with 3 digits
    assert result == 100 * 100 * 100 // (15 * 100 * 15)  # Example simplified product

def test_is_non_trivial_digit_cancelling():
    assert is_non_trivial_digit_cancelling(49, 98) == True
    assert is_non_trivial_digit_cancelling(49, 98) == False
    assert is_non_trivial_digit_cancelling(98, 49) == False

def test_simplify_fraction():
    assert simplify_fraction(10, 20) == (1, 2)
    assert simplify_fraction(20, 10) == (2, 1)
    assert simplify_fraction(15, 5) == (3, 1)