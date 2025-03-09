def replace_surrounded_substring(text, old_substring, new_substring):
    """
    Replace all occurrences of old_substring in text with new_substring,
    but only when the old_substring is surrounded by spaces.
    """
    pattern = r'\b' + re.escape(old_substring) + r'\b'
    return re.sub(pattern, new_substring, text)