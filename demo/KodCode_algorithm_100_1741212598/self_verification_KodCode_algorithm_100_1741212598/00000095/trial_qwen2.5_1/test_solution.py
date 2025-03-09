from solution import *

\

def test_is_balanced():
    assert is_balanced("({[\\]})") == True, "Failed with escaped square bracket"
    assert is_balanced("({[\\[\\]})") == False, "Failed with malformed input"
    assert is_balanced("[{()}\\{\\}[]]") == True, "Failed with nested sequences and escaped characters"
    assert is_balanced("abc[def]ghi") == True, "Failed with non-bracket characters in between"
    assert is_balanced("{{{{}])") == False, "Failed with imbalanced closing curly braces"
    assert is_balanced("\\[{\\}]") == True, "Failed with escaped square brackets"
    assert is_balanced("\\[\\{\\}\\]") == True, "Failed with properly escaped and nested brackets"
    assert is_balanced("\\[\\{\\]})") == False, "Failed with escape and malformed input"
    assert is_balanced("") == True, "Failed with empty string"
    assert is_balanced("()[]{}") == True, "Failed with properly balanced strings"
    assert is_balanced("([]{})") == True, "Failed with nested balanced strings"
    assert is_balanced("[]{}") == True, "Failed with interleaved balanced strings"
    assert is_balanced("([)]") == False, "Failed with mismatched closing brackets"
    assert is_balanced("{[}") == False, "Failed with mismatched closing brackets"
    assert is_balanced("({[\\]])") == False, "Failed with mismatched and escaped closing brackets"
    
test_is_balanced()