import xml.etree.ElementTree as ET
import csv

# Parse the JUnit XML result file
tree = ET.parse('results/results.xml')
root = tree.getroot()

# Open CSV file to write scores
with open('results/scores.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Student', 'Score'])

    # Extract relevant information
    for testcase in root.iter('testcase'):
        name = testcase.attrib['name']
        time = testcase.attrib['time']
        score = 25 if not testcase.find('failure') else 0  # Simplified example
        writer.writerow([name, score])
