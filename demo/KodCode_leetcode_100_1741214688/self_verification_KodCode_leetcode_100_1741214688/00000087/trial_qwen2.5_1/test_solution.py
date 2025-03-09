from solution import *

def test_exist():
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False
    assert exist([], "ABCCED") == False
    assert exist([["a"]], "a") == True
    assert exist([["a"]], "b") == False
    assert exist([["a","b","c"],["d","e","f"]], "acef") == True
    assert exist([["a","b","c"],["d","e","f"]], "abcdef") == False  # Cannot use the same cell more than once

test_exist()