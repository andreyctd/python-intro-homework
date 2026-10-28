# Warmup 2: Dictionary Operations

student = {
    "name": "Alex",
    "grade": 10,
    "subjects": ["Math", "English", "Science"]
}

# 1. Print each key-value pair using .items()
for key, value in student.items():
    print(f"{key}: {value}")

# 2. Add a new key "graduated" with the value False
student["graduated"] = False

# 3. Print the updated dictionary
print("\nUpdated dictionary:")
print(student)
