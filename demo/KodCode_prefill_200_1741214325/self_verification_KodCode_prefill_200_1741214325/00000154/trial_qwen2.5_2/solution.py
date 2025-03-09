def split_string_into_words(s: str):
    """
    Splits a given string into words based on the delimiters: ',', '.', and ' '.
    """
    delimiters = [',', '.', ' ']
    words = []
    current_word = ''
    for char in s:
        if char in delimiters:
            if current_word:  # If there is a non-empty word to add
                words.append(current_word)
                current_word = ''
        else:
            current_word += char
    if current_word:  # Add the last word if any
        words.append(current_word)
    return words