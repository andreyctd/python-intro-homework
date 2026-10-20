# Mini-Project: Day Planner

day = input("What day is it? ").strip().lower()
time_of_day = input("What time of day? ").strip().lower()

if day not in ["monday", "tuesday", "saturday"]:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, or Saturday.")
elif time_of_day not in ["morning", "afternoon", "evening"]:
    print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening.")
else:
    if day == "monday" and time_of_day == "morning":
        suggestion = "Start the week with a Python lesson — great time to focus!"
    elif day == "monday" and time_of_day == "afternoon":
        suggestion = "Practice coding and work on your assignments."
    elif day == "monday" and time_of_day == "evening":
        suggestion = "Relax and plan your goals for the week."

    elif day == "tuesday" and time_of_day == "morning":
        suggestion = "Review your notes and learn something new."
    elif day == "tuesday" and time_of_day == "afternoon":
        suggestion = "Take a break and go for a walk outside."
    elif day == "tuesday" and time_of_day == "evening":
        suggestion = "Spend some time playing guitar."

    elif day == "saturday" and time_of_day == "morning":
        suggestion = "Enjoy breakfast and get some fresh air."
    elif day == "saturday" and time_of_day == "afternoon":
        suggestion = "Go to the beach or play tennis."
    else:
        suggestion = "Perfect night for a movie or trying a new recipe."

    print(f"Suggestion: {suggestion}")
    