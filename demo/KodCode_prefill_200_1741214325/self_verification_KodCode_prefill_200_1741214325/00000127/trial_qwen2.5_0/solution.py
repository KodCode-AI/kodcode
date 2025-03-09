def evaluate_infix_expression(expression):
    """
    Evaluates the value of an infix expression.
    """
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    def greater_precedence(op1, op2):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        return precedence[op1] > precedence[op2]

    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j
        elif expression[i] in '+-*/':
            while (operators and greater_precedence(operators[-1], expression[i])):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1
    while operators:
        apply_operator(operators, values)

    return values[0]