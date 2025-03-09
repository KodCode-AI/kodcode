from solution import *

``
import math
from solution import enhanced_factorial

def test_enhanced_factorial_integers():
    assert enhanced_factorial(0) == "1"
    assert enhanced_factorial(5) == "120"
    assert enhanced_factorial(20) == "2432902008176640000"
    assert enhanced_factorial(1000) == "10888869450418352160768000"

def test_enhanced_factorial_floats():
    assert enhanced_factorial(0.5) == "1.128"
    assert enhanced_factorial(3.5) == "11.632"
    assert enhanced_factorial(5.5) == "523.428"
    assert enhanced_factorial(10.5) == "371588.831"

def test_enhanced_factorial_large_input():
    assert enhanced_factorial(50) == "30414093201713378043612608166064768844377641568960512000000000000"

def test_enhanced_factorial_negative_input():
    assert enhanced_factorial(-1) == "1"
    assert enhanced_factorial(-2) == "1"
    assert enhanced_factorial(-1.5) == "1.128"