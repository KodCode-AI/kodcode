import re
import operator

def arithmetic_eval(expression):
    """
    Evaluates an arithmetic expression given as a string.
    
    Supported operations: +, -, *, (, )
    """
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    def calculate(expr):
        if isinstance(expr, int):
            return expr
        op = expr[1]
        if op == '-':
            return -calculate(expr[2])
        elif op == '*':
            return calculate(expr[2]) * calculate(expr[3])
        elif op == '+':
            return calculate(expr[2]) + calculate(expr[3])
    
    def parse_expression(expr):
        stack = []
        i = 0
        while i < len(expr):
            if expr[i].isdigit():
                start = i
                while i < len(expr) and expr[i].isdigit():
                    i += 1
                stack.append(int(expr[start:i]))
                continue
            if expr[i] in '+-*(':
                stack.append(expr[i])
                i += 1
                continue
            if expr[i] == ')':
                sub_expr = []
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()  # Remove the '('
                sub_expr.reverse()
                stack.append(calculate(sub_expr))
                i += 1
        return stack
    
    tokens = parse_expression(expression)
    return calculate(tokens)