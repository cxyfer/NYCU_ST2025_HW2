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
        result = 0
        if op == "+":
            result = self.add(a, b)
        elif op == "-":
            result = self.subtract(a, b)
        elif op == "*":
            result = self.multiply(a, b)
        elif op == "/":
            result = self.divide(a, b)
        else:
            raise ValueError(f"Invalid operator: {op}")
        return result
