from solution import *

def test_is_balanced():
    assert is_balanced("({[\\]})") == True, "Test with escaped square bracket failed."
    assert is_balanced("({[\\[\\]})") == False, "Test with malformed input failed."
    assert is_balanced("[{()}\\{\\}[]]") == True, "Test with nested sequences and escaped characters failed."
    assert is_balanced("([)]") == False, "Test with unbalanced nested sequences failed."
    assert is_balanced("") == True, "Test with empty string failed."
    assert is_balanced("([]{})") == True, "Test with well-formed nested sequences failed."
    assert is_balanced("([{}])") == True, "Test with correctly nested sequences failed."
    assert is_balanced("\\([{}])") == True, "Test with escaped opening and closing brackets failed."
    assert is_balanced("\\([{}]") == False, "Test with malformed input due to unescaped closing bracket failed."

test_is_balanced()