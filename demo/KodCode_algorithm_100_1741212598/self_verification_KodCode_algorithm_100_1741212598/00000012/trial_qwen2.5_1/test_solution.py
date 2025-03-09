from solution import *

import pytest
from solution import simpson_integration

def test simpson_integration_positive_function():
    assert simpson_integration(lambda x: x * x, 1, 2, 4) == 2.333

def test_simpson_integration_linear_function():
    assert simpson_integration(lambda x: 2 * x + 1, 0, 4, 4) == 32.0

def test_simpson_integration_cosine_function():
    assert simpson_integration(lambda x: 4 * (math.cos(x)), 0, math.pi, 4) == 8.0

def test_simpson_integration_constant_function():
    assert simpson_integration(lambda x: 3, 1, 4, 4) == 9.0

def test_simpson_integration_edge_case():
    with pytest.raises(ValueError):
        simpson_integration(lambda x: x, -1, 1, 2)
        
def test_simpson_integration_precision():
    assert simpson_integration(lambda x: x * x, 1, 2, 2) == 2.33
    assert simpson_integration(lambda x: x * x, 1, 2, 5) == 2.33333