# daily_reminder.py

# Prompt for the task description
task = input("Enter your task: ")

# Prompt for priority level
priority = input("Priority (high/medium/low): ").strip().lower()

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case for priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unrecognized priority"

# Use if statement for time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ("high", "medium"):
        message += ". Make sure to address it soon."
    else:
        message += ". Consider completing it when you have free time."

# Print final reminder
print(message)
