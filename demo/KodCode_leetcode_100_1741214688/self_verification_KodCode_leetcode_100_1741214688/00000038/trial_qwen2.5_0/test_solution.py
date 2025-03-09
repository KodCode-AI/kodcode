from solution import *

def test_longest_alphabetical_substring():
    assert longest_alphabetical_substring("abcbdefg") == 7
    assert longest_alphabetical_substring("aaaaa") == 5
    assert longest_alphabetical_substring("abcdek") == 6
    assert longest_alphabetical_substring("abcbdefgh") == 8
    assert longest_alphabetical_substring("xyz") == 3
    assert longest_alphabetical_substring("xya") == 3
    assert longest_alphabetical_substring("abc") == 3
    assert longest_alphabetical_substring("abdefghijklmnopqrstuvwxyza") == 27