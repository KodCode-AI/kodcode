def interleave_strings(first_str: str, second_str: str) -> str:
    result = ""
    max_length = max(len(first_str), len(second_str))
    for i in range(max_length):
        if i < len(first_str):
            result += first_str[i]
        if i < len(second_str):
            result += second_str[i]
    return result