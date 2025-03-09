from solution import *

def test_has_valid_path():
    assert has_valid_path([[1, 1, 1], [1, 0, 0], [1, 1, 1]], 5) == True
    assert has_valid_path([[1, 1, 1], [1, 0, 0], [1, 1, 1]], 8) == False
    assert has_valid_path([[1, 2, 3], [4, 5, 6]], 12) == True
    assert has_valid_path([[1, 2, 3], [4, 5, 6]], 16) == False
    assert has_valid_path([[1], [1]], 2) == True
    assert has_valid_path([[1], [1]], 0) == False
    assert has_valid_path([[1], [1]], 1) == True