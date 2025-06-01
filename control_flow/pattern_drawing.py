# pattern_drawing.py

# Prompt user to enter the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))

    if size <= 0:
        print("Please enter a positive integer.")
    else:
        row = 0
        while row < size:
            for col in range(size):
                print("*", end="")
            print()  # Move to the next line after one row is printed
            row += 1

except ValueError:
    print("Invalid input. Please enter a positive integer.")
