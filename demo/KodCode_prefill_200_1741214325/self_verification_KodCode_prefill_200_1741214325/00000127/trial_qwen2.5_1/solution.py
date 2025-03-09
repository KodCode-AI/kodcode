import operator
import re

def evaluate_infix_expression(expression):
    """
    Evaluates the given infix expression and returns the result.
    Supports integers, +, -, *, /, and parentheses.
    """
    def precedence(op):
        if op in ("+", "-"):
            return 1
        if op in ("*", "/"):
            return 2
        return 0
    
    def apply_operator(operands, operators):
        op = operators.pop()
        right = operands.pop()
        left = operands.pop()
        operands.append(eval(f"{left} {op} {right}"))
    
    def evaluate(expression):
        operands = []
        operators = []
        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                start = i
                while i < len(expression) and expression[i].isdigit():
                    i += 1
                operands.append(int(expression[start:i]))
                i -= 1
            elif expression[i] in "+-*/":
                while (operators and operators[-1] != "(" and
                       precedence(operators[-1]) >= precedence(expression[i])):
                    apply_operator(operands, operators)
                operators.append(expression[i])
            elif expression[i] == "(":
                operators.append(expression[i])
            elif expression[i] == ")":
                while operators[-1] != "(":
                    apply_operator(operands, operators)
                operators.pop()  # Remove '(' from operators
            i += 1
        
        while operators:
            apply_operator(operands, operators)
        
        return operands[0]
    
    expression = re.sub(r'\s+', '', expression)
    return evaluate(expression)

# Predefined operations
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
for op in ops:
    setattr(evaluate_infix_expression, op, ops[op])