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


if __name__ == "__main__":
    unittest.main()
