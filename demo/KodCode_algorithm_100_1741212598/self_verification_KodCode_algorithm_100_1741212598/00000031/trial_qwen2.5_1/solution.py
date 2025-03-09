def question_function(n: int) -> int:
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def solution(func):
    sum_of_fits = 0
    for k in range(1, 11):
        for n in range(1, 100):
            if func(n) != sum(func(i**k for i in range(n + 1))):
                sum_of_fits += n
                break
    return sum_of_fits