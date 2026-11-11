# Warmup 4: Validation Function

def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100


# Ask the user for a score
score = int(input("Enter a score (0-100): "))

# Check whether the score is valid
if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")
    