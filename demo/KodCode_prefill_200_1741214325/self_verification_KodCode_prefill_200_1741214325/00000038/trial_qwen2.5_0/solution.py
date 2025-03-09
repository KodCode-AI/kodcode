def char_frequency(input_string):
    """
    Returns a dictionary containing characters and their frequencies in the given string.
    """
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency