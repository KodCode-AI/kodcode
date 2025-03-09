from solution import *

from solution import longest_common_subsequence

def test_longest_common_subsequence():
    a = "AGGTAB"
    b = "GXTXAYB"
    expected_output = (4, ["GTAB", "GBAB"])
    assert longest_common_subsequence(a, b) == expected_output

    a = "ABC"
    b = "AC"
    expected_output = (2, ["AC"])
    assert longest_common_subsequence(a, b) == expected_output

    a = "ABCDGH"
    b = "AEDFHR"
    expected_output = (3, ["ADH"])
    assert longest_common_subsequence(a, b) == expected_output

    a = "AGGTAB"
    b = "AGGTAB"
    expected_output = (6, ["AGGTAB"])
    assert longest_common_subsequence(a, b) == expected_output

    a = "ABAC"
    b = "BAC"
    expected_output = (2, ["AB", "BA"])
    assert longest_common_subsequence(a, b) == expected_output

    a = ""
    b = "ABCD"
    expected_output = (0, [])
    assert longest_common_subsequence(a, b) == expected_output

    a = "abcdGH"
    b = "defgh"
    expected_output = (0, [])
    assert longest_common_subsequence(a, b) == expected_output

    a = "banana"
    b = "bandana"
    expected_output = (4, ["ban", "bana"])
    assert longest_common_subsequence(a, b) == expected_output