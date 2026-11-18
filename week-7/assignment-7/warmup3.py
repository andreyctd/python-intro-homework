# Warmup 3: Use the os Module

import os

# 1. Print the current working directory
print("Current working directory:", os.getcwd())

# 2. Check if expenses.csv exists
if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Build the file path using os.path.join()
file_path = os.path.join("..", "data", "expenses.csv")
print(file_path)
