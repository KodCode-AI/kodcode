def evaluate_postfix(expression: str) -> int:
    """
    Evaluates a postfix (Reverse Polish Notation) expression.
    
    Args:
    expression (str): A string representing a postfix expression.
    
    Returns:
    int: The result of the evaluation.
    """
    stack = []
    for term in expression.split():
        if term.isdigit():  # if the term is a number, push it onto the stack
            stack.append(int(term))
        else:  # if the term is an operation
            b = stack.pop()
            a = stack.pop()
            if term == '+':
                stack.append(a + b)
            elif term == '-':
                stack.append(a - b)
            elif term == '*':
                stack.append(a * b)
            elif term == '/':
                stack.append(int(a / b))  # use int to truncate towards zero
            else:
                raise ValueError(f"Unsupported operation: {term}")
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]