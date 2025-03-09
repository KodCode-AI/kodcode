def replace_substring_with_spaces(text, old_substring, new_substring):
    """
    Replace all occurrences of old_substring in text surrounded by spaces with new_substring.
    """
    import re
    pattern = r'\s' + re.escape(old_substring) + r'\s'
    return re.sub(pattern, ' ' + new_substring + ' ', text)