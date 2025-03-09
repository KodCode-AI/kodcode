from solution import *

from solution import can_beautiful_string

def test_can_beautiful_string():
    assert can_beautiful_string("a") == True
    assert can_beautiful_string("aa") == False
    assert can_beautiful_string("aba") == False
    assert can_beautiful_string("abca") == True
    assert can_beautiful_string("abc") == False
    assert can_beautiful_string("abcba") == True
    assert can_beautiful_string("aaaa") == True
    assert can_beautiful_string("aabaa") == True
    assert can_beautiful_string("adnea") == True
    assert can_beautiful_string("aeiaa") == False
    assert can_beautiful_string("auvia") == True
    assert can_beautiful_string("퉤") == True  # Non-English character test, should act as any other character
    assert can_beautiful_string("pii") == False
    assert can_beautiful_string("aaab") == False
    assert can_beautiful_string("aaaaa") == True