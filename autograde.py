import os

# Define the test cases
test_cases = [
    (5, 120),   # Factorial of 5
    (0, 1),     # Factorial of 0
    (10, 3628800),  # Factorial of 10
    (-5, "Error"),  # Factorial of a negative number
    (1, 1)     
]

# Function to grade a student's factorial function
def grade_factorial(student_code):
    try:
        # Execute the student's code
        exec(student_code)

        # Access the factorial function defined by the student
        factorial = locals().get('factorial')
        if not factorial:
            return 0, "Function not found"

        score = 0
        for case in test_cases:
            input_val, expected_output = case
            try:
                result = factorial(input_val)
                if result == expected_output:
                    score += 5
            except Exception as e:
                if input_val < 0 and str(e) == "Error":
                    score += 5
                else:
                    return score, f"Failed on input {input_val}: {e}"

        return score, "Passed"

    except Exception as e:
        return 0, f"Error running code: {e}"

# Load the student's code from the solution.py file
with open('solution.py', 'r') as file:
    student_code = file.read()

score, feedback = grade_factorial(student_code)

# Save the autograding results
with open('autograde_results.txt', 'w') as result_file:
    result_file.write(f"Score: {score}\n")
    result_file.write(f"Feedback: {feedback}\n")

print("Autograding complete. Results saved to 'autograde_results.txt'.")
