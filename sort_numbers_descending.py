# List to store numbers.
numbers = []  

# Loop until invalid input.
while True:  
    try:
        # Prompt user to input a number
        num = float(input("Enter a number: ")) 
        # Store the number to list.
        numbers.append(num)

# Stop on non-number input.
# Sort from highest to lowest.
# Display the sorted numbers.
# Else, no input message.