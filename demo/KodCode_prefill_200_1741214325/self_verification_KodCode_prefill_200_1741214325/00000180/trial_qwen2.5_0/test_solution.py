from solution import *

from solution import has_separated_repeats

def test_no_repeats():
    assert not has_separated_repeats("abcdefg")

def test_adjacent_repeats():
    assert not has_separated_repeats("aabbcc")

def test_non_adjacent_repeats():
    assert has_separated_repeats("aabbccdd")

def test_single_char():
    assert not has_separated_repeats("a")

def test_several_non_adjacent_repeats():
    assert has_separated_repeats("ababa")
    assert has_separated_repeats("abcda")
    assert has_separated_repeats("abbcdd")