from solution import *

import pytest

def test_liouville_lambda():
    assert liouville_lambda(10) == 1, "10 has an even number of prime factors"
    assert liouville_lambda(11) == -1, "11 has an odd number of prime factors"
    assert liouville_lambda(100) == 1, "100 has an even number of prime factors"
    assert liouville_lambda(30030) == -1, "30030 has an odd number of prime factors"
    with pytest.raises(ValueError, match="Input must be a positive integer."):
        liouville_lambda(0)
    with pytest.raises(ValueError, match="Input must be a positive integer."):
        liouville_lambda(-3)
    with pytest.raises(ValueError, match="Input must be a positive integer."):
        liouville_lambda(3.14)
    with pytest.raises(ValueError, match="Input must be a positive integer."):
        liouville_lambda("string")
    assert liouville_lambda(2) == -1, "2 has an odd number of prime factors"
    assert liouville_lambda(4) == 1, "4 has an even number of prime factors"

if __name__ == "__main__":
    pytest.main()