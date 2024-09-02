import xml.etree.ElementTree as ET
import csv

# Define the total points per test case
POINTS_PER_TEST = 5
TOTAL_TESTS = 5  # Adjust this according to the number of tests you have

# Parse the JUnit XML result file
tree = ET.parse('results/results.xml')
root = tree.getroot()

# Open CSV file to write scores
with open('results/scores.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student', 'Score'])

    # Extract relevant information
    for testcase in root.iter('testcase'):
        student_name = testcase.attrib['classname']  # Assuming the student's name is stored here
        # Calculate the score from 25
        failures = len(testcase.findall('failure'))
        passed_tests = TOTAL_TESTS - failures
        score = passed_tests * POINTS_PER_TEST
        writer.writerow([student_name, score])
