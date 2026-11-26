# Part 2: Mini-Project — Defensive CSV Reader

import csv

# Store valid rows and skipped row descriptions
clean_data = []
skipped_rows = []
rows_attempted = 0

# 1. Open the CSV file safely
try:
    with open("../data/messy_data.csv", "r") as file:

        # 2. Read the CSV using DictReader
        reader = csv.DictReader(file)

        # 3. Process each row
        for row_number, row in enumerate(reader, start=1):
            rows_attempted += 1

            # Check for extra columns
            if None in row:
                skipped_rows.append(
                    f"Row {row_number}: extra column detected — skipped"
                )
                continue

            try:
                # Convert amount to float
                amount = float(row["amount"])

                # Check required values
                name = row["name"]
                category = row["category"]

                if not name or not category:
                    raise ValueError("missing name or category")

                # 4. Store successfully parsed rows
                clean_data.append({
                    "name": name,
                    "category": category,
                    "amount": amount
                })

            except ValueError as error:
                skipped_rows.append(
                    f"Row {row_number}: ValueError — {error}"
                )

            except KeyError as error:
                skipped_rows.append(
                    f"Row {row_number}: KeyError — missing column {error}"
                )

except FileNotFoundError:
    print('Error: "messy_data.csv" was not found. Please check the file path.')
    raise SystemExit

# 5. Print the summary
rows_parsed = len(clean_data)
rows_skipped = len(skipped_rows)

print("=== CSV Report ===")
print(f"Rows attempted:  {rows_attempted}")
print(f"Rows parsed:     {rows_parsed}")
print(f"Rows skipped:    {rows_skipped}")

print("\nSkipped rows:")

for skipped in skipped_rows:
    print(f"  {skipped}")

print("\nClean data:")

for item in clean_data:
    print(
        f"  {item['name']} | {item['category']} | "
        f"${item['amount']:.2f}"
    )
