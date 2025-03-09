def smallest_string(s):
    """
    Returns the lexicographically smallest string that can be obtained by swapping adjacent characters
    in the given string 's' any number of times according to the specified rule.
    """
    stack = []
    for char in s:
        # Keep popping from stack until the current character is smaller than the character at the top
        # of the stack. This ensures the string remains lexicographically smallest.
        while stack and stack[-1] > char:
            stack.pop()
        stack.append(char)
    return ''.join(stack)