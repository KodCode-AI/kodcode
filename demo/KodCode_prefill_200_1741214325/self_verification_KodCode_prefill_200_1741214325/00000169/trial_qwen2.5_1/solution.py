def evaluate_postfix(expression):
    """
    Evaluates a postfix expression (also known as Reverse Polish Notation).
    
    Arguments:
    expression -- A string containing the postfix expression to be evaluated.
    
    Returns:
    The result of the postfix expression evaluation.
    """
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit():  # Check if the token is a digit
            stack.append(int(token))
        else:
            # Pop the last two elements from the stack
            right_operand = stack.pop()
            left_operand = stack.pop()
            # Perform the operation
            if token == '+':
                stack.append(left_operand + right_operand)
            elif token == '-':
                stack.append(left_operand - right_operand)
            elif token == '*':
                stack.append(left_operand * right_operand)
            elif token == '/':
                stack.append(left_operand // right_operand)  # Integer division
    
    # The result will be the only element left in the stack
    return stack.pop()