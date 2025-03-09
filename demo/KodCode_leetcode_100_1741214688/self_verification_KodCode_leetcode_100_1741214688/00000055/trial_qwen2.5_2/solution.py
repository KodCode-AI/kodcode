def smallest_string(s):
    """
    Returns the lexicographically smallest string that can be obtained by replacing
    any two adjacent characters with their lexicographically smallest character.
    """
    stack = []
    for char in s:
        # Keep popping the stack until it's empty or the top of the stack is smaller than the current character
        while stack and stack[-1] > char:
            stack.pop()
        stack.append(char)
    return ''.join(stack)