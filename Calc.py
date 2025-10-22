from typing import Union

class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def subtract(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> Union[int, float]:
        if float(b) == 0.0:
            return float("inf")
        return int(a / b) if a % b == 0 else a / b

    def compute(self, a: int, b: int, op: str) -> Union[int, float]:
        ops_map = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
        }
        if op not in ops_map:
            raise ValueError(f"Invalid operator: {op}")
        return ops_map[op](a, b)

    def _parse_tokens(self, expression: str) -> list[str]:
        n = len(expression)
        tokens = []
        i = 0
        while i < n:
            if expression[i] == ' ':
                i += 1
                continue
            if expression[i].isdigit():
                j = i
                while j < n and expression[j].isdigit():
                    j += 1
                tokens.append(expression[i:j])
                i = j
            elif expression[i] in "+-*/()":
                tokens.append(expression[i])
                i += 1
            else:
                raise ValueError(f"Invalid character: {expression[i]}")
        return tokens

    def eval(self, expression: str) -> Union[int, float]:
        priority_map = {
            '(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }
        
        tokens = self._parse_tokens(expression)
        nums, ops = [], []

        def helper():
            if len(nums) < 2 or len(ops) < 1:
                raise ValueError("Invalid expression")
            b, a = nums.pop(), nums.pop()
            op = ops.pop()
            nums.append(self.compute(a, b, op))

        for i, token in enumerate(tokens):
            if token.isdigit():
                nums.append(int(token))
            elif token == '(':
                ops.append(token)
            elif token == ')':
                # calculate until meet '('
                while ops and ops[-1] != '(':
                    helper()
                ops.pop()  # pop '('
            elif token in priority_map:
                # handle unary operator
                if i == 0 or tokens[i-1] in ['(', '+', '-', '*', '/']:
                    if token == '+' or token == '-':
                        nums.append(0)
                while ops and priority_map[ops[-1]] >= priority_map[token]:
                    helper()
                ops.append(token)
            else:
                raise ValueError(f"Invalid token: {token}")
        while ops:
            helper()
        return nums[0]