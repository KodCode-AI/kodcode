from solution import *

import pytest

def test_first_repeating_char():
    assert first_repeating_char("programming") == 2
    assert first_repeating_char("abcdef") == -1
    assert first_repeating_char("aabbcc") == 1
    assert first_repeating_char("ababab") == 1
    assert first_repeating_char("aa") == 1
    assert first_repeating_char("") == -1