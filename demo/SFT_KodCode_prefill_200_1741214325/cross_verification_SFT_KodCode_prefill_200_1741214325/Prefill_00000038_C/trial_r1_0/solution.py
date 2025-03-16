def char_frequency(input_string: str) -> dict:
    freq_dict = {}
    for char in input_string:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict