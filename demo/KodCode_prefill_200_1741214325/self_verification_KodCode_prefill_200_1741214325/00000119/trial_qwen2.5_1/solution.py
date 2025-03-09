def replace_surrounded_substring(text, old_substring, new_substring):
    """
    Replaces all occurrences of old_substring in text that are surrounded by spaces with new_substring.
    """
    pattern = r'\b{}\b'.format(re.escape(old_substring))
    return re.sub(pattern, new_substring, text)