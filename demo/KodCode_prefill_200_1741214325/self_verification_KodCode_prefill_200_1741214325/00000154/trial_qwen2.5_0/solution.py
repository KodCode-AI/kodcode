def split_string_into_words(s):
    """
    Splits the given string into words based on the delimiters ',', '.', and ' '.
    Args:
    s (str): The input string to split.
    
    Returns:
    list: A list of words from the input string.
    """
    delimiters = [',', '.', ' ']
    words = []
    current_word = ''
    for char in s:
        if char not in delimiters:
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ''
    if current_word:  # Append the last word if it exists
        words.append(current_word)
    return words