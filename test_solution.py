import unittest
import subprocess

class TestFactorialProgram(unittest.TestCase):
    def run_program(self, input_value):
        # Run the student's program and capture the output
        result = subprocess.run(
            ["python3", "solution.py"], input=input_value, text=True, capture_output=True
        )
        return result.stdout.strip()

    def test_factorial_zero(self):
        output = self.run_program("0\n")
        self.assertEqual(output, "1")

    def test_factorial_one(self):
        output = self.run_program("1\n")
        self.assertEqual(output, "1")

    def test_factorial_positive_integer(self):
        output = self.run_program("5\n")
        self.assertEqual(output, "120")

    def test_factorial_large_number(self):
        output = self.run_program("10\n")
        self.assertEqual(output, "3628800")

    def test_factorial_negative_number(self):
        output = self.run_program("-10\n")
        self.assertEqual(output, "Error: Enter negative value")

if __name__ == "__main__":
    unittest.main()
