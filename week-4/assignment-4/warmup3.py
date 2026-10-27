# Warmup 3: Set Operations

# Create two lists of programming languages
languages1 = ["Python", "JavaScript", "Java", "C++"]
languages2 = ["Python", "Ruby", "JavaScript", "Go"]

# Convert each list to a set
set1 = set(languages1)
set2 = set(languages2)

# 1. Union: all languages from both sets, without duplicates
print("Union:", set1 | set2)

# 2. Intersection: languages found in both sets
print("Intersection:", set1 & set2)

# 3. Difference: languages only in the first set
print("Difference:", set1 - set2)
