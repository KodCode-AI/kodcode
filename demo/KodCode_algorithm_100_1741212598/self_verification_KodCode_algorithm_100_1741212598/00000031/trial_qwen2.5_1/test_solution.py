from solution import *

from solution import question_function, solution

def test_solution():
    assert solution(question_function) == 98410

def test_order_1():
    def func(n: int) -> int:
        return 1 - n

    assert solution(func) == 1

def test_order_2():
    def func(n: int) -> int:
        return 1 - n + n**2

    assert solution(func) == 4

def test_order_3():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3

    assert solution(func) == 10

def test_order_4():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3 + n**4

    assert solution(func) == 21

def test_order_5():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3 + n**4 - n**5

    assert solution(func) == 36

def test_order_6():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6

    assert solution(func) == 56

def test_order_7():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7

    assert solution(func) == 81

def test_order_8():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8

    assert solution(func) == 112

def test_order_9():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9

    assert solution(func) == 150

def test_order_10():
    def func(n: int) -> int:
        return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

    assert solution(func) == 98410