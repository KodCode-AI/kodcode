from solution import *

def test_count_substrings():
    words1 = ["aim", "at", "apple", "apricot", "orange"]
    target1 = "ap"
    assert count_substrings(words1, target1) == 3

    words2 = ["hello", "world", "python", "programming"]
    target2 = "py"
    assert count_substrings(words2, target2) == 1

    words3 = ["big", "small", "bigs", "smalls"]
    target3 = "big"
    assert count_substrings(words3, target3) == 2

    words4 = ["challenge", "response", "react", "reactive"]
    target4 = "res"
    assert count_substrings(words4, target4) == 2

    words5 = ["data", "science", "statistics", "probability", "bayesian"]
    target5 = "sci"
    assert count_substrings(words5, target5) == 1