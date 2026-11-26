# Warmup 3: Handle a Missing File

try:
    # Attempt to open the missing file
    with open("../data/missing.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('Error: "missing.txt" was not found. Please check the file path and try again.')
    