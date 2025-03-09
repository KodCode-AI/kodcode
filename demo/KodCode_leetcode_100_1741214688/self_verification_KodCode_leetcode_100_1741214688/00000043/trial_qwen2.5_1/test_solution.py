from solution import *

from solution import max_product

def test_max_product():
    speed = [2, 10, 3]
    efficiency = [1, 2, 5]
    k = 2
    assert max_product(speed, efficiency, k) == 600

def test_two_engineers_case():
    speed = [5, 10, 3]
    efficiency = [3, 8, 4]
    k = 2
    assert max_product(speed, efficiency, k) == 60

def test_large_k_case():
    speed = [10, 10, 10, 10, 10, 10]
    efficiency = [10, 10, 10, 10, 10, 10]
    k = 5
    assert max_product(speed, efficiency, k) == 100

def test_single_engineer_case():
    speed = [50]
    efficiency = [100]
    k = 1
    assert max_product(speed, efficiency, k) == 50

def test_equal_speed_efficiency_case():
    speed = [1, 2, 3, 4, 5]
    efficiency = [1, 2, 3, 4, 5]
    k = 3
    assert max_product(speed, efficiency, k) == 400

def test_zero_case():
    speed = [0, 0, 0]
    efficiency = [0, 0, 0]
    k = 2
    assert max_product(speed, efficiency, k) == 0