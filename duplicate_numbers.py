# Initialize an empty list for storing entered number
entered_numbers = []

# Ask user 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    entered_numbers.append(num)

# Initialize an empty list for counting duplicate numbers
duplicate_numbers = []

# Track duplicates
for num in entered_numbers:
    if entered_numbers.count(num) > 1 and num not in duplicate_numbers:
        duplicate_numbers.append(num)

# Display numbers that have duplicate