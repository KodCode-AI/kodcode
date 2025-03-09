from solution import *

from solution import semidivisible_sum

def test_semidivisible_sum():
    assert semidivisible_sum(15) == 30, "Test case 15 failed"
    assert semidivisible_sum(1000) == 34825, "Test case 1000 failed"
    assert semidivisible_sum(999_966_663_333) == 2480389586872, "Test case 999_966_663_333 failed"
    assert semidivisible_sum(4) == 4, "Test case 4 failed"
    assert semidivisible_sum(5) == 5, "Test case 5 failed"
    assert semidivisible_sum(6) == 10, "Test case 6 failed"
    assert semidivisible_sum(7) == 10, "Test case 7 failed"
    assert semidivisible_sum(8) == 16, "Test case 8 failed"
    assert semidivisible_sum(9) == 16, "Test case 9 failed"
    assert semidivisible_sum(10) == 30, "Test case 10 failed"

test_semidivisible_sum()