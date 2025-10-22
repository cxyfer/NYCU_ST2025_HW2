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
