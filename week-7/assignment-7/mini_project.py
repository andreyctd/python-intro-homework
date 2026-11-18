# Mini-Project — Expense Report Generator

import os
import csv
from datetime import datetime

# 1. Check if expenses.csv exists
file_path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(file_path):
    print("Error: expenses.csv not found.")
    raise SystemExit

# 2. Read the CSV file into a list of dictionaries
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    expenses = list(reader)

# 3. Convert amount to float for each expense
for expense in expenses:
    expense["amount"] = float(expense["amount"])

# 4. Filter expenses to include only Food
food_expenses = [
    expense for expense in expenses
    if expense["category"] == "Food"
]

# 5. Calculate the total Food expenses
total = sum(expense["amount"] for expense in food_expenses)

# 6. Get today's date
today = datetime.now().strftime("%B %d, %Y")

# 7. Write the report to food_report.txt
with open("food_report.txt", "w") as file:
    file.write(f"Food Expense Report — generated {today}\n")

    for expense in food_expenses:
        file.write(
            f"{expense['date']}: ${expense['amount']:.2f}\n"
        )

    file.write(f"Total: ${total:.2f}\n")

print("Food expense report generated successfully!")
