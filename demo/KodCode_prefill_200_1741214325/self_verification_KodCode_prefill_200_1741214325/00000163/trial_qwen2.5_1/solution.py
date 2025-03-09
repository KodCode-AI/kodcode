import re
from collections import defaultdict

def extract_shortest_words(text):
    """
    Returns a dictionary of all the shortest words in the text, mapping them to their lengths.
    """
    # Split the text into words using regular expression to handle punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return {}

    min_length = min(len(word) for word in words)
    shortest_words = {word: min_length for word in words if len(word) == min_length}
    return shortest_words