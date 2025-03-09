from solution import *

import pytest

def test_count_letters():
    assert count_letters(3) == 3
    assert count_letters(11) == 6
    assert count_letters(100) == 11
    assert count_letters(342) == 23
    assert count_letters(115) == 20
    assert count_letters(1000) == 21124
    assert count_letters(999) == 21052
    with pytest.raises(ValueError):
        count_letters(1001)
    with pytest.raises(ValueError):
        count_letters(0)