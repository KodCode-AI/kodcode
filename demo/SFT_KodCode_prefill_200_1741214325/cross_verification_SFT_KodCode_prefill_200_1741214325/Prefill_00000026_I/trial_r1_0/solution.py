def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)