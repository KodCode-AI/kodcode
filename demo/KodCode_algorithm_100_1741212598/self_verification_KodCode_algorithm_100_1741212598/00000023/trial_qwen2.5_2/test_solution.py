from solution import *

def test_count_letters():
    assert count_letters(100) == 11
    assert count_letters(342) == 23
    assert count_letters(115) == 20
    assert count_letters(1000) == 21124
    assert count_letters(5) == 4
    assert count_letters(19) == 10
    assert count_letters(123) == 32
    assert count_letters(300) == 9
    assert count_letters(999) == 2234