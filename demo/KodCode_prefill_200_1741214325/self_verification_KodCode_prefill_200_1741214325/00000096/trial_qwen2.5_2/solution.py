def evaluate_expression(expression: str) -> int:
    """
    Evaluates an arithmetic expression given as a string.
    The expression can include integers, the operators '+', '-', '*', 
    and '(', ')'.
    """
    def compute(nums, ops):
        while len(ops) > 0:
            cur_op = ops.pop()
            if cur_op == '+':
                nums[-2] += nums[-1]
                nums.pop()
            elif cur_op == '-':
                nums[-2] -= nums[-1]
                nums.pop()
            elif cur_op == '*':
                nums[-2] *= nums[-1]
                nums.pop()
    
    def evaluate(parens):
        nums, ops = [], []
        idx = 0
        while idx < len(parens):
            if parens[idx].isdigit():
                num = 0
                while idx < len(parens) and parens[idx].isdigit():
                    num = num * 10 + int(parens[idx])
                    idx += 1
                nums.append(num)
                idx -= 1
            elif parens[idx] == '(':
                temp = evaluate(parens[idx+1:])
                nums.append(temp[0])
                idx += temp[1]
            elif parens[idx] == '+' or parens[idx] == '-' or parens[idx] == '*':
                while len(ops) > 0 and ops[-1] != '(' and precedence[ops[-1]] >= precedence[paresns[idx]]:
                    compute(nums, ops)
                ops.append(parens[idx])
            idx += 1
        while len(ops) > 0:
            compute(nums, ops)
        return nums[0]

    precedence = {'+': 1, '-': 1, '*': 2}
    return evaluate(expression)