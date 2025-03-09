from solution import *

import pytest

def test_min_swaps_to_target():
    assert min_swaps_to_target(["abc", "def", "ghi"], "defabcghi") == 2
    assert min_swaps_to_target(["abc", "def", "ghi"], "abcdefg") == 3
    assert min_swaps_to_target(["abc", "def", "ghi"], "defabch") == -1
    assert min_swaps_to_target(["abc", "def", "ghi"], "abcdefgh") == -1
    assert min_swaps_to_target(["abc", "def", "ghi"], "abcdef") == 3
    assert min_swaps_to_target(["abc", "def", "ghi"], "defabc") == 1