def second_maximum(numbers):
    unique_nums = sorted(set(numbers))
    if len(unique_nums) < 2:
        return None
    return unique_nums[-2]