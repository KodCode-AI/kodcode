from solution import *

from solution import find_min_string

def test_find_min_string():
    assert find_min_string("bbbaaa", 3) == ('aaaaabbb', 3)
    assert find_min_string("ccbb", 2) == ('bbcc', 1)
    assert find_min_string("abc", 5) == ('abc', 0)  # Already smallest
    assert find_min_string("ccc", 3) == ('ccc', 0)  # Already smallest
    assert find_min_string("zzzz", 2) == ('zzzz', 1)  # Can be made smaller with 1 operation

if __name__ == "__main__":
    import pytest
    pytest.main(['-v', '--tb=line', '-rN', __file__])