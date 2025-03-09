from solution import *

from solution import solution

def u(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def getFIT(n):
    poly = [u(i) for i in range(n)]
    for i in range(1, n):
        if poly[i] != u(i):
            return i
    return n

# Test cases for individual FIT calculations
assert getFIT(1) == 1
assert getFIT(2) == 4
assert getFIT(3) == 7
assert getFIT(4) == 43
assert getFIT(5) == 51
assert getFIT(6) == 66
assert getFIT(7) == 73
assert getFIT(8) == 84
assert getFIT(9) == 91
assert getFIT(10) == 101

# Final test for solution function
assert solution(u, 10) == 98410