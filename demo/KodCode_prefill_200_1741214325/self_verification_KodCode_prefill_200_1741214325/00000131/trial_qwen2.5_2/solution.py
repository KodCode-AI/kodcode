def reverse_string(input_str):
    """
    Reverses the input string without using built-in reverse functions or slicing.
    
    Parameters:
    input_str (str or int): The input string or integer sequence to reverse.
    
    Returns:
    str: The reversed string.
    """
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str