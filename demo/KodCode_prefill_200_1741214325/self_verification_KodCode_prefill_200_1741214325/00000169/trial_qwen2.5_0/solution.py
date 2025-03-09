def evaluate_postfix(expression: str) -> int:
    """
    Evaluates a postfix expression.
    :param expression: A string representing a postfix expression.
    :return: The result of the expression.
    """
    stack = []
    operators = set(['+', '-', '*', '/'])
    
    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            right = stack.pop()
            left = stack.pop()
            
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                if right == 0:
                    raise ValueError("Division by zero")
                stack.append(int(left / right))
                
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    
    return stack[0]