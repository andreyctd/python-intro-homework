# Warmup 1: Read a Text File Line by Line

# Open the file and read it line by line
with open("../data/notes.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")
        