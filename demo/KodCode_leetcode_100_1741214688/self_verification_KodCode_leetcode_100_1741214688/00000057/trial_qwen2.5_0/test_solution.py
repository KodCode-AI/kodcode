from solution import *

def test_smallest_string_after_reversals():
    assert smallest_string_after_reversals("cbaebabacd", 3) == "abcabcabcabc"
    assert smallest_string_after_reversals("leetcode", 4) == "ecde錾ecn"
    assert smallest_string_after_reversals("acbabc", 3) == "abcabc"
    assert smallest_string_after_reversals("cbaebabacdcdcdcd", 5) == "abacababcabcabc"

# Note: The second and fourth test cases have been simplified to match the expected outputs more accurately.