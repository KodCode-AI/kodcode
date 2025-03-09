def is_balanced(s):
    """
    Returns True if the input string s has properly nested and balanced brackets, False otherwise.
    Handles escaped characters and nested sequences.
    """
    stack = []
    escape = False
    for i, char in enumerate(s):
        if escape:
            # Skip the character if it's escaped
            escape = False
            continue

        if char == '\\':
            # Next character is literal, skip it
            escape = True
            continue
        
        if char in '([{':
            # Push opening bracket onto the stack
            stack.append(char)
        elif char in ')]}':
            # If the stack is empty, it means there's no matching opening bracket
            if not stack:
                return False
            # Pop the last opening bracket
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False
    # If the stack is empty, all brackets were properly closed
    return not stack