# Initialize an empty list to store numbers
numbers = []  

# Prompt the user to input numbers
while True:
    try:
        num = float(input("Enter a number: "))
        # Store the number to the list.
        numbers.append(num)  

    except ValueError:
        # Check if the list is not empty.
        if numbers: 
            # Check if the list is not empty.
            print(f"Numbers entered: {numbers}")
            # Find and print the max number
            print(f"Highest: {max(numbers)}") 

# Find and print the max number
# Stop on invalid input.