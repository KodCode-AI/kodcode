from solution import *

def test_max_racecar_instances():
    assert max_racecar_instances("赛车竞技") == 0  # Chinese characters should not affect the count
    assert max_racecar_instances("racecar") == 1
    assert max_racecar_instances("rcaacecar") == 1
    assert max_racecar_instances("racecarracecar") == 2
    assert max_racecar_instances("racecabracelerac") == 1
    assert max_racecar_instances("racecarabracadabra") == 2
    assert max_racecar_instances("a") == 0
    assert max_racecar_instances("racecarca") == 1
    assert max_racecar_instances("racecarra") == 1
    assert max_racecar_instances("racecarracecarracecar") == 3

test_max_racecar_instances()