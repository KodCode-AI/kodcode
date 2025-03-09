def evaluate_expression(expression: str) -> int:
    """
    Evaluates an arithmetic expression given as a string.
    The expression includes integers, the operators '+', '-', '*', and '(', ')'.
    
    :param expression: str, the arithmetic expression to evaluate
    :return: int, the result of the evaluation
    """
    def compute(operands, operators):
        right = operands.pop()
        left = operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)
        elif op == '*':
            operands.append(left * right)

    def parse(expression):
        num = 0
        operands, operators = [], []
        i, n = 0, len(expression)
        while i < n:
            if expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
                if i == n or not expression[i].isdigit():
                    operands.append(num)
                    num = 0
            elif expression[i] in '+-*/':
                while operators and operators[-1] != '(' and (expression[i] in '+-' or (expression[i] in '*/' and operators[-1] in '*/')):
                    compute(operands, operators)
                operators.append(expression[i])
                i += 1
            elif expression[i] == '(':
                operators.append(expression[i])
                i += 1
            elif expression[i] == ')':
                while operators[-1] != '(':
                    compute(operands, operators)
                operators.pop()  # Remove '(' from stack
                i += 1
        while operators:
            compute(operands, operators)
        return operands[-1]

    return parse(expression)