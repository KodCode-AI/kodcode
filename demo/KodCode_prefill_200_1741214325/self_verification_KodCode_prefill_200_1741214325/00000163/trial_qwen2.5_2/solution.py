def shortest_words(text):
    """
    Returns a list of the shortest words in a given text.
    If there are multiple words of the same shortest length, all are included.
    """
    words = text.split()
    if not words:
        return []
    
    min_length = min(len(word) for word in words)
    shortest_words_list = [word for word in words if len(word) == min_length]
    return shortest_words_list