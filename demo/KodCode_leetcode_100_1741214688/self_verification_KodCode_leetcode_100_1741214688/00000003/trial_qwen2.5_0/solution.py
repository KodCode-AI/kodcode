def smallest_string(s):
    """
    Returns the lexicographically smallest string after performing any number of adjacent character swaps
    where the first character has a higher ASCII value than the second character.
    """
    stack = []
    for char in s:
        while stack and stack[-1] > char:
            stack.pop()
        stack.append(char)
    return ''.join(stack)