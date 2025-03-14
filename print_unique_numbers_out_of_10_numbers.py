# Initialize an empty list to store the numbers entered by the user.
numbers = []
# Loop 10 times using 'i' in range to 10
for i in range(10):
    # Prompt the user input a number.
    num = int(input(f"Enter number {i + 1}: "))
    # Add the entered number to the 'numbers' list.
    numbers.append(num)

 # Initialize an empty list to store the numbers that appear only once.
    unique_numbers = []
    # Loop through each number in the 'numbers' list.
    for num in numbers:
        # Check if the current number appears only once.
        if numbers.count(num) == 1:
            # If yes, add to the 'unique_numbers' list.
            unique_numbers.append(num)

# Print the list of numbers that don't have duplicates.
print("Numbers without duplicates:", unique_numbers)