from solution import *

``
from solution import liouville_lambda

def test_liouville_lambda_single():
    assert liouville_lambda(10) == 1
    assert liouville_lambda(11) == -1
    assert liouville_lambda(12) == -1

def test_liouville_lambda_list():
    assert liouville_lambda([10, 11, 12]) == [1, -1, -1]
    assert liouville_lambda([1, 2, 3, 4, 5, 6]) == [1, -1, -1, 1, -1, -1]
    assert liouville_lambda([100]) == 1
    assert liouville_lambda([]) == 0

def test_liouville_lambda_edge_cases():
    assert liouville_lambda(-10) == 0
    assert liouville_lambda(0) == 0
    assert liouville_lambda(1) == 1

def test_liouville_lambda_input_type():
    assert liouville_lambda([10]) == 1
    assert liouville_lambda(10) == 1