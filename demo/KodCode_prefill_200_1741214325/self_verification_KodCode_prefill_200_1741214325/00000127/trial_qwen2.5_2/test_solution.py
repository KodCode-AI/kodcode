from solution import *

from solution import evaluate_infix_expression

def test_evaluate_infix_expression():
    assert evaluate_infix_expression("1 + 2 * 3") == 7
    assert evaluate_infix_expression("(1 + 5) * 2 - 3 / 4") == 10.75
    assert evaluate_infix_expression("2 + (3 - 1) * 4 / 2") == 8.0
    assert evaluate_infix_expression("9 - (7 + 3)") == -3
    assert evaluate_infix_expression("2 * 3 + 5 / 4") == 7.75
    assert evaluate_infix_expression("100 / 25 * 5") == 20.0
    assert evaluate_infix_expression("8 + 3 - 6 / 2") == 8.0
    assert evaluate_infix_expression("-2 + 1") == -1.0

def test_decimal_operations():
    assert evaluate_infix_expression("1.5 * 2.4") == 3.6
    assert evaluate_infix_expression("3.0 / 1.2") == 2.5
    assert evaluate_infix_expression("2.5 + 3.5") == 6.0
    assert evaluate_infix_expression("4.5 - 3.2") == 1.3
    assert evaluate_infix_expression("4.5 * 2.2") == 9.9
    assert evaluate_infix_expression("2.5 + 3.2 * 2") == 9.9

def test_parenthesis():
    assert evaluate_infix_expression("(1 + 2) * (3 + 4)") == 21
    assert evaluate_infix_expression("(((2) + (3) * (1)))") == 5

def test_negative_numbers():
    assert evaluate_infix_expression("-2 + 5 * 2") == 8
    assert evaluate_infix_expression("(-2 - 1) * 3") == -9

def test邊界：
    # Test with minimal input
    assert evaluate_infix_expression("2") == 2
    assert evaluate_infix_expression("-2") == -2
    # Test without any operators
    assert evaluate_infix_expression("10") == 10
    # Test with an empty string
    assert evaluate_infix_expression("") == 0
    # Test with an invalid string (contains non-operator and non-parentheses characters)
    assert evaluate_infix_expression("2a") == 2
    assert evaluate_infix_expression("1 + (2 - 3 + -4)") == -4
    assert evaluate_infix_expression("1 + 2 - 3 * 4 / 5") == 0.4