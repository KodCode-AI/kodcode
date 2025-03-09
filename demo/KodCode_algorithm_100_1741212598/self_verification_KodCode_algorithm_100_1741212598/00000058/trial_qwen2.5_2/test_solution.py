from solution import *

``
import pytest

def test_semidivisible_sum():
    assert semidivisible_sum(15) == 30
    assert semidivisible_sum(1000) == 34825
    assert semidivisible_sum(999_966_663_333) == 2480389586872
    assert semidivisible_sum(4) == 4
    assert semidivisible_sum(5) == 4
    assert semidivisible_sum(6) == 10
    assert semidivisible_sum(10) == 22
    assert semidivisible_sum(11) == 10
    assert semidivisible_sum(12) == 32
    assert semidivisible_sum(13) == 10
    assert semidivisible_sum(14) == 44
    assert semidivisible_sum(15) == 30
    assert semidivisible_sum(16) == 68
    assert semidivisible_sum(17) == 10