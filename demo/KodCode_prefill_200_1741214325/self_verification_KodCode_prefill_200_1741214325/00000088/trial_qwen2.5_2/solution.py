def filter_words不含("{}", "{}"):
    """
    Returns a list of words from the input list that do not contain the specified substring.
    """
    return [word for word in input_list if substring not in word]