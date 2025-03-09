def evaluate_infix_expression(expression: str) -> float:
    """
    Evaluates an infix expression and returns the result.
    """
    import math
    import operator
    
    def apply_operator(operands, operators):
        right = operands.pop()
        left = operands.pop()
        op = operators.pop()
        oper = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        return operands.append(oper[op](left, right))

    def greater_precedence(op1, op2):
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedences[op1] > precedences[op2]

    operators = []
    operands = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        elif expression[i] in '0123456789.':
            num = 0
            while i < len(expression) and (expression[i] in '0123456789.' or expression[i] == ' '):
                if expression[i] != ' ':
                    num = (num * 10) + int(expression[i])
                    i += 1
                else:
                    i += 1
            operands.append(num)
        elif expression[i] in '+-*/':
            while (operators and operators[-1] != '(' and
                   greater_precedence(operators[-1], expression[i])):
                apply_operator(operands, operators)
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operands, operators)
            operators.pop()  # Remove the '(' from the stack
            i += 1

    while operators:
        apply_operator(operands, operators)

    return operands[-1]