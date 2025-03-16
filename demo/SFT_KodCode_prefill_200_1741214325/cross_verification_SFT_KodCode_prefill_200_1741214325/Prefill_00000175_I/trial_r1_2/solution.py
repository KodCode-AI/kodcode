def fibonacci(n):
    if n <= 0:
        print([])
        return
    fib_list = []
    if n >= 1:
        fib_list.append(1)
    if n >= 2:
        fib_list.append(1)
    for i in range(3, n + 1):
        next_num = fib_list[i-2] + fib_list[i-3]
        fib_list.append(next_num)
    print(fib_list)