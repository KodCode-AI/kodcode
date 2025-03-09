from solution import *

from solution import evaluate_postfix

def test_simple_addition():
    assert evaluate_postfix("3 4 +") == 7

def test_simple_subtraction():
    assert evaluate_postfix("10 5 -") == 5

def test_simple_multiplication():
    assert evaluate_postfix("3 5 *") == 15

def test_simple_division():
    assert evaluate_postfix("20 4 /") == 5

def test_complex_expression():
    assert evaluate_postfix("5 1 2 + 4 * + 3 -") == 14

def test_invalid_expression():
    try:
        evaluate_postfix("5 1 2 + 4 * + 3 a")
    except ValueError:
        # This is expected, indicating that the function correctly handles invalid inputs
        pass
    else:
        assert False, "Expected a ValueError for invalid input"

def test_divide_by_zero():
    try:
        evaluate_postfix("20 0 /")
    except ValueError:
        # This is expected
        pass
    else:
        assert False, "Expected a ValueError when dividing by zero"