from solution import *

import pytest

def test_min_swaps_to_target():
    assert min_swaps_to_target(["abc", "def", "ghi"], "defabcghi") == 2
    assert min_swaps_to_target(["a","b","c"], "aaabbbb") == -1
    assert min_swaps_to_target(["cde","abc"], "ceabdccba") == 6
    assert min_swaps_to_target(["a","a","a","a"], "aaaa") == 0
    assert min_swaps_to_target(["a","a","a","a"], "bbaaaa") == 2
    assert min_swaps_to_target(["abc","def","ghi"], "defabc") == -1

pytest.main()