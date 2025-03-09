def filter_words(words_list, substring):
    """
    Returns a list of words that do not contain the specified substring.
    
    :param words_list: List of words to be filtered.
    :param substring: Substring to filter out from the words.
    :return: List of words that do not contain the specified substring.
    """
    return [word for word in words_list if substring not in word]