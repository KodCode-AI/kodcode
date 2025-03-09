def char_frequency(input_string):
    """
    Returns a dictionary containing the frequency of each character in the input_string.
    """
    frequency_dict = {}
    for char in input_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict