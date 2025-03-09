def is_balanced(s: str) -> bool:
    """
    Checks if the input string s has balanced brackets, considering escape characters.
    Escaped characters treat the next character as literal.
    """
    stack = []
    escape = False
    for i, char in enumerate(s):
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char in '([{':
            stack.append(char)
        elif char in '}])':
            if not stack or stack[-1] == '{' and char != '}' or stack[-1] == '(' and char != ')' or stack[-1] == '[' and char != ']':
                return False
            stack.pop()
        else:
            # Ignore other characters
            continue
    return not stack