def make_smallest_lexicographical_string(s: str) -> str:
    """
    Returns the lexicographically smallest string that can be obtained by 
    reversing any number of substrings in the given string `s`.
    """
    stack = []
    for char in s:
        # While the last character in the stack is greater than the current character and we can pop,
        # pop from the stack
        while stack and char < stack[-1]:
            stack.pop()
        stack.append(char)
    
    # Join the characters in the stack to form the smallest lexicographical string
    result = ''.join(stack)
    
    # Fill the remaining positions with the original characters that are not in the stack
    result += s[len(result):]
    
    return result