# Initialize and empty list to store numbers.
numbers = []  

# Loop until invalid input.
while True:
    try:
        # Prompt user to input a number
        num = float(input("Enter a number: "))  
        # Store number to the list.
        numbers.append(num)

    # Stop on non-number input.
    except ValueError:
        break  

# If at least one number was entered.
if numbers:  
    # Calculate average.
    average = sum(numbers) / len(numbers)  

# Print the average.
# Else, no input message.