def string_to_list_of_words(s):
    """
    Convert a string into a list of words.
    
    Args:
        s (str): The input string.
    
    Returns:
        list: A list of words from the input string.
    """
    return s.split()

# Example usage
print(string_to_list("Hello world"))  # ["Hello", "world"]