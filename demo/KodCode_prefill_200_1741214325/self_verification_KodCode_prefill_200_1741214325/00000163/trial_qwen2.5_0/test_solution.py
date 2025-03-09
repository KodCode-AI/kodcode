from solution import *

from solution import extract_shortest_words

def test_extract_shortest_words():
    assert extract_shortest_words("The quick brown fox") == ['The', 'fox']  # 'The' and 'fox' are both 3 characters long
    assert extract_shortest_words("Jumped over the lazy dog") == ['over', 'the']  # 'over' and 'the' are both 4 characters long
    assert extract_shortest_words("aaaa bbb c") == ['aaa', 'bbb']  # 'aaa' and 'bbb' are both 3 characters long
    assert extract_shortest_words("") == []  # Empty string should return an empty list
    assert extract_shortest_words("a b c d e f g") == ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # All words are one character long
    assert extract_shortest_words("primirro") == ['primirro']  # Single word, longest one