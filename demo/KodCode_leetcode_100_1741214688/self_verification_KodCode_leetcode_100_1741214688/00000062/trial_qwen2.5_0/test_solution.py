from solution import *

def test_min_operations_to_uniform_string():
    assert min_operations_to_uniform_string("azbzczbzcz") == 5
    assert min_operations_to_uniform_string("aaazzzzz") == 1
    assert min_operations_to_uniform_string("zzzzyy") == 4
    assert min_operations_to_uniform_string("aaa") == -1
    assert min_operations_to_uniform_string("zzz") == -1
    assert min_operations_to_uniform_string("azzazzazz") == 3
    assert min_operations_to_uniform_string("aazzazzazz") == 4
    assert min_operations_to_uniform_string("zzazzazz") == 3

test_min_operations_to_uniform_string()