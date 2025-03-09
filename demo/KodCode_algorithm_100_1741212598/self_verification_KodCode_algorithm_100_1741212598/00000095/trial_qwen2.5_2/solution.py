def is_balanced(s: str) -> bool:
    """
    Returns True if the input string s has a properly nested sequence of brackets, considering escaped characters.
    """
    stack = []
    escape_next = False
    
    for char in s:
        if escape_next:
            escape_next = False
            continue
        
        if char == '\\':
            escape_next = True
            continue
        
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or not is_matching_pair(stack.pop(), char):
                return False
    
    return not stack

def is_matching_pair(opening: str, closing: str) -> bool:
    """
    Returns True if the given opening and closing brackets form a matching pair.
    """
    return (opening == '(' and closing == ')') or \
           (opening == '[' and closing == ']') or \
           (opening == '{' and closing == '}')