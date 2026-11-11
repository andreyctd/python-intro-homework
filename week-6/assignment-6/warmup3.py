# Warmup 3: Scope in Action

# Example 1: Local variable scope

def my_function():
    message = "Hello from inside the function!"
    print(message)


my_function()

# Trying to access the local variable outside the function:
# print(message)

# Error:
# NameError: name 'message' is not defined


# Example 2: Using return to access a value outside the function

def get_message():
    message = "Return makes the value accessible!"
    return message


# Store the returned value in an outer-scope variable
result = get_message()

# Print the result
print(result)
