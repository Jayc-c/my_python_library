# Initialize an empty list to store numbers.
numbers = []

# Prompt the user to input a number.
while True:
    try:
        value = float(input("Enter a number: "))

        # Store the number.
        numbers.append(value)
        # Sort the list of number.
        numbers.sort()
        # Display current sorted list.
        print("Sorted:", numbers)

# Stop on invalid input.