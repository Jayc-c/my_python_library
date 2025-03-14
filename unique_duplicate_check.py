# Track Entered Numbers (using a list instead of a set)
seen_numbers = []

# Prompt the user to input a number. (Loop)
while True:
    try:
        user_input = input("Enter a number (or anything else to stop): ")

        # Validate number input.
        number = float(user_input)
    
# Check for duplicates.
        if number in seen_numbers:
            # Display Unique/Duplicate Status.
            print("Duplicate")
        else:
            # Display Unique/Duplicate Status.
            print("Unique")
            # Record Unique Number.
            seen_numbers.append(number)

# Stop on invalid input.
    except ValueError:
        break