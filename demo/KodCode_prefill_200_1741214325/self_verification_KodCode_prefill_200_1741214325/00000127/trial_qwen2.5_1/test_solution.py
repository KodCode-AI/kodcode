from solution import *

from solution import evaluate_infix_expression

def test_simple_addition():
    assert evaluate_infix_expression("2 + 3") == 5

def test_simple_subtraction():
    assert evaluate_infix_expression("5 - 3") == 2

def test_simple_multiplication():
    assert evaluate_infix_expression("4 * 5") == 20

def test_simple_division():
    assert evaluate_infix_expression("8 / 2") == 4

def test_precedence_addition_subtraction():
    assert evaluate_infix_expression("2 + 3 - 1") == 4

def test_precedence_multiplication_division():
    assert evaluate_infix_expression("2 * 3 / 2") == 3

def test_precedence_mixed_operations():
    assert evaluate_infix_expression("2 + 3 * 4 - 6 / 3") == 10

def test_parentheses_evaluation():
    assert evaluate_infix_expression("(2 + 3) * 4") == 20

def test_negative_numbers():
    assert evaluate_infix_expression("-2 + 3 * 4") == 10

def test_complex_expression():
    assert evaluate_infix_expression("10 + 2 * (3 + 4) - 5 / (2 + 1)") == 20