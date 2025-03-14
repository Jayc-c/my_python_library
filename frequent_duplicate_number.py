 # Initialize an empty list to store numbers.
entered_numbers = [] 

# Prompt user to input numbers.
while True:
    try:
        num = int(input('Enter number: '))   
        # Store the number to the list.
        entered_numbers.append(num)

        # Get the unique numbers from the list.       
        unique_numbers = set(entered_numbers)
        # Find the number that appears most often.
        most_frequent = max(unique_numbers, key=entered_numbers.count)
        # Count how many times the most frequent number appears.
        count = entered_numbers.count(most_frequent)

# Display the most frequent number and its count.
# Stops the program if invalid input.     