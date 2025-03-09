from solution import *

from solution import max_racecar_instances
from collections import Counter

def test_max_racecar_instances():
    assert max_racecar_instances("racecar") == 1
    assert max_racecar_instances("racecaracecar") == 2
    assert max_racecar_instances("racceara") == 1
    assert max_racecar_instances("rrrraaaacecaarr") == 2
    assert max_racecar_instances("a") == 0
    assert max_racecar_instances("racecars") == 0  # 's' is not in the target
    assert max_racecar_instances("rcrcaaeerr") == 1
    assert max_racecar_instances("racecarracecar") == 2