# Initialize an empty list for storing entered number
entered_numbers = []

# Ask user 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    entered_numbers.append(num)

# Initialize an empty list for counting duplicate numbers
# Track duplicates
# display numbers that have duplicate