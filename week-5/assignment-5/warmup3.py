# Warmup 3: Linear Search

names = ["Jazmine", "Luis", "Sara", "Marcus", "Priya", "Devon", "Mia", "Eli"]

search_name = input("Enter a name to search for: ")

found = False

for index in range(len(names)):
    if names[index] == search_name:
        print(f'Found "{search_name}" at index {index}.')
        found = True
        break

if not found:
    print(f'"{search_name}" was not found in the list.')
