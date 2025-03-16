from solution import *

def test_sum_of_n_natural_numbers():
    assert sum_of_n_natural_numbers(1) == 1
    assert sum_of_n_natural_numbers(2) == 3
    assert sum_of_n_natural_numbers(3) == 6
    assert sum_of_n_natural_numbers(10) == 55
    assert sum_of_n_natural_numbers(100) == 5050
    assert sum_of_n_natural_numbers(0) == 0