from solution import *

from solution import find_smallest_string

def test_find_smallest_string():
    assert find_smallest_string("daily", 1) == ("adily", 1)
    assert find_smallest_string("onlinesubmission", 2) == ("bimonlinesusmission", 2)
    assert find_smallest_string("acbbcabbba", 3) == ("aaabbbcccb", 3)
    assert find_smallest_string("abcdxyz", 2) == ("abcdxyz", 0)
    assert find_smallest_string("zzzzzzzzab", 1) == ("aabzzzzzzz", 8)

def test_min_operations():
    assert find_smallest_string("daily", 1)[1] == 1
    assert find_smallest_string("onlinesubmission", 2)[1] == 2
    assert find_smallest_string("acbbcabbba", 3)[1] == 3
    assert find_smallest_string("abcdxyz", 2)[1] == 0
    assert find_smallest_string("zzzzzzzzab", 1)[1] == 8