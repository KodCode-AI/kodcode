from solution import *

from solution import longest_alphabetical_substring

def test_longest_alphabetical_substring():
    assert longest_alphabetical_substring("abcbdefg") == 7
    assert longest_alphabetical_substring("abcde") == 5
    assert longest_alphabetical_substring("a") == 1
    assert longest_alphabetical_substring("azbcdefg") == 5
    assert longest_alphabetical_substring("aabbccddeeff") == 2
    assert longest_alphabetical_substring("zab") == 3
    assert longest_alphabetical_substring("zzzzzzz") == 1