def count_uppercase(s: str) -> int:
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count