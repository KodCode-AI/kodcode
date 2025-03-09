from solution import *

def test_is_balanced():
    assert is_balanced("({[\\]})") == True, "Failed on balanced with escaped square bracket"
    assert is_balanced("({[\\[\\]})") == False, "Failed on malformed input with escaped characters"
    assert is_balanced("[{()}\\{\\}[]]") == True, "Failed on nested sequences and escaped characters"
    assert is_balanced("([]{})") == True, "Failed on simple nested balance"
    assert is_balanced("([)]") == False, "Failed on improper nesting"
    assert is_balanced("({[]})") == True, "Failed on balanced nested sequence"
    assert is_balanced("\\[\\]{}") == True, "Failed on balanced with escaped opening and closing brackets"
    assert is_balanced("\\{\\[\\}\\]") == True, "Failed on balanced with escaped characters inside nested brackets"
    assert is_balanced("\\{\\[\\}") == False, "Failed on malformed input with escaped characters inside nested brackets"
    assert is_balanced("") == True, "Failed on empty string"
    assert is_balanced("a({[\\]})b") == True, "Failed on string with escaped characters in the middle"