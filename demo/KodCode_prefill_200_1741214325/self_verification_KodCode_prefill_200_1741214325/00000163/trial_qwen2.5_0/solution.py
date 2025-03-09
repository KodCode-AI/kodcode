def extract_shortest_words(text):
    """
    Returns a list of the shortest words in the given text.
    If there are multiple words of the same shortest length, all are included.
    Words are considered as sequences of alphanumeric characters separated by non-alphanumeric characters.
    """
    # Split the text into words based on non-alphanumeric characters
    words = text.split()
    # Find the minimum length of words to determine the shortest words
    min_length = min(len(word) for word in words)
    # Extract all words that are of the minimum length
    shortest_words = [word for word in words if len(word) == min_length]
    return shortest_words