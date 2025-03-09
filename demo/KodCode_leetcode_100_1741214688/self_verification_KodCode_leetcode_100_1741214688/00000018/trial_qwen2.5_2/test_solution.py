from solution import *

def test_minimum_cost():
    assert minimum_cost([1,2,3], [10,15,20]) == 10
    assert minimum_cost([3,1,1,1], [10,1,1,1]) == 12
    assert minimum_cost([3,1,2], [4,2,1]) == 4

def test_minimum_cost_with_zeros():
    assert minimum_cost([0,0,0], [1,2,3]) == 0
    assert minimum_cost([0,0,0], [100,100,100]) == 0

def test_minimum_cost_all_elements():
    assert minimum_cost([1,1,1,1], [2,2,2,2]) == 8
    assert minimum_cost([1,1,1,1,1], [1,2,3,4,5]) == 5

def test_minimum_cost_example():
    assert minimum_cost([2,2,3,1,1,0], [10,10,10,10,10,10]) == 20
    assert minimum_cost([1,2,3], [0,0,0]) == 0