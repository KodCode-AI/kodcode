from solution import *

def test_min_operations():
    assert min_operations("azbzczbzcz") == 5
    assert min_operations("zzzazzzazz") == 5
    assert min_operations("zzzzz") == 0
    assert min_operations("aaaaa") == 0
    assert min_operations("aaazaaaz") == 1
    assert min_operations("zzzzzzzzaa") == -1