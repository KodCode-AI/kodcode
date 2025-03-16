def interleave_strings(first_str: str, second_str: str) -> str:
    max_length = max(len(first_str), len(second_str))
    result = []
    for i in range(max_length):
        if i < len(first_str):
            result.append(first_str[i])
        if i < len(second_str):
            result.append(second_str[i])
    return ''.join(result)