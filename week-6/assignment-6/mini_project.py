# Mini-Project: Refactor the Number Cruncher

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93,
           31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


# Find the minimum value using a loop
def find_min(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


# Find the maximum value using a loop
def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


# Search for a target and return its index
def search(numbers, target):
    for index in range(len(numbers)):
        if numbers[index] == target:
            return index

    return -1


# Bubble sort without modifying the original list
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    for i in range(len(sorted_numbers)):
        for j in range(len(sorted_numbers) - 1 - i):
            if sorted_numbers[j] > sorted_numbers[j + 1]:
                sorted_numbers[j], sorted_numbers[j + 1] = (
                    sorted_numbers[j + 1],
                    sorted_numbers[j]
                )

    return sorted_numbers


# Display the menu and get the user's choice
def show_menu():
    print("\n===== NUMBER CRUNCHER =====")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a Number")
    print("4. Sort Numbers")
    print("5. Show Original Numbers")
    print("6. Exit")

    choice = input("Enter your choice: ")
    return choice


# Main program loop
def main():
    while True:
        choice = show_menu()

        if choice == "1":
            print("Minimum:", find_min(numbers))

        elif choice == "2":
            print("Maximum:", find_max(numbers))

        elif choice == "3":
            target = int(input("Enter number to search for: "))
            result = search(numbers, target)

            if result != -1:
                print(f"Found at index {result}")
            else:
                print("Not found")

        elif choice == "4":
            print("Sorted numbers:", bubble_sort(numbers))

        elif choice == "5":
            print("Original numbers:", numbers)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()
