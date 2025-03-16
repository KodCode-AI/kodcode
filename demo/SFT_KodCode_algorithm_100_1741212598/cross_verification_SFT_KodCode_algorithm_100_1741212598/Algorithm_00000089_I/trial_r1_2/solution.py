def find_next_prime(value: int) -> int:
    candidate = value + 1
    if candidate == 2:
        return candidate
    if candidate % 2 == 0:
        candidate += 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 2