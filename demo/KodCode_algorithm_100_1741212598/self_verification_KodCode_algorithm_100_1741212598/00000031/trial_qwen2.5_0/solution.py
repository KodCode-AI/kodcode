def solution(func):
    fit_sum = 0
    for order in range(1, 11):
        for n in range(1, 100):
            generated_value = func(n)
            interpolating_polynomial = sum([a * (n**i) for i, a in enumerate([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]) if i <= order])
            if generated_value != interpolating_polynomial:
                fit_sum += n
                break
    return fit_sum