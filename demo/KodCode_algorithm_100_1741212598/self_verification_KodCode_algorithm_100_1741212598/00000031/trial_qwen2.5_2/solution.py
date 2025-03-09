def solution(func, order):
    def getFIT(n):
        poly = [func(i) for i in range(n)]
        for i in range(1, n):
            if poly[i] != u(i):
                return i
        return n

    def u(n):
        return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

    fit_sum = 0
    for k in range(1, order + 1):
        fit_sum += getFIT(k)
    return fit_sum