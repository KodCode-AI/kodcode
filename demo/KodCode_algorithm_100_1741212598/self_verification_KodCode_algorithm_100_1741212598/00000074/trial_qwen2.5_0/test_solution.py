from solution import *

from solution import count_reversible_numbers

def test_count_reversible_numbers():
    assert count_reversible_numbers(3) == 120
    assert count_reversible_numbers(6) == 18720
    assert count_reversible_numbers(7) == 68720
    assert count_reversible_numbers(1) == 5
    assert count_reversible_numbers(2) == 5
    assert count_reversible_numbers(4) == 1350
    assert count_reversible_numbers(5) == 18000