def interleave_strings(first_str: str, second_str: str) -> str:
    result = []
    len1, len2 = len(first_str), len(second_str)
    max_len = max(len1, len2)
    for i in range(max_len):
        if i < len1:
            result.append(first_str[i])
        if i < len2:
            result.append(second_str[i])
    return ''.join(result)