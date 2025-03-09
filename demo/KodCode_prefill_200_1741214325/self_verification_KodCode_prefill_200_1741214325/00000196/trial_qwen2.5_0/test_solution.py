from solution import *

def rabin_karp_search(substring, string):
    return rabin_karp.search(substring, string)

def test_rabin_karp_with_matching_substring_at_start():
    assert rabin_karp_search('test', 'testmatchingstring') == 0

def test_rabin_karp_with_matching_substring_in_middle():
    assert rabin_karp_search('string', 'testmatchingstring') == 6

def test_rabin_karp_with_non_matching_substring():
    assert rabin_karp_search('abc', 'teststring') == -1

def test_rabin_karp_with_empty_substring():
    assert rabin_karp_search('', 'teststring') == -1

def test_rabin_karp_with_longer_substring_than_given_string():
    assert rabin_karp_search('teststring', 'test') == -1