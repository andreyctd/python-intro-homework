# Warmup 2: Read a CSV with DictReader

import csv

# Open the CSV file and read it using DictReader
with open("../data/students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        print(f"{student['name']}: {student['score']}")
