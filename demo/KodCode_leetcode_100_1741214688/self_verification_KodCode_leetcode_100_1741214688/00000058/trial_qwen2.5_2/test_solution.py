from solution import *

from solution import reverse_segment

def test_reverse_segment():
    assert reverse_segment("abcdeaa", 3) == "aebcd"
    assert reverse_segment("abcd", 2) == "abcd"  # 'a' is only found once, so no change
    assert reverse_segment("aabcde", 2) == "aaebcd"  # 'a' is found twice, but in reverse order
    assert reverse_segment("abcdaa", 4) == "aabcd"  # 'a' is found four times, but the segment includes the second 'a'
    assert reverse_segment("aaaaaa", 1) == "a"  # 'a' is found many times, but the segment is only 1 character
    assert reverse_segment("abcdefg", 0) == "abcdefg"  # No 'a' at index 0, so no change
    assert reverse_segment("", 0) == ""  # Empty string, no changes