from solution import *

import pytest

def question_function(n: int) -> int:
    return (
        1
        - n
        + n**2
        - n**3
        + n**4
        - n**5
        + n**6
        - n**7
        + n**8
        - n**9
        + n**10
    )

def test_solution():
    assert solution(question_function) == 98410

def test_small_order():
    assert solution(lambda n: n) == 1  # Order 1
    assert solution(lambda n: 1 - n) == 2  # Order 2
    assert solution(lambda n: 1 - n + n**2) == 3  # Order 3
    assert solution(lambda n: 1 - n + n**2 - n**3) == 4  # Order 4
    assert solution(lambda n: 1 - n + n**2 - n**3 + n**4) == 5  # Order 5
    assert solution(lambda n: 1 - n + n**2 - n**3 + n**4 - n**5) == 6  # Order 6
    assert solution(lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6) == 7  # Order 7
    assert solution(lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7) == 8  # Order 8
    assert solution(lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8) == 9  # Order 9
    assert solution(lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9) == 10  # Order 10

if __name__ == "__main__":
    pytest.main()