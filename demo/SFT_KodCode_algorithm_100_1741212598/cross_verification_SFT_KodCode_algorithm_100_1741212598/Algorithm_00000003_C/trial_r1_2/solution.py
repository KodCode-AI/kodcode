def interleave_strings(first_str: str, second_str: str) -> str:
    result = []
    len_first = len(first_str)
    len_second = len(second_str)
    i = j = 0
    while i < len_first or j < len_second:
        if i < len_first:
            result.append(first_str[i])
            i += 1
        if j < len_second:
            result.append(second_str[j])
            j += 1
    return ''.join(result)