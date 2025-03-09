def filter_words_notContaining_substring(words, substring):
    """
    Returns a list of words that do not contain the specified substring.
    
    :param words: List of words to filter.
    :param substring: The substring to check for in the words.
    :return: A list of words that do not contain the substring.
    """
    return [word for word in words if substring not in word]