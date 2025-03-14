# Initialize an empty list to store the numbers entered by the user.
numbers = [] 

# Prompt the user to input 20 numbers.
for i in range(10):
    num = int(input(f"Enter your {i + 1} number: "))  
    # Store the number. 
    numbers.append(num)  

# Display the numbers that don't have duplicates
# Check each number in the list
# Check if unique.
# Print unique number.