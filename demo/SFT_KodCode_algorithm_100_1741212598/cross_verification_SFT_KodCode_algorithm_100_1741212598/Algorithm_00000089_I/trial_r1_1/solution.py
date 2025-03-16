def find_next_prime(value: int) -> int:
    if value < 2:
        return 2
    if value % 2 == 0:
        candidate = value + 1
    else:
        candidate = value + 2
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 2