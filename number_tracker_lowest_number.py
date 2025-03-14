# Initialize an empty list to store numbers.
entered_numbers = []

# Prompt the user to input a number.
while True:
    try:
        num = int(input("Enter a number: "))  

        # Stores the number
        entered_numbers.append(num)  
        # check if the list is not empty before finding min.
        if entered_numbers: 
            # Show the lowest number.
            print(f"Lowest number so far: {min(entered_numbers)}")

# stops the program if invalid input.