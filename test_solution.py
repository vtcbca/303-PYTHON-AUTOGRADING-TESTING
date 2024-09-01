import unittest
from solution import factorial  # Import the student's solution

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        # Test factorial of 0
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        # Test factorial of 1
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive_integer(self):
        # Test factorial of a positive integer (e.g., 5)
        self.assertEqual(factorial(5), 120)

    def test_factorial_large_number(self):
        # Test factorial of a larger number (e.g., 10)
        self.assertEqual(factorial(10), 3628800)

if __name__ == "__main__":
    unittest.main()
