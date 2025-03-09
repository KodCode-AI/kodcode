from solution import *

import pytest

def test_max_racecar_instances():
    assert max_racecar_instances("rcetarac") == 1
    assert max_racecar_instances("raceccara") == 1
    assert max_racecar_instances("raccaerace") == 2
    assert max_racecar_instances("racedracecar") == 1
    assert max_racecar_instances("eaaacccecceracc") == 2
    assert max_racecar_instances("racecar") == 1
    assert max_racecar_instances("a") == 0
    assert max_racecar_instances("racecarsracecar") == 1  # Only one complete "racecar" can be formed