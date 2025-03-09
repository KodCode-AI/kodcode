from solution import *

from solution import max_team_product

def test_max_team_product():
    # Test case 1
    assert max_team_product([10, 20, 30, 40], [10, 20, 30, 40], 3) == 600
    # Test case 2
    assert max_team_product([40, 20, 30], [20, 30, 10], 2) == 600
    # Test case 3
    assert max_team_product([10, 20, 50, 70], [5, 25, 40, 100], 1) == 1000
    # Test case 4
    assert max_team_product([10, 20, 5, 7], [5, 25, 40, 10], 2) == 250
    # Test case 5
    assert max_team_product([5,4,3,2,1], [1,2,3,4,5], 3) % (10**9 + 7) == 35