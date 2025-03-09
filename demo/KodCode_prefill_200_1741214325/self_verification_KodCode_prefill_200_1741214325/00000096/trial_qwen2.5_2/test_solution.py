from solution import *

import pytest

def test_evaluate_expression():
    assert evaluate_expression("1+2") == 3
    assert evaluate_expression("1+2*3") == 7
    assert evaluate_expression("3+2*(1+2)*4") == 31

def test_integer_only():
    assert evaluate_expression("123") == 123

def test_complex_expression():
    assert evaluate_expression("2-1+1") == 2
    assert evaluate_expression("6*2-(4*3)") == -6

def test_precedence():
    assert evaluate_expression("2*3-4*5") == -14

def test_parentheses():
    assert evaluate_expression("5-(8-3)") == 0
    assert evaluate_expression("(2+2)*3") == 12

def test_singleton():
    assert evaluate_expression("1") == 1