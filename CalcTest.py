import unittest
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)  # Expect 5 - 3 = 2

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 3)
        self.assertEqual(result, 12)  # Expect 4 × 3 = 12

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)  # Expect 10 ÷ 2 = 5 (int)
        self.assertIsInstance(result, int)  # Expect result to be an integer
        result = calc.divide(10, 3)
        self.assertAlmostEqual(result, 3.333333, places=5)  # Expect 10 ÷ 3 ≈ 3.33333
        result = calc.divide(10, 0)
        self.assertEqual(result, float("inf"))  # Expect 10 ÷ 0 = inf

    def test_compute(self):
        calc = Calculator()
        result = calc.compute(1, 2, "+")
        self.assertEqual(result, 3)
        result = calc.compute(1, 2, "-")
        self.assertEqual(result, -1)
        result = calc.compute(1, -2, "*")
        self.assertEqual(result, -2)
        result = calc.compute(1, 2, "/")
        self.assertEqual(result, 0.5)
        with self.assertRaises(ValueError):
            calc.compute(1, 2, "$")

    def test_eval_simple(self):
        """
        The expression of the test should be strictly separated by spaces.
        """
        calc = Calculator()
        expressions = [
            "1 + 1",
            "2 - 1 + 2",
            "( 1 + 2 ) * 3",
            "4 / ( ( 1 + 2 ) * 3 + 1 ) + 5",
        ]
        for expression in expressions:
            result = calc.eval(expression)
            self.assertEqual(result, eval(expression))

    def test_eval_complex(self):
        calc = Calculator()
        expressions = [
            "(1+(4+5+2)-3)+(6+8)",
            "(2+6*3+5-(3*14/7+2)*5)+3",
            "(0-3)/4",
        ]
        for expression in expressions:
            result = calc.eval(expression)
            self.assertEqual(result, eval(expression))

if __name__ == "__main__":
    unittest.main()
