# Warmup 4: Use the datetime Module

from datetime import datetime

# Get the current date and time
today = datetime.now()

# Format and print today's date
print("Today is " + today.strftime("%B %d, %Y") + ".")
