from solution import *

``
from test_solution import longest_common_subsequence

def test_longest_common_subsequence():
    # Test case 1
    a = "AGGTAB"
    b = "GXTXAYB"
    expected = (4, ["GTAB", "GBAB"])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 2
    a = "ABCDEF"
    b = "FBDAMN"
    expected = (2, ["BD"])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 3
    a = "AABAA"
    b = "ABBAA"
    expected = (4, ["AABA", "ABAA"])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 4
    a = "ABCBDAB"
    b = "BDCABA"
    expected = (4, ["BCAB", "BDAB"])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 5
    a = "ABCDGH"
    b = "AEDFHR"
    expected = (3, ["ADH"])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 6
    a = ""
    b = "abc"
    expected = (0, [])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 7
    a = "abc"
    b = ""
    expected = (0, [])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 8
    a = "aaa"
    b = "bbb"
    expected = (0, [])
    assert longest_common_subsequence(a, b) == expected
    
    # Test case 9
    a = "aaa"
    b = "aaa"
    expected = (3, ["aaa"])
    assert longest_common_subsequence(a, b) == expected

# Run the tests
test_longest_common_subsequence()