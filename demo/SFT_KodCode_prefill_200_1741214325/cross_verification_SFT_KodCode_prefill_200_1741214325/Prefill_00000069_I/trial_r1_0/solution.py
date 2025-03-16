def count_trailing_zeros(n):
    if n == 0:
        return 1
    try:
        n = abs(int(n))
    except ValueError:
        raise TypeError("n must be an integer or convertible to integer")
    s = str(n)
    count = 0
    for char in reversed(s):
        if char == '0':
            count += 1
        else:
            break
    return count