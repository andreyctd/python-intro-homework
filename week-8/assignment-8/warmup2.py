# Warmup 2: Safe Division

try:
    # Ask the user for two numbers
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # Perform division
    result = numerator / denominator

    print(f"{numerator} ÷ {denominator} = {result}")

except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")
    