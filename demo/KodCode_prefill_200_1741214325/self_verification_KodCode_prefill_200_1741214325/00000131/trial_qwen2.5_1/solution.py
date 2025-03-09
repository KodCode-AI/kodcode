def reverse_string(s):
    """
    Reverses the input string without using the built-in reverse function or slicing.
    
    Parameters:
    s (str or int): The string or integer sequence to be reversed.
    
    Returns:
    str: The reversed string.
    """
    reversed_string = ''
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string