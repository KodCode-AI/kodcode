from solution import *

import math
from solution import enhanced_factorial

def test_exact_integer_factorials():
    assert enhanced_factorial(5) == "120"
    assert enhanced_factorial(20) == "2432902008176640000"

def test_float_stirling_approximation():
    assert enhanced_factorial(0.5) == "1.128"
    assert enhanced_factorial(3.5) == "11.632"

def test_large_integer_upper_limit():
    assert enhanced_factorial(1000) == "3.0414093201713376e+2567"

def test_edge_case_zero():
    assert enhanced_factorial(0) == "1"
    assert enhanced_factorial(0.0) == "1.0"

def test_edge_case_one():
    assert enhanced_factorial(1) == "1"
    assert enhanced_factorial(1.0) == "1.0"

def test_greater_than_100_exact():
    for i in range(5, 101):
        assert int(enhanced_factorial(i)) == math.factorial(i)

def test_stirling_accuracy_for_large_floats():
    for n in range(10, 101, 10):
        float_n = n + 0.5
        stirling_result = enhanced_factorial(float_n)
        stirling_approximation = math.sqrt(2 * math.pi / float_n) * (float_n / math.e)**float_n
        assert round(float(stirling_result), 3) == round(stirling_approximation, 3)