from solution import *

from solution import simpson_integration

def test_simpson_integration():
    def f1(x):
        return x * x
    assert abs(simpson_integration(f1, 1, 2, 4) - 2.3333) < 1e-3

def test_simpson_integration_with_log():
    import math
    def f2(x):
        return math.log(x)
    assert abs(simpson_integration(f2, 1, 3, 3) - 2.197) < 1e-3

def test_simpson_integration_with_exp():
    import math
    def f3(x):
        return math.exp(x)
    assert abs(simpson_integration(f3, 0, 1, 3) - 1.718) < 1e-3

def test_simpson_integration_edge_case():
    def f4(x):
        return x
    assert abs(simpson_integration(f4, 0, 1, 4) - 0.5) < 1e-4

def test_simpson_integration_out_of_bounds():
    import pytest
    with pytest.raises(ValueError):
        simpson_integration(lambda x: x, -1, 1, 2)
    with pytest.raises(ValueError):
        simpson_integration(lambda x: x, 1, 5001, 2)
    with pytest.raises(ValueError):
        simpson_integration(lambda x: x, 1, 5, 11)

def test_simpson_integration_precision():
    def f5(x):
        return x * x
    assert abs(simpson_integration(f5, 1, 2, 1) - 2.3) < 1e-3