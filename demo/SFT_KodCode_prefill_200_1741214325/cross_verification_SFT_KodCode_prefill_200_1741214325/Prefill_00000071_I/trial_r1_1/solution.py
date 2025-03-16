def sum_of_multiples():
    limit = 1000
    sum3 = (3 * ((limit - 1) // 3) * ((limit - 1) // 3 + 1)) // 2
    sum5 = (5 * ((limit - 1) // 5) * ((limit - 1) // 5 + 1)) // 2
    sum15 = (15 * ((limit - 1) // 15) * ((limit - 1) // 15 + 1)) // 2
    return sum3 + sum5 - sum15

result = sum_of_multiples()
print(result)