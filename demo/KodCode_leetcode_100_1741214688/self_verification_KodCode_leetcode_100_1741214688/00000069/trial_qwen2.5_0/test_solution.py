from solution import *

import pytest

def test_can_rearrange_string():
    assert can_rearrange_string("aaabbe") == False
    assert can_rearrange_string("aebdec") == True
    assert can_rearrange_string(" Portions ") == False
    assert can_rearrange_string("aAi") == True
    assert can_rearrange_string("aAiAe") == True
    assert can_rearrange_string(" aAe") == False
    assert can_rearrange_string(" aA") == False
    assert can_rearrange_string("a") == False
    assert can_rearrange_string("aa") == False

# The test for "aAi" is replaceable as "aAiAe" already covers the case where there are more vowels than consonants in odd/even positions.