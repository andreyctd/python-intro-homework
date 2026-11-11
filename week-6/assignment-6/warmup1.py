# Warmup 1: Default Parameters

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# 1. With only a name argument
greet("Alex")

# 2. With a name and custom greeting
greet("Alex", "Good morning")

# 3. With greeting passed as a keyword argument
greet("Alex", greeting="Hello")
