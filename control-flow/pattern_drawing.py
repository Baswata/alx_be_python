# pattern_drawing.py

# Prompt user for size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate through rows
while row < size:
    # Use for loop to print asterisks in a row
    for _ in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1
