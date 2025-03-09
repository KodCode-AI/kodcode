from solution import *

def test_optimized_solution():
    assert optimized_solution(1) == 4
    assert optimized_solution(2) == 32
    assert optimized_solution(5) == 1200
    assert optimized_solution(10) == 120000
    assert optimized_solution(50) == 3125000000