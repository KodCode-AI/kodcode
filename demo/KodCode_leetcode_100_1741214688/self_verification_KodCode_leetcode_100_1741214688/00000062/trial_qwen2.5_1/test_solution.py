from solution import *

def test_min_operations_to_uniform():
    assert min_operations_to_uniform("azbzczbzcz") == 5
    assert min_operations_to_uniform("a") == 0
    assert min_operations_to_uniform("z") == 0
    assert min_operations_to_uniform("abz") == 1
    assert min_operations_to_uniform("azbz") == 1
    assert min_operations_to_uniform("aaz") == -1
    assert min_operations_to_uniform("zzaa") == -1
    assert min_operations_to_uniform("aba") == -1
    assert min_operations_to_uniform("azbzzbza") == 2