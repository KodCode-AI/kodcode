import re

def split_string_into_words(input_string):
    """
    Splits the input string based on ',', '.', and ' ' (space) and returns a list of words.
    """
    return re.split(r'[ ,.]+', input_string)